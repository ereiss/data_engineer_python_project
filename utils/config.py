# config.py

# Constants
GOOGLE_DRIVE_DATA_URL = "https://drive.google.com/file/d/1SfmhSUwFKQ4EZ9aa1l86-3EAxx0-NASI/view?usp=sharing"
DATASET_NAME = "netflix_title.csv"
DATABASE_NAME = "data/netflix.db"

# Mapping criteria
CHANGE_COLUMN_NAMES_MAPPING = { 'cast': 'actor',
                                'listed_in': 'genres'}

REPLACE_NULL_MAPPING = {'director': 'No Director',
                        'actor': 'No Actor',
                        'country': 'No Country'}

CHANGE_VALUES_MAPPING = {'country': {'West Germany': 'Germany',
                                     'East Germany': 'Germany',
                                     'Soviet Union': 'Russia'},
                         'duration': {'1 Season': '1 Seasons'},
                         'genres': {'TV Dramas': 'Dramas',
                                    'International Movies': 'International',
                                    'International TV Shows': 'International',
                                    'TV Comedies': 'Comedies',
                                    'TV Action & Adventure': 'Action & Adventure',
                                    'Independent Movies': 'Independent',
                                    'TV Thrillers': 'Thrillers',
                                    'Romantic TV Shows': 'Romantic',
                                    'Romantic Movies': 'Romantic',
                                    'Horror Movies': 'Horror',
                                    'TV Horror': 'Horror',
                                    'Docuseries': 'Documentaries',
                                    'Anime Series': 'Anime',
                                    'Anime Features': 'Anime',
                                    'Spanish-Language TV Shows': 'Spanish-Language',
                                    'British TV Shows': 'British',
                                    'Sports Movies': 'Sports',
                                    'TV Mysteries': 'Mysteries',
                                    "Kids' TV": 'Children & Family',
                                    'Children & Family Movies': 'Children & Family',
                                    'TV Sci-Fi & Fantasy': 'Sci-Fi & Fantasy',
                                    'Crime TV Shows': 'Crime',
                                    'Korean TV Shows': 'Korean',
                                    'Classic Movies': 'Classic',
                                    'Cult Movies': 'Classic',
                                    'Classic & Cult TV': 'Classic',
                                    'Teen TV Shows': 'Teen',
                                    'LGBTQ Movies': 'LGBTQ',
                                    'Reality TV': 'Reality',
                                    'Stand-Up Comedy & Talk Shows': 'Stand-Up Comedy',
                                    'Science & Nature TV': 'Science & Nature'}}

DELETE_VALUES_MAPPING = {'genres': ['TV Shows', 'Movies']}
DB_TABLES = {'netflix_directors':['type', 'title', 'director', 'date_added', 
                                  'release_year', 'rating', 'duration', 
                                  'duration_digits', 'duration_unit', 
                                  'year_added', 'month_added', 'day_added'],
            'netflix_actors':['type', 'title', 'actor', 'date_added', 
                              'release_year', 'rating', 'duration', 
                              'duration_digits', 'duration_unit', 
                              'year_added', 'month_added', 'day_added'],
            'netflix_countries':['type', 'title', 'country', 'date_added', 
                                 'release_year', 'rating', 'duration', 
                                 'duration_digits', 'duration_unit', 
                                 'year_added', 'month_added', 'day_added'],
            'netflix_genres':['type', 'title', 'genres', 'date_added', 
                              'release_year', 'rating', 'duration', 
                              'duration_digits', 'duration_unit', 
                              'year_added', 'month_added', 'day_added'],
            'netflix_titles_all':['type', 'title', 'date_added', 
                                  'release_year', 'rating', 'duration', 
                                  'duration_digits', 'duration_unit', 
                                  'year_added', 'month_added', 'day_added']
            }

# Lists
COLUMNS_TO_DROP = ['show_id', 'description']
COLUMNS_TO_DELETE_NULL = ['date_added', 'rating', 'duration']
COLUMNS_TO_SPLIT = ['director', 'actor', 'country', 'genres']
COLUMNS_TO_TRIM = ['director', 'actor', 'country', 'genres', 'date_added']


