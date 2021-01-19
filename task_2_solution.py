import pandas as pd
import numpy as np


def calculate_data_shape(dataframe):
    dt = dataframe
    return print(dt.shape)


def take_columns(dataframe):
    dt = dataframe
    return print(dt.columns)


def calculate_target_ratio():
    pass


def calculate_data_dtypes():
    pass


def calculate_cheap_apartment():
    pass


def calculate_squad_in_cheap_apartment():
    pass


def calculate_mean_price_in_new_housing():
    pass


def calculate_mean_squared_by_num_rooms():
    pass


def calculate_squared_stats_by_material():
    pass


def calculate_crosstab():
    pass


df = pd.read_csv('sberbank_housing_market.csv', sep=',')
calculate_data_shape(df)
take_columns(df)
