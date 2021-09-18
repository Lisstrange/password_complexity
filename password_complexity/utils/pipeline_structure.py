"""
Make pipeline schema
"""

##### Add arguments #####
import argparse
#########################

##### Model structure #####
from typing import List
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
###########################

##### Models #####
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
##################

##### Preprocessing #####
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
#########################



def create_pipeline_structure(num_columns : List, cat_columns: List) -> Pipeline:
        
    ## Cоздаем конвейер для количественных переменных
    num_pipe = Pipeline([
        ('imputer', SimpleImputer()),
        ('scaler', StandardScaler())
    ])

    # Создаем конвейер для категориальных переменных
    cat_pipe = Pipeline([
        ('imputer', SimpleImputer()),
        ('feature_encoding', OneHotEncoder(sparse=False, handle_unknown='ignore'))
    ])
    # создаем список трехэлементных кортежей, в котором
    # первый элемент кортежа - название конвейера с
    # преобразованиями для определённого типа признаков
    transformers = [('num', num_pipe, num_columns),
                ('cat', cat_pipe, cat_columns)]

    # передаем список трансформеров в  Columnransformer
    transformer = ColumnTransformer(transformers=transformers)

    # задаем итоговый конвейрер
    pipe = Pipeline([('transform', transformer), 
                     ('regressor', RandomForestRegressor())])
    return pipe


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--num_columns', dest='num_columns', required=True)
    args_parser.add_argument('--cat_columns', dest='cat_columns', required=True)
    args = args_parser.parse_args()
    num_columns=args.num_columns
    cat_columns=args.cat_columns
    create_pipeline_structure(num_columns = num_columns, cat_columns = cat_columns)