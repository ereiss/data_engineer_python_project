# data_loading.py

import pandas as pd

class dataframe_to_tables:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def create_tables(self, engine, dbname, tables_to_create):
        # Select subset of columns
        print(f">>> Load dataframe to '{dbname}' database")
        print("*******************************************************")
        for table_name, subset_columns in tables_to_create.items():
            subset_df = self.dataframe[subset_columns]

            # Remove duplicates
            processed_df = subset_df.drop_duplicates()

            # Load table to database
            processed_df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Table '{table_name}' has been created successfully")
        print("*******************************************************\n")