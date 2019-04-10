# Import dependencies
import pandas as pd
from sqlalchemy import create_engine
import pymysql

import pandas as pd
from sqlalchemy import create_engine
import pymysql


# Create database connection
def loads():

    connection_string = "root:root@127.0.0.1:3306/us_museums_db"
    engine = create_engine(f'mysql+pymysql://{connection_string}')

    # Confirm tables
    engine.table_names()

    # Load DataFrames into database
    museums_by_address.to_sql(name = 'address', con = engine, if_exists = 'append', index = True) 

if __name__ == '__main__':
   loads()