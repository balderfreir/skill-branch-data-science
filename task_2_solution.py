import pandas as pd
import numpy as np


def calculate_data_shape(dt):
    return print(dt.shape)


def take_columns(dt):
    return print(dt.columns)


def calculate_target_ratio(dataframe, target_name):
    mean = round(dataframe[target_name].mean(),2)
    return print(mean)


def calculate_data_dtypes(df):
    return print(df.dtypes)


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


# df = pd.read_csv('sberbank_housing_market.csv', sep=',')
# calculate_data_shape(df)
# take_columns(df)
# calculate_target_ratio(df,'price_doc')
# calculate_data_dtypes(df)