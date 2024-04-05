import click
import pandas as pd
import copy
import os

# TODO - Trim level is indicative of the quality of the vehicle which 
# would be indicative of whether it is more/less likely it's a lemon.
# Too many Trims defined though so removing this column for now but may
# be better to abstract it into higher categories at a later time.
HIGH_CARDINALITY_COLUMNS = ['Model', 'Trim', 'SubModel', 'Color']
UNINFORMATIVE_COLUMNS = ['RefId', 'WheelType', 'PRIMEUNIT', 'AUCGUART']
STRING_COLUMNS = ['Nationality', 'TopThreeAmericanName']

@click.command()
@click.option("--data-file-path", default="kaggle_2024/data/raw/training.csv")
@click.option("--output-folder", default='kaggle_2024/data/processed/')
def preprocess_raw_data(data_file_path: str, output_folder: str):    
    df = pd.read_csv(data_file_path)
    # We know from inspecting WheelType that WheelTypeID 0 is equal to Null
    df['WheelTypeID'] = df['WheelTypeID'].fillna(0)
    df = _drop_columns(df)
    df = _delete_rows_with_blank_values(df)
    path = os.path.join(output_folder, 'preprocessed_data.csv')
    df.to_csv(path, index=False)
    print(f'Wrote preprocessed data file to {path}.')

def _drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    # Assuming the dataframe will be small for now and that deep copying is not an issue
    df_copy = copy.deepcopy(df)
    df_copy = df_copy.drop(columns=HIGH_CARDINALITY_COLUMNS)
    return df_copy.drop(columns=UNINFORMATIVE_COLUMNS)

def _delete_rows_with_blank_values(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = copy.deepcopy(df)
    blank_rows = df_copy[df_copy.isna().any(axis=1)]
    if len(blank_rows) >= 500:
        print(f'There are {len(blank_rows)} rows with blank values. Are you sure you want to delete these rows?')
        raise NotImplementedError
    print(f'Dropped {len(blank_rows)} rows.')
    return df_copy.dropna()



if __name__ == "__main__":
    preprocess_raw_data()