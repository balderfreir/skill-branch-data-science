import pandas as pd
import numpy as np


def calculate_data_shape(dataframe):
    return dataframe.shape


def take_columns(dataframe):
    return dataframe.columns


def calculate_target_ratio(dataframe, target_name):
    return round(dataframe[target_name].mean(), 2)


def calculate_data_dtypes(dataframe):
    cat_pri = 0
    num_pri = 0
    list_columns = dataframe.columns
    for column in list_columns:
        if dataframe[column].dtype == 'object':
            cat_pri += 1
        else:
            num_pri += 1

    return num_pri, cat_pri


def calculate_cheap_apartment(dataframe):
    df = dataframe.loc[dataframe.loc[:, 'price_doc'] <= 1000000]
    return len(df.index)


def calculate_squad_in_cheap_apartment(dataframe):
    # df = dataframe.loc[dataframe.loc[:, 'full_sq'] != 0.0]
    # df = dataframe.loc[dataframe.loc[:, 'price_doc'] != 0.0]
    df = dataframe.loc[dataframe.loc[:, 'price_doc'] <= 1000000]

    return int(df['full_sq'].mean())


def calculate_mean_price_in_new_housing(dataframe):

    df = dataframe.loc[dataframe.loc[:, 'build_year'] >= 2010.0]
    df = dataframe.loc[dataframe.loc[:, 'num_room'] == 3.0]
    return int(df['price_doc'].mean())


def calculate_mean_squared_by_num_rooms(dataframe):
    df = round(dataframe.groupby('num_room')['full_sq'].mean(), 2)
    return df


def calculate_squared_stats_by_material():
    pass


def calculate_crosstab():
    pass


# df = pd.read_csv('sberbank_housing_market.csv', sep=',')
# df = df.loc[df.loc[:, 'price_doc'] <= 1000000]
# print(calculate_data_dtypes(df))
# print(len(df.columns))
# print(calculate_cheap_apartment(df))
# print(calculate_squad_in_cheap_apartment(df))
# print(calculate_mean_price_in_new_housing(df))
#print(calculate_mean_squared_by_num_rooms(df))
# print(take_columns(df))
# print(df['num_room'])
# print(df['build_year'])
# print(df['material'])
