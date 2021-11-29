import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")


def prep_telco(df):
    '''
    This function will clean the data prior to splitting.
    '''

    # Drop redundant and unhelpful columns.
    df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id'], inplace=True)

    # Drop customers with no tenure or total charges
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']

    # Convert datatype
    df['total_charges'] = df.total_charges.astype(float)

    # encode binary categorical variables into numeric values
    df['gender_encoded'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})

    # Drop the original object columns these values were encoded from
    df.drop(columns=['gender', 'partner', 'dependents', 'phone_service', 'paperless_billing', 'churn'], inplace=True)

    # Encode object columns with more than two choices
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                                'online_security', \
                                'online_backup', \
                                'device_protection', \
                                'tech_support', \
                                'streaming_tv', \
                                'streaming_movies', \
                                'contract_type', \
                                'internet_service_type', \
                                'payment_type']], dummy_na=False, \
                                drop_first=True)
    dummy_df

    # Combine newly encoded
    df = pd.concat([df, dummy_df], axis=1)
    df.head()

    # Drop the original object columns these values were encoded from

    df.drop(columns=['multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 'internet_service_type', 'payment_type'], inplace=True)

    # Drop the redundant newly encoded columns
    df.drop(columns=['multiple_lines_No phone service', 'online_security_No internet service', 'online_backup_No internet service', 'device_protection_No internet service', 'tech_support_No internet service', 'streaming_tv_No internet service', 'streaming_movies_No internet service'], inplace=True)
    
    return df

def split_telco(df):
    train_validate, telco_test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn_encoded)

    telco_train, telco_validate = train_test_split(train_validate, test_size=.3, 
                                    random_state=123, 
                                    stratify=train_validate.churn_encoded)

    return telco_train, telco_validate, telco_test