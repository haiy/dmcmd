'''
load all kinds of data to numpy array 
'''

import pandas as pd
import pickle


class LoadDataException(Exception):
    pass


class InputType():
    def __init__(self):
        self.HDFS = 'hdfs'
        self.CSV = 'csv'
        self.URL = 'url'
        self.HIVE_TABLE = 'hive_table'


input_type = InputType()


def load_hdfs_data(data_path):
    pass


def load_hive_table(table_name):
    pass


def load_csv_data(file_name):
    df = pd.read_csv(file_name, header=0)
    return df


def load_url_data(url_path):
    pass


load_func_dict = {input_type.CSV: load_csv_data, input_type.HDFS: load_hdfs_data}


def load_data(table_name, src_type):
    if src_type not in load_func_dict:
        raise LoadDataException("Wrong src type!")
    return load_func_dict[src_type](table_name)


def save_csv_data(path, data):
    data.to_csv(path)


def get_cols_np(pd_df, cols):
    cols2 = cols
    return cols2


def save_model(model_path, input_model):
    pickle.dump(input_model, open(model_path, 'wb'))