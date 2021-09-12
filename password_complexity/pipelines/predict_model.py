'''
Train pipeline and save best result
'''
import argparse

import joblib
import pandas as pd
from password_complexity.features.generate import generate_features
from password_complexity.utils.config import load_config
from password_complexity.metrics.metrics import *
from password_complexity.utils.hyperparameters import params_distribution

import os
from pathlib import Path


# print('текущий путь',os.path.abspath(''))
# print()
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

def predict_model(password: str, config_path:Path) -> float:
    # config_path=Path.cwd().joinpath('CONFIG_PATH.yaml') # лучше передавать путь к конфигу параметром
    config_=load_config(config_path)
    
    df  = pd.DataFrame({'Password' : [password]})
    df = generate_features(df)

    model=joblib.load(config_.train_model.model_path)

    prediction=model.predict(df)[0]
    print('result:', prediction)
    return prediction

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--password', dest='password', required=True)
    args_parser.add_argument('--config', dest='config', required=True)
    args=args_parser.parse_args()
    config_path = Path(args.config)
    password = args.password
    predict_model(password=password, config_path=config_path)