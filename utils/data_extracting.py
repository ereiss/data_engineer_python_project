# data_extracting.py

import pandas as pd

# Extract csv file from google drive
class google_drive_csv_reader:
    def __init__(self, file_url, dataset_name):
        self.file_url = file_url
        self.dataset_name = dataset_name

    def _csv_drive_path_generatoer(self):
        path = 'https://drive.google.com/uc?export=download&id='+ self.file_url.split('/')[-2]
        return path

    def read_csv_to_dataframe(self):
        print("\n>>> Extract file from google drive:")
        print("*******************************************************")
        df = pd.read_csv(self._csv_drive_path_generatoer())
        print(f"--  Dataset '{self.dataset_name}' is extracted successfully.")
        print("*******************************************************\n")
        return df