import pandas as pd
import numpy as np


def calculate_data_shape(dataframe):  # 1
    return dataframe.shape


def take_columns(dataframe):  # 2
    return dataframe.columns


def calculate_target_ratio(dataframe, target_name):  # 3
    return round(dataframe[target_name].mean(), 2)


def calculate_data_dtypes(dataframe):  # 4
    cat_pri = 0
    num_pri = 0
    list_columns = dataframe.columns
    for column in list_columns:
        if dataframe[column].dtype == 'object':
            cat_pri += 1
        else:
            num_pri += 1

    return num_pri, cat_pri


def calculate_cheap_apartment(dataframe):  # 5
    df = dataframe.loc[dataframe.loc[:, 'price_doc'] <= 1000000]
    return len(df.index)


def calculate_squad_in_cheap_apartment(dataframe):  # 6
    # df = dataframe.loc[dataframe.loc[:, 'full_sq'] != 0.0]
    # df = dataframe.loc[dataframe.loc[:, 'price_doc'] != 0.0]
    # df = dataframe.loc[dataframe.loc[:, 'price_doc'] <= 1000000]
    df = dataframe[dataframe['price_doc'] <= 1000000]

    return round(df['full_sq'].mean())


def calculate_mean_price_in_new_housing(dataframe):  # 7

    df = dataframe[(dataframe['num_room'] == 3.0) & (dataframe['build_year'] >= 2010.0)]

    return round(df['price_doc'].mean())


def calculate_mean_squared_by_num_rooms(dataframe):  # 8
    df = round(dataframe.groupby('num_room')['full_sq'].mean(), 2)
    return df


def calculate_squared_stats_by_material(dataframe): # Задание 9.
    # df = dataframe
    # df['min'] = dataframe.groupby('material')['full_sq'].min()
    # df['max'] = dataframe.groupby('material')['full_sq'].max()


    return pd.pivot_table(dataframe,index='material',values='full_sq',aggfunc={'full_sq': [np.max, np.min]})

def calculate_crosstab(x): # Задание 10.
    pass


# df = pd.read_csv('sberbank_housing_market.csv', sep=',')
# print(calculate_squad_in_cheap_apartment(df))  # 6
# print(calculate_mean_price_in_new_housing(df))  # 7
# print(calculate_squared_stats_by_material(df))  # 9
# print(calculate_crosstab(df))  # 10

