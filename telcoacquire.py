import pandas as pd
import numpy as np
import os
from env import host, user, password

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

###################### Acquire Telco Data ######################


def new_telco_data():
    '''
    This function reads the telco data from the Codeup database into a dataframe.
    '''
    sql_query = '''
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                '''
    
    # Read in DataFrame from Codeup db.
    telco_df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return telco_df

def get_telco_data():
    '''
    This function reads in telco data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a dataframe.
    '''
    if os.path.isfile('telco.csv'):
        
        # If csv file exists read in data from csv file.
        telco_df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        telco_df = new_telco_data()
        
        # Cache data
        telco_df.to_csv('telco.csv')
        
    return telco_df

#################### Make Telco Endineered Features ##########################
# Will complete models with fields in the database first, then try with these additional Features to see if any improvements result

def telco_eng(df):
    # Create engineered features
    # encode number_relationships by utilizing information from dependents_encoded and partner_encoded
    df['number_relationships'] = df['dependents_encoded'] + df['partner_encoded']

    # convert streaming_tv into numeric data
    df['streaming_tv_bool'] = df.streaming_tv.map({'Yes': 1, 'No': 0, 'No internet service': 0})

    # convert streaming_movies into numeric data
    df['streaming_movies_bool'] = df.streaming_movies.map({'Yes': 1, 'No': 0, 'No internet service': 0}) 

    # encode number_streaming_services by utilizing information from streaming_tv_encoded and streaming_movies_encoded
    df['number_streaming_services'] = df['streaming_tv_bool'] + df['streaming_movies_bool']

    # convert online_security into numeric data
    df['online_security_bool'] = df.online_security.map({'Yes': 1, 'No': 0, 'No internet service': 0})

    # convert online_backup into numeric data
    df['online_backup_bool'] = df.online_backup.map({'Yes': 1, 'No': 0, 'No internet service': 0}) 

    # encode number_online_services by utilizing information from online_security_encoded and online_backup_encoded
    df['number_online_services'] = df['online_security_bool'] + df['online_backup_bool']

    # encode tenure in years (rounded down) by utilizing information from tenure (currently stored in months)
    df['yearly_tenure'] = df.tenure.apply(lambda x: math.floor(x/12))

    # encode has_internet
    df['has_internet'] = df.internet_service_type.apply(lambda x: 0 if x == 'None' else 1)

    return df

#################### Summarize Telco Data ##########################

def object_vals(df):
    '''
    This is a helper function for viewing the value_counts for object cols.
    '''
    for col in df.columns:
        if df[col].dtype == 'object':
            print(df[col].value_counts(dropna=False))

def col_range(df):
    stats_df = df.describe().T
    stats_df['range'] = stats_df['max'] - stats_df['min']
    return stats_df

    
def summarize_df(df):
    '''
    This function returns the shape, info, a preview, the value_counts of object columns
    and the summary stats for numeric columns.
    '''
    print(f'This dataframe has {df.shape[0]} rows and {df.shape[1]} columns.')
    print('------------------------')
    print('')
    print(df.info())
    print('------------------------')
    print('')
    print(df.head())
    print('------------------------')
    print('')
    object_vals(df)
    print('------------------------')
    print('')
    print(col_range(df))

    