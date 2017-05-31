from sklearn import preprocessing
from sklearn import linear_model
import copy

# http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
def exec_min_max(para_dict, input_x, input_y):
    new_x = copy.deepcopy(input_x)
    min_max = preprocessing.MinMaxScaler(feature_range=(0, 1))
    min_max.fit(new_x)
    min_max.fit_transform(new_x)
    return new_x, min_max


# http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler
def exec_standardization(para_dict, input_x, input_y):
    new_x = copy.deepcopy(input_x)
    s = preprocessing.StandardScaler().fit(new_x)
    s.fit_transform(new_x)
    return new_x, s


def set_paras(raw_paras, input_paras):
    for input_p_name, input_p_val in input_paras.items():
        if input_p_name in raw_paras:
            raw_paras[input_p_name] = raw_paras[input_p_name]


# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
# train method
def exec_lr(para_dict, input_x, input_y):
    raw_para_dict = {
        "penalty": 'l2',
        "dual": False,
        "tol": 1e-4,
        "C": 1.0,
        "fit_intercept": True,
        "intercept_scaling": 1,
        "class_weight": None,
        "random_state": None,
        "solver": 'liblinear',
        "max_iter": 100,
        "multi_class": 'ovr',
        "verbose": 0,
        "warm_start": False,
        "n_jobs": 1,
    }
    set_paras(raw_para_dict, para_dict)
    lr = linear_model.LogisticRegression(**raw_para_dict)
    lr.fit(input_x, input_y)
    return lr


FUNC_DICT = {'min_max': exec_min_max, 'standardization': exec_standardization, 'lr': exec_lr}
MODLES = ['lr']