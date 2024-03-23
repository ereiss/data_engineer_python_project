# Data Engineer Course - Python Project

## Project's requirements
> ## Goals
* Design and implement an ETL end-to-end
* Practice Python project development
* Practice Pandas capabilities
* Experiment with real-life data sets

## Introduction

> ### Netflix Movies and TV Shows
* Netflix is one of the most popular media and video streaming platforms. They have over 8000 movies or tv shows available on their platform, as of mid-2021, they have over 200M Subscribers globally.
* Referring to kaggle Netflix Movies and TV Shows dataset: **netflix_titles.csv**:
>> This tabular dataset consists of listings of all the movies and tv shows available on Netflix, along with details such as - cast, directors, ratings, release year, duration, etc.

> ### Dataset description

![image](https://github.com/ereiss/data_engineer_python_project/blob/main/artifacts/netflix_dataset_description.png)

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
- Jupyter Notebook (for initial data exploration and testing)

## Instructions

To run the ETL process:

1. Clone this repository to your local machine.
2. Ensure you have Python and the required libraries installed (Pandas, SQLAlchemy).
3. Download the `netflix_titles.csv` dataset from the provided source and place it in the project directory.
4. Open the Jupyter Notebook `ETL_Netflix.ipynb` and execute the cells sequentially.

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

## Database Schema

The schema for the database table where the cleaned data is loaded follows:

- Table Name: `netflix_titles`
  
  | Column Name   | Data Type | Description          |
  |---------------|-----------|----------------------|
  | show_id       | VARCHAR   | Unique identifier    |
  | type          | VARCHAR   | Type of content      |
  | title         | VARCHAR   | Title of the content |
  | director      | VARCHAR   | Director(s)          |
  | cast          | VARCHAR   | Cast members         |
  | country       | VARCHAR   | Country of origin    |
  | release_year  | INTEGER   | Year of release      |
  | rating        | VARCHAR   | Content rating       |
  | duration      | VARCHAR   | Duration             |
  | listed_in     | VARCHAR   | Genre(s)             |
  | description   | VARCHAR   | Description          |

## Conclusion

This ETL project successfully cleans and loads the Netflix Titles dataset into a relational database, making it easier to query and analyze the data for further insights and applications.

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




