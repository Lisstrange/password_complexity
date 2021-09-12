import numpy as np
from sklearn.metrics import make_scorer, mean_squared_log_error, mean_squared_error


def rmsle(real, predicted):
    sum=0.0
    n=len(predicted)
    for x in range(n):
        if predicted[x]<0 or real[x]<0: #check for negative values
            # continue
            p = np.log(predicted[x]+1)
            r = np.log(real[x]+1)
            sum = sum + (p - r)**2
        if predicted==0:
            sum=sum+100000
    return (sum/n)**0.5

def RMSLE(y_true:np.ndarray, y_pred:np.ndarray) -> np.float64:
    """
        The Root Mean Squared Log Error (RMSLE) metric 
        
        :param y_true: The ground truth labels given in the dataset
        :param y_pred: Our predictions
        :return: The RMSLE score
    """
    return np.sqrt(mean_squared_log_error(y_true, y_pred))


# def RMSLE(y_true:np.ndarray, y_pred:np.ndarray) -> np.float64:
#     """
#         The Root Mean Squared Log Error (RMSLE) metric 
        
#         :param y_true: The ground truth labels given in the dataset
#         :param y_pred: Our predictions
#         :return: The RMSLE score
#     """
#     return mean_squared_error(y_true, y_pred)

RMSLE_score = make_scorer(RMSLE, greater_is_better=False)

rmsle_score = make_scorer(rmsle, greater_is_better=False)
