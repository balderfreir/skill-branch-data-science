import pandas as pd
import numpy as np


def calculate_data_shape(dataframe):
    return dataframe.shape


def take_columns(dataframe):
    return dataframe.columns


def calculate_target_ratio(dataframe, target_name):
    return round(dataframe[target_name].mean(), 2)


def calculate_data_dtypes(dataframe):
    return dataframe.dtypes


def calculate_cheap_apartment(dataframe):
    df = dataframe.loc[dataframe.loc[:,'price_doc'] <= 1000000 ]
    return len(df.index)


def calculate_squad_in_cheap_apartment(dataframe):
    df = dataframe.loc[dataframe.loc[:, 'price_doc'] <= 1000000]
    return int(df['full_sq'].mean())


def calculate_mean_price_in_new_housing(dataframe):
    df = dataframe.loc[dataframe.loc[:, 'num_room'] == 3.0]
    df = dataframe.loc[dataframe.loc[:, 'build_year'] >= 2010.0]
    return int(df['price_doc'].mean())


def calculate_mean_squared_by_num_rooms(dataframe):
    dataframe['price_mean'] = round(dataframe['full_sq']/dataframe['num_room'],2)
    return dataframe['price_mean']


def calculate_squared_stats_by_material():
    pass


def calculate_crosstab():
    pass

# df = pd.read_csv('sberbank_housing_market.csv', sep=',')

# print(df.shape)
# print(calculate_cheap_apartment(df))
# print(calculate_squad_in_cheap_apartment(df))
# print(calculate_mean_price_in_new_housing(df))
# print(calculate_mean_squared_by_num_rooms(df))
# print(take_columns(df))
# # calculate_data_dtypes(df)
# print(df['num_room'])
# print(df['build_year'])
# print(df['material'])