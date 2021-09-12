from optuna.integration import OptunaSearchCV
from optuna.distributions import *

params_distribution = {
        'transform__cat__imputer__strategy': CategoricalDistribution(['mean', 'median']),
        'linear__normalize': CategoricalDistribution([True, False]),
        'linear__positive': CategoricalDistribution([True])
    }
