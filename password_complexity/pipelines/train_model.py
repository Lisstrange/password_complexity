'''
Train pipeline and save best result
'''

##### custom lib and metrics #####
from password_complexity.metrics.metrics import rmsle_score, RMSLE_score, RMSLE
from password_complexity.features.generate import generate_features
from password_complexity.utils.config import load_config
from password_complexity.metrics.metrics import *
from password_complexity.utils.hyperparameters import params_distribution


##### common lib #####
import os
from pathlib import Path
import joblib

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from re import X
import argparse






# print()
config_path=Path.cwd().joinpath('CONFIG_PATH.yaml')
# print('путь к файлу со всеми путями',config_path)
# print()
# print()
config_=load_config(config_path)
# print(config_)
model=joblib.load(config_.train_model.model_path)
# print(model)
# print()
# print()


# print(config_.make_dataset.train_dataset)


# train=pd.read_csv(config_.make_dataset.train_dataset)
# train=generate_features(train)

# y_train = train['Times']
# X_train = train.drop('Times', axis=1)


# preds=model.predict(X_train.iloc[15000:30000])
# y_valid=y_train[15000:30000]

# print(RMSLE(y_valid, preds))

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
    

    model = joblib.load(config_.train_model.model_path)
    # импортируем старую модель

    
    config_.make_dataset.train_dataset

    return ''