'''
Predict pipeline
'''
import logging
import argparse

import joblib
import pandas as pd
from password_complexity.metrics.metrics import *
from password_complexity.features.generate import generate_features
from password_complexity.utils.config import load_config
from password_complexity.utils.logger import get_logger
from password_complexity.utils.hyperparameters import params_distribution

import os
from pathlib import Path


def predict_model(password: str, config_path:Path) -> float:
    # config_path=Path.cwd().joinpath('CONFIG_PATH.yaml') # лучше передавать путь к конфигу параметром
    logging.info('loading config...')
    config_=load_config(config_path)

    logger = get_logger('Make dataset...', config_.base.log_level)
    df  = pd.DataFrame({'Password...' : [password]})

    logger = get_logger('Generate features...', config_.base.log_level)
    df = generate_features(df)

    logger = get_logger('Load model...', config_.base.log_level)
    model=joblib.load(config_.train_model.model_path)

    logger = get_logger('predict model...', config_.base.log_level)
    prediction=model.predict(df)[0]
    logging.info('result:', prediction)
    return prediction

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--password', dest='password', required=True)
    args_parser.add_argument('--config', dest='config', required=True)
    args=args_parser.parse_args()
    config_path = Path(args.config)
    password = args.password
    predict_model(password=password, config_path=config_path)