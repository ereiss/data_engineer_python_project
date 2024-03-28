import utils.config as config
import utils.data_extracting as extract
import utils.data_processing as transform
import utils.data_loading as load
from sqlalchemy import create_engine, text
import pandas as pd

#############################################
# 1. Data extracting from google drive
#############################################
csv_reader = extract.google_drive_csv_reader(config.GOOGLE_DRIVE_DATA_URL, config.DATASET_NAME)
df_original = csv_reader.read_csv_to_dataframe()

#############################################
# 2. Data transformation
#############################################
df_sandbox = df_original.copy()

# Change columns name
change_column_names_handler = transform.change_columns_names(dataframe = df_sandbox)
df_sandbox = change_column_names_handler.change_column_names(config.CHANGE_COLUMN_NAMES_MAPPING)

# Drop columns with no business value
drop_columns_handler = transform.drop_columns(dataframe = df_sandbox)
df_sandbox = drop_columns_handler.drop_columns(config.COLUMNS_TO_DROP)

# Replace missing values based
null_handler = transform.handle_null_values(dataframe=df_sandbox)
df_sandbox = null_handler.replace_nulls(config.REPLACE_NULL_MAPPING)

# Remove rows with missing values
df_sandbox = null_handler.delete_nulls(config.COLUMNS_TO_DELETE_NULL)

# Column to split and explode
splitter_handler = transform.handle_splitting_columns(dataframe = df_sandbox)
df_sandbox = splitter_handler.split_columns(config.COLUMNS_TO_SPLIT)

# Remove leading/trailing spaces
trim_handler = transform.handle_trim_whitespace(dataframe = df_sandbox)
df_sandbox = trim_handler.trim_columns(config.COLUMNS_TO_TRIM)

# Changing columns values: replace + removing certain values
column_changer_handler = transform.handle_change_columns_values(dataframe = df_sandbox)
df_sandbox = column_changer_handler.change_column_values(config.CHANGE_VALUES_MAPPING)
df_sandbox = column_changer_handler.delete_column_values(config.DELETE_VALUES_MAPPING)

# Remove duplicates
duplicates_handler = transform.handle_duplicate_rows(dataframe = df_sandbox)
df_sandbox = duplicates_handler.remove_duplicates()

pd.options.mode.copy_on_write = True
df_sandbox[['duration_digits', 'duration_unit']] = df_sandbox['duration'].str.split(r'(\d+)', expand=True).iloc[:, 1:]
df_sandbox['duration_digits'] = df_sandbox['duration_digits'].astype(int)

df_sandbox['date_added'] = pd.to_datetime(df_sandbox['date_added'])
df_sandbox['year_added'] = df_sandbox['date_added'].dt.year
df_sandbox['month_added'] = df_sandbox['date_added'].dt.month
df_sandbox['day_added'] = df_sandbox['date_added'].dt.day

###################################################
# 3. Data load
###################################################

# Create an SQLAlchemy engine

dbname = config.DATABASE_NAME
db_path = f'sqlite:///{dbname}'
engine = create_engine(db_path)

loader_to_database = load.dataframe_to_tables(dataframe = df_sandbox)
loader_to_database.create_tables(engine = engine, dbname = dbname, tables_to_create=config.DB_TABLES)

engine.dispose()

##########################################
### 4. Querying from database
##########################################

# Open connection to database
engine = create_engine('sqlite:///data/netflix.db')
connection = engine.connect()

print("Querying tables from database:")
print("======================================================")

print("\n>>> Top 5 most successfull directors:")
print("***************************************************\n")
query = f'''SELECT director, count(*) as NumTitles 
        FROM netflix_directors
        WHERE director <> 'No Director'
        GROUP BY director
        ORDER BY 2 DESC
        LIMIT 5'''

# Execute the query and fetch the results into a DataFrame
result = connection.execute(text(query))
rows = result.fetchall()

df = pd.DataFrame(rows, columns=result.keys())
print(df.head(5))

'''
df_from_sql_directors = pd.read_sql_query(query, connection)
print(df_from_sql_directors.head(5))
'''

print("\n>>> Who is the most productive Movie actor:")
print("***************************************************\n")

query = f'''SELECT actor, count(*) as NumTitles
            FROM netflix_actors
            WHERE 1=1 
                AND actor <> 'No Actor'
                AND type = 'Movie'
            GROUP BY actor
            ORDER BY 2 DESC
            LIMIT 1'''

# Execute the query and fetch the results into a DataFrame

result = connection.execute(text(query))
rows = result.fetchall()

df = pd.DataFrame(rows, columns=result.keys())
print(df.head(5))

print("\n>>> Who is the most productive TV Show actor:")
print("***************************************************\n")

query = f'''SELECT actor, count(*) as NumTitles
            FROM netflix_actors
            WHERE 1=1 
                AND actor <> 'No Actor'
                AND type = 'TV Show'
            GROUP BY actor
            ORDER BY 2 DESC
            LIMIT 1'''

# Execute the query and fetch the results into a DataFrame

result = connection.execute(text(query))
rows = result.fetchall()

df = pd.DataFrame(rows, columns=result.keys())
print(df.head())


print("\n>>> Most frequent countries:")
print("***************************************************\n")

query = f'''SELECT country, count(*) as NumTitiles
            FROM netflix_countries
            WHERE 1=1
                AND country <> 'No Country'
            GROUP BY country
            ORDER BY 2 DESC
            LIMIT 10'''

# Execute the query and fetch the results into a DataFrame

result = connection.execute(text(query))
rows = result.fetchall()

df = pd.DataFrame(rows, columns=result.keys())
print(df.head(10))

print("\n>>> Most frequent genres:")
print("***************************************************\n")
query = f'''SELECT genres, count(*) as NumTitles 
            FROM netflix_genres
            GROUP BY genres
            ORDER BY 2 DESC
            LIMIT 5'''

# Execute the query and fetch the results into a DataFrame

result = connection.execute(text(query))
rows = result.fetchall()

df = pd.DataFrame(rows, columns=result.keys())
print(df.head(10))

