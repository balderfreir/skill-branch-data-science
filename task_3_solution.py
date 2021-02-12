import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from copy import deepcopy
# from tqdm import tqdm

from sklearn.datasets import make_regression
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split


def split_data_into_two_samples(dataframe):  # 1
    x_train, x_test = train_test_split(dataframe, test_size=0.3,
                                       random_state=42)
    # df_size = round(len(dataframe))

    # x = dataframe.head(int(df_size*0.7))
    # y = dataframe.tail(df_size - len(x))

    return x_train, x_test


def prepare_data(dataframe):  # 2
    df = dataframe.select_dtypes(exclude='object')
    price_doc = df['price_doc']
    df = df.drop(['price_doc'], axis='columns')
    df = df.drop(['id'], axis='columns')
    df = df.dropna()
    df = df.dropna(axis='columns', inplace=True)

    # columns_list = df.columns
    # for el in columns_list:
    #     if df[el].dtypes == 'object':
    #         df = df.drop([el], axis='columns')
    #
    # price_doc = df['price_doc']
    # df = df.drop(['price_doc'], axis='columns')
    #
    # print(df.dtypes)
    return price_doc, df


def scale_data(dataframe):  # 3
    pass


def prepare_data_for_model(dataframe):  # 4
    pass


def fit_first_linear_model(dataframe):  # 5, 6
    pass


def evaluate_model(dataframe):  # 7
    pass


def calculate_model_weights(dataframe):  # 8
    pass


# df = pd.read_csv('sberbank_housing_market.csv', sep=',')
# print(split_data_into_two_samples(df))
# print(prepare_data(df))

# print(df['id'].dtypes)
