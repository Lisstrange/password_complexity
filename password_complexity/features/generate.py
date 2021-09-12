import pandas as pd
from nltk.corpus import words


def generate_features(features_df: pd.DataFrame) -> pd.DataFrame:
    """Genrate new features

    Args:
        features_df (pd.DataFrame): Original features
    
    Returns:
        pd.DataFrame: Original and generated features.
    """
    
    ### Fill Nan passwords #####
    features_df['Password'] = features_df['Password'].fillna('No_set_password')
    ############################

    features_df['password_length'] = features_df['Password'].str.len()
    features_df['unique_chars_count'] = features_df['Password'].apply(lambda x: len(set(str(x))))
    features_df['unique_chars_prop'] = features_df.eval('unique_chars_count / password_length')
    features_df['is_alnum'] = features_df['Password'].str.isalnum().astype('int')
    features_df['is_alpha'] = features_df['Password'].str.isalpha().astype('int')
    features_df['is_lower'] = features_df['Password'].str.islower().astype('int')
    features_df['is_upper'] = features_df['Password'].str.isupper().astype('int')
    features_df['is_numeric'] = features_df['Password'].str.isnumeric().astype('int')
    features_df['letters_count'] = features_df['Password'].apply(lambda x: sum([i.isalpha() for i in x]))
    features_df['letters_prob'] = features_df['letters_count']/features_df['password_length']
    features_df['difits_count'] = features_df['Password'].apply(lambda x: sum([i.isdigit() for i in x]))
    features_df['digits_prob'] = features_df['difits_count']/features_df['password_length']
    features_df['is_lower_and_upper'] = features_df['is_lower']+features_df['is_upper']
    features_df['palindrom'] = features_df['Password'] == features_df['Password'].str[::-1]
    # features_df['word']=features_df['Password'].str.lower().apply(lambda x: x in words.words()) ## uncommit it if your notebook is powerfull
    
    features_df = features_df.drop('Password', axis=1)
    return features_df