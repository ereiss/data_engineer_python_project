# ETL Project: Cleaning and Loading Netflix Titles Dataset

## Overview

This project performs Extract, Transform, and Load (ETL) operations on the Netflix Titles dataset. The dataset, sourced from Kaggle, contains information about various movies and TV shows available on Netflix.

The ETL process involves:

1. **Extract**: Reading the data from the provided `netflix_titles.csv` file.
2. **Transform**: Performing comprehensive data cleaning and preparation.
3. **Load**: Writing the cleaned data into a relational database using SQLAlchemy.

## Data Source

- **Dataset**: `netflix_titles.csv`
- **Source**: [Netflix Movies and TV Shows](https://www.kaggle.com/shivamb/netflix-shows)

## Tools and Libraries Used

- Python
- Pandas
- SQLAlchemy
- Google colab notebook (for initial data exploration and testing)

## Instructions

To run the ETL process:

1. Clone this repository to your local machine.
2. Ensure you have Python and the required libraries installed (Pandas, SQLAlchemy):
   - pip install pandas
   - pip install sqlalchemy
3. `netflix_titles.csv` dataset is dowloaded from google drive to project workspace - do nothing
4. run: python main.py

## Dependencies

1. Project's files tree:

![image](https://github.com/ereiss/data_engineer_python_project/blob/main/artifacts/project_file_tree.png)

2. Files description:

Provides flexibility to override default configurations and customize settings based on specific project requirements or deployment environments. This can be achieved through conditional logic or by importing environment-specific configuration files.


   | File name                   | Description                                                                    |
   |-----------------------------|--------------------------------------------------------------------------------|
   | /artifacts/\*.\*            | Non python files, mostly png files for README.md                               |
   | /data/netflix.db            | Database file to where tables are written as part of the Load of ETL process   |
   | /utils/config.py            | A file that contains project's default configurations and customize settings   |
   | /utils/data_extracting.py   | Methods required in order to connect to dataset and fetch it into dataframe    |
   | /utils/data_processing.py   | Methods containing all data cleaning "tools" for this project                  |
   | /utils/data_loading.py      | Methods for loading process data into database tables                          |
   | README.md                   | repository readme file                                                         |	
   | main.py                     | main run file                                                                  |


## Detailed Process

1. **Extract**:
   - The provided dataset, `netflix_titles.csv`, is read into a Pandas DataFrame. The following describes the dataset content: 

     | Column Name   | Description                                      |
     |---------------|--------------------------------------------------|
     | show_id       | Unique ID for every Movie / Tv Show              |
     | type          | Identifier - A Movie or TV Show                  |
     | title         | Title of the Movie / Tv Show                     |
     | director      | Director of the Movie                            |
     | cast          | Actors involved in the movie / show              |
     | country       | Country where the movie / show was produced      |
     | date_added    | Date it was added on Netflix                     |	
     | release_year  | Actual Release year of the move / show           |
     | rating        | TV Rating of the movie / show                    |
     | duration      | Total Duration - in minutes or number of seasons |
     | listed_in     | Genere                                           |
     | description   | The summary description                          |

2. **Transform**:
   - Data cleaning and preprocessing steps are performed, including handling missing values, standardizing data formats, and correcting inconsistencies.
   - Comprehensive cleaning operations are conducted to ensure data integrity and consistency.

3. **Load**:
   - A connection to the database is established using SQLAlchemy.
   - The cleaned DataFrame is written to the database as a new table.

## Cleaning the Netflix Titles dataset

It involves various steps to ensure data integrity and consistency. Before we dig in the actions that are going to take place lets have a short sample view on dataset:

![image](https://github.com/ereiss/data_engineer_python_project/blob/main/artifacts/head.png)

These are the steps that are going to be taken:

1. **Remove Columns With No Business Value**:
   - show_id and description can be removed since they are with no business value to us

2. **Handle Missing Values**:
   - Identify columns with missing values and decide how to handle them.
   - Options include removing rows with missing values or imputing them using appropriate methods.

3. **Standardize Data Formats**:
   - Convert all dates to a consistent format (e.g., YYYY-MM-DD).
   - Standardize durations to a consistent unit (e.g., minutes for movies, seasons for TV shows).

4. **Parse and Extract Information**:
   - Extract useful information from columns containing multiple pieces of data (e.g., cast, listed_in).
   - Split columns into multiple columns or use them to create new features (e.g., date_add splitted into year_added, month_added, day_added).

5. **Correct Inconsistencies**:
   - Standardize country names, genres.
   - Ensure consistent spelling and formatting for genres.
   - Handle inconsistencies names like remove leading/trailing spaces.

6. **Remove Duplicates**:
   - Check for and remove duplicate rows.
   - Be cautious when removing duplicates to avoid deleting legitimate data.

## Conclusion

This ETL project successfully cleans and loads the Netflix Titles dataset into a relational database, making it easier to query and analyze the data for further insights and applications.
