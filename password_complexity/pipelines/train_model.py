'''
Train pipeline and save best result
'''
##### Add arguments #####
import argparse
#########################

##### custom lib and metrics #####
from password_complexity.metrics.metrics import rmsle_score, RMSLE_score, RMSLE
from password_complexity.features.generate import generate_features
from password_complexity.utils.config import load_config
from password_complexity.metrics.metrics import *
from password_complexity.utils.hyperparameters import params_distribution
from password_complexity.utils.pipeline_structure import create_pipeline_structure
#################################

##### Preprocessing #####
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
#########################

##### Path lib #####
import os
from pathlib import Path
import joblib
####################

##### dataset instruments #####
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
###############################

##### Model structure #####
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
###########################

##### Models #####
from sklearn.linear_model import LinearRegression
##################

##### hyperparams optimize #####
import optuna
from optuna.integration import OptunaSearchCV
from optuna.distributions import *
################################

def train_model(config_path: Path) -> float:
    """
    train pipeline
    1) load previous pipeline and validate on test_dataset

    2) create new pipeline with space of hyperpamaters, optimised with optuna

    3)compare two pipelines with RMSLE score

    4)save best result
    """
    config_ = load_config(config_path)
    print('загружаем конфиг', config_)
    df=pd.read_csv(config_.make_dataset.train_dataset)

    df=generate_features(df)
    print('читаем датасет и генерим фичи')

    y = df['Times']
    X = df.drop('Times', axis=1)
    print('разбиваем на таргет и лейбл')
    X_train, X_test, y_train, y_test = train_test_split(
                                                        X,y, 
                                                        train_size=config_.train_model.train_size, 
                                                        random_state=config_.base.random_state
                                                       )
    print('разбиваем на обучение и тест', X_train.shape, X_test.shape)

    X_train=X_train.iloc[:100000]
    y_train=y_train.iloc[:100000]

    model = joblib.load(config_.train_model.model_path)
    # импортируем старую модель
    print('импортирем старую модель')

    ## Создаем списки коннилчественных
    ## и категориальных столбцов
    cat_columns = X_train.dtypes[X_train.dtypes == 'object'].index
    num_columns = X_train.dtypes[X_train.dtypes != 'object'].index

    pipe = create_pipeline_structure(num_columns, cat_columns)
    print('Создаем пайплайн для обучения', pipe)

    optuna_search = OptunaSearchCV(
                                pipe,
                                params_distribution,
                                scoring=RMSLE_score,
                                random_state=config_.base.random_state,
                                n_trials=5,
                                verbose=1,
                                cv=5
                                )


    optuna_search.fit(X_train, y_train)
    print("обучаем новый пайплайн на крос валидации с нашей кастомной метрикой")

    old_rmsle=np.abs(RMSLE(y_test, model.predict(X_test)))
    new_rmsle=np.abs(RMSLE(y_test, optuna_search.best_estimator_.predict(X_test)))
    print('old_rmsle , new_rmsle', old_rmsle, new_rmsle)
    if new_rmsle < old_rmsle:
        print('Модель улучшилась, сохраняем новую модель...')
        joblib.dump(optuna_search.best_estimator_, config_.train_model.model_path)

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args=args_parser.parse_args()
    config = args.config
    train_model(config_path=config)
