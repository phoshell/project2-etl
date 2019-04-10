import pandas as pd


def extract_museums():
    museums_csv = "Resources/us_museums_final.csv"
    us_museums_df = pd.read_csv(museums_csv, low_memory = False)
    # us_museums_df.head()
    
    return us_museums_df
