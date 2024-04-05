import click
import pandas as pd
import copy
from kaggle_2024.src.assumptions.kicked_cars_assumptions import STATES_LEMON_GRADES, SIZE_TO_GENDER_PROPORTION, MAKE_TO_DEPENDABILITY, SIZE_TO_FT_PERCENT, SIZE_TO_PT_PERCENT, SIZE_TO_UNEMPLOYED_PERCENT, SIZE_TO_RETIRED_PERCENT
import os


AUCTION_MAP = {'ADESA': 0, 'MANHEIM': 1, 'OTHER': 2}
TRANSMISSION_MAP = {'AUTO': 0, 'MANUAL': 1, 'Manual': 1}
UNUSED_COLUMNS = ['MMRAcquisitionAuctionAveragePrice',
                    'MMRAcquisitionAuctionCleanPrice',
                    'MMRAcquisitionRetailAveragePrice',
                    'MMRAcquisitonRetailCleanPrice',
                    'MMRCurrentAuctionAveragePrice',
                    'MMRCurrentAuctionCleanPrice',
                    'MMRCurrentRetailAveragePrice',
                    'MMRCurrentRetailCleanPrice',
                    'VNST',
                    'Size',
                    'VNZIP1',
                    'Make',
                    'Nationality',
                    'PurchDate']
TOP_THREE_MAP = {'OTHER': 0, 'CHRYSLER': 1, 'FORD': 2, 'GM': 3}


@click.command()
@click.option("--data-file-path", default="kaggle_2024/data/processed/preprocessed_data.csv")
@click.option("--output-folder", default="kaggle_2024/data/final/")
def engineer_features(data_file_path: str, output_folder: str):    
    df = pd.read_csv(data_file_path)
    _check_all_values_are_mappable(df)
    df = _map_categorical_variables_to_defined_dicts(df)
    df = _engineer_new_pricing_columns(df)
    _check_occupation_columns_sum_to_one(df)
    df = _deconstruct_dates(df)
    df = df.drop(columns=UNUSED_COLUMNS)
    path = os.path.join(output_folder, 'engineered_features.csv')
    df.to_csv(path, index=False)
    print(f'Wrote engineered features to {path}.')


def _deconstruct_dates(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = copy.deepcopy(df)
    df_copy['PurchDate'] = pd.to_datetime(df_copy['PurchDate'])
    df_copy['month'] = df_copy['PurchDate'].dt.month
    df_copy['day_of_week'] = df_copy['PurchDate'].dt.dayofweek  # Monday=0, Sunday=6
    # One-hot encode 'day_of_week'
    return pd.get_dummies(df_copy, columns=['day_of_week'], prefix='day_of_week', dtype=int)    

def _check_occupation_columns_sum_to_one(df: pd.DataFrame) -> pd.DataFrame:
    sum = df[['FT_Prob', 'PT_Prob', 'Unemployed_Prob', 'Retired_Prob']].sum().sum()
    length = len(df)
    if sum/length != 100:
        print('The occupation columns do not sum to 100.')
        raise NotImplementedError

def _map_categorical_variables_to_defined_dicts(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = copy.deepcopy(df)
    df_copy['Auction'] = df_copy['Auction'].map(AUCTION_MAP)
    df_copy['Transmission'] = df_copy['Transmission'].map(TRANSMISSION_MAP)
    df_copy['TopThreeAmericanName'] = df_copy['TopThreeAmericanName'].map(TOP_THREE_MAP)
    df_copy['State_Lemon_Grades'] = df_copy['VNST'].map(STATES_LEMON_GRADES)
    df_copy['Gender_Proportion'] = df_copy['Size'].map(SIZE_TO_GENDER_PROPORTION)
    df_copy['FT_Prob'] = df_copy['Size'].map(SIZE_TO_FT_PERCENT)
    df_copy['PT_Prob'] = df_copy['Size'].map(SIZE_TO_PT_PERCENT)
    df_copy['Unemployed_Prob'] = df_copy['Size'].map(SIZE_TO_UNEMPLOYED_PERCENT)
    df_copy['Retired_Prob'] = df_copy['Size'].map(SIZE_TO_RETIRED_PERCENT)
    return df_copy


def _engineer_new_pricing_columns(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = copy.deepcopy(df)
    df_copy['Cost_Buffer'] = df_copy['MMRAcquisitionAuctionAveragePrice'] - df_copy['VehBCost']
    df_copy['Expected_Profit'] = df_copy['MMRAcquisitionRetailAveragePrice'] - df_copy['MMRAcquisitionAuctionAveragePrice']
    return df_copy

def _check_all_values_are_mappable(df: pd.DataFrame):
    '''
    See if there are any values that are not recognized in any keys of the dictionaries.
    If yes, flag it before conducting the mapping. 
    '''
    if len(df.loc[~df['Auction'].isin(AUCTION_MAP.keys()), 'Auction'].unique()) > 0:
        print(f"The following Auctions are not recognized {df.loc[~df['Auction'].isin(AUCTION_MAP.keys()), 'Auction'].unique()}")
        raise NotImplementedError
    if len(df.loc[~df['Transmission'].isin(TRANSMISSION_MAP.keys()), 'Transmission'].unique()) > 0:
        print(f"The following Transmissions are not recognized {df.loc[~df['Transmission'].isin(TRANSMISSION_MAP.keys()), 'Transmission'].unique()}")
        raise NotImplementedError    
    if len(df.loc[~df['VNST'].isin(STATES_LEMON_GRADES.keys()), 'VNST'].unique()) > 0:
        print(f"The following States are not recognized {df.loc[~df['VNST'].isin(STATES_LEMON_GRADES.keys()), 'VNST'].unique()}")
        raise NotImplementedError
    # TODO: Should run a check to make sure that all the 'Size' dictionaries should have the same keys
    # Otherwise could have a situation for example where SIZE_TO_GENDER_PROPORTION have one set of keys
    # SIZE_TO_FT_PERCENT have a different set of keys
    if len(df.loc[~df['Size'].isin(SIZE_TO_GENDER_PROPORTION.keys()), 'Size'].unique()) > 0:
        print(f"The following Sizes are not recognized {df.loc[~df['Size'].isin(SIZE_TO_GENDER_PROPORTION.keys()), 'Size'].unique()}")
        raise NotImplementedError


if __name__ == "__main__":
    engineer_features()