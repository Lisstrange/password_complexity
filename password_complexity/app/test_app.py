import pandas as pd
import numpy as np
import box
import joblib
from password_complexity.features.generate import generate_features
from password_complexity.utils.config import load_config
from password_complexity.metrics.metrics import rmsle_score, RMSLE_score, RMSLE

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

from flask import Flask, request, render_template

import os
from pathlib import Path


print('текущий путь',os.path.abspath(''))
print()
print()
config_path=Path.cwd().joinpath('CONFIG_PATH.yaml')
print('путь к файлу со всеми путями',config_path)
print()
print()
config_=load_config(config_path)
print(config_)
model=joblib.load(config_.train_model.model_path)
print(model)
print()
print()


print(config_.make_dataset.train_dataset)
train=pd.read_csv(config_.make_dataset.train_dataset)
train=generate_features(train)

y_train = train['Times']
X_train = train.drop('Times', axis=1)


preds=model.predict(X_train.iloc[15000:30000])
y_valid=y_train[15000:30000]

print(RMSLE(y_valid, preds))
