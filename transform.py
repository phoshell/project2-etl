# Transform DataFrame into tables

# TABLE 1 - Museums by NAME

def transform_museums_by_name(us_museums_df):
# Create a filtered dataframe from specific columns
    name_col = ["MID", "COMMONNAME", "LEGALNAME"]
    museums_by_name = us_museums_df[name_col].copy()

# Rename the column headers
    museums_by_name = museums_by_name.rename(columns = {"MID": "id",
                                                          "COMMONNAME": "common_name",
                                                          "LEGALNAME": "legal_name"})

# Clean the data by dropping duplicates and setting the index
    museums_by_name.drop_duplicates("id", inplace = True)
    museums_by_name.set_index("id", inplace = True)

    #museums_by_name.head()
    return museums_by_name

# TABLE 2 - Museums by ADDRESS 
def transform_museums_by_address(us_museums_df):

# Create a filtered dataframe from specific columns
    name_col = ["MID", "ADSTREET", "ADCITY", "ADSTATE", "ADZIP5", "LONGITUDE", "LATITUDE"]
    museums_by_address = us_museums_df[name_col].copy()

# Rename the column headers
    museums_by_address = museums_by_address.rename(columns = {"MID": "id",
                                                    "ADSTREET": "street_address",
                                                    "ADCITY": "city",
                                                    "ADSTATE": "state",
                                                    "ADZIP5": "zip_code",
                                                    "LONGITUDE": "longitude",
                                                    "LATITUDE": "latitude"
                                                   })
# Clean the data by dropping duplicates and setting the index
    museums_by_address.drop_duplicates("id", inplace = True)
    museums_by_address.set_index("id", inplace = True)

    #museums_by_address.head(40)
    return museums_by_address


 # TABLE 3 - Museums by MUSEUM BY AAM 

def transform_museums_by_aam(us_museums_df):
# Create a filtered dataframe from specific columns
    name_col = ["MID", "AAMREG"]
    museums_by_region = us_museums_df[name_col].copy()

# Rename the column headers
    museums_by_region = museums_by_region.rename(columns = {"MID": "id",
                                                    "AAMREG": "reg_number"})

# Clean the data by dropping duplicates and setting the index
    museums_by_region.drop_duplicates("id", inplace = True)
    museums_by_region.set_index("id", inplace = True)

    #museums_by_region.head()
    return museums_by_region


