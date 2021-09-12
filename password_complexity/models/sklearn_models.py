from sklearn import ensemble, linear_model, svm, neighbors
import numpy as np

from warnings import simplefilter, filterwarnings
from sklearn.exceptions import ConvergenceWarning, DataConversionWarning

simplefilter("ignore", category=ConvergenceWarning)
filterwarnings(
    "ignore",
    category=ConvergenceWarning,
    message="^Maximum number of iteration reached",
)
filterwarnings(
    "ignore", category=ConvergenceWarning, message="^Liblinear failed to converge"
)
simplefilter("ignore", category=DataConversionWarning)


################################## LinearModel ##########################################################

