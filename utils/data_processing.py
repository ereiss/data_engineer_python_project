# data_processing.py

import pandas as pd

# Change some columns names for clarity purpose
class change_columns_names:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def change_column_names(self, new_names_mapping):
        print(">>> Changing columns names:")
        print("*******************************************************")
        for old_name, new_name in new_names_mapping.items():
            if old_name in self.dataframe.columns:
                self.dataframe.rename(columns={old_name: new_name}, inplace=True)
                print(f"--  Changed column name '{old_name}' to '{new_name}'.")
            else:
                print(f"--  Column '{old_name}' does not exist.")
        print("*******************************************************\n")
        return self.dataframe


# Drop non business value columns
class drop_columns:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def drop_columns(self, columns_to_drop):
        print(">>> Dropping columns names:")
        print("*******************************************************")
        for column_name in columns_to_drop:
            if column_name in self.dataframe.columns:
                self.dataframe.drop(columns=column_name, inplace=True)
                print(f"Success: Dropped column '{column_name}'.")
            else:
                print(f"Column '{column_name}' does not exist.")
        print("*******************************************************\n")
        return self.dataframe

# Dealing with NULL values: > replace NULLs (keeping rows), delete NULL rows
class handle_null_values:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def replace_nulls(self, replace_null_mapping):
        print(">>> Replace NULL values:")
        print("*******************************************************")
        for column_name, value_to_replace in replace_null_mapping.items():
          if column_name in self.dataframe.columns:
            if self.dataframe[column_name].isnull().any():
            #  self.dataframe[column_name].fillna(value_to_replace, inplace=True)
              self.dataframe[column_name] = self.dataframe[column_name].fillna(value_to_replace)
              print(f"Column '{column_name}' null value is changed to '{value_to_replace}'")
            else:
              print(f"Column '{column_name}' has no null values. nothing to change to")
          else:
            print(f"Column '{column_name}' does not exist in the DataFrame.")
        print("*******************************************************\n")
        return self.dataframe

    def delete_nulls(self, columns_delete_null):
        print(">>> Remove NULL values:")
        print("*******************************************************")
        for column_name in columns_delete_null:
          if column_name in self.dataframe.columns:
            if self.dataframe[column_name].isnull().any():
              self.dataframe.dropna(subset=[column_name], inplace=True)
              print(f"Column '{column_name}' null values has deleted")
            else:
              print(f"Column '{column_name}' has no null values. no need to delete anything")
          else:
            print(f"Column '{column_name}' does not exist in the DataFrame.")
        print("*******************************************************\n")
        return self.dataframe

# Columns with multiple values in each rows should be splitted into multiple rows
class handle_splitting_columns:
  def __init__(self, dataframe):
    self.dataframe = dataframe

  def _is_split_required(self, column_name):
    if self.dataframe[column_name].str.contains(',').any():
      return True
    else:
      return False

  def split_columns(self, columns_to_split):
    print(">>> Split and explode columns:")
    print("*******************************************************")
    for column_name in columns_to_split:
      if column_name in self.dataframe.columns:
        if self._is_split_required(column_name):
          self.dataframe[column_name] = self.dataframe[column_name].str.split(',')
          self.dataframe = self.dataframe.explode(column_name, ignore_index=True)
          print(f"Column '{column_name}' has splitted and exploded successfully")
        else:
          print(f"Column '{column_name}' is not required to be splitted")
      else:
        print(f"Column '{column_name}' does not exist")
    print("*******************************************************\n")
    return self.dataframe

# Remove leading/trailing spaces
class handle_trim_whitespace:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def trim_columns(self, columns_to_trim):
      print(">>> Remove leading/trailing spaces:")
      print("*******************************************************")
      for column_name in columns_to_trim:
        if column_name in self.dataframe.columns:
            if self.dataframe[column_name].dtype == 'object':
                self.dataframe[column_name] = self.dataframe[column_name].str.strip()
                print(f"Trimmed whitespace from column '{column_name}'.")
            else:
                print(f"Column '{column_name}' is not of type 'object'.")
        else:
            print(f"Column '{column_name}' does not exist.")
      print("*******************************************************\n")
      return self.dataframe

# Changing columns values based on change_values_mapping
class handle_change_columns_values:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def change_column_values(self, change_values_mapping):
        print(">>> Change columns values:")
        print("*******************************************************")
        for column_name, mapping in change_values_mapping.items():
            if column_name in self.dataframe.columns:
              for old_value, new_value in mapping.items():
                  self.dataframe[column_name] = self.dataframe[column_name].replace(mapping)
              print(f"'{column_name}' values has changed as required")
            else:
              print(f"Column '{column_name}' does not exist")

        print("*******************************************************\n")
        return self.dataframe

    def delete_column_values(self, change_values_mapping):
        print(">>> Delete columns values:")
        print("*******************************************************")
        for column_name, mapping in change_values_mapping.items():
            if column_name in self.dataframe.columns:
              self.dataframe = self.dataframe[~self.dataframe[column_name].isin(mapping)]
              print(f"'{column_name}' rows are deleted as specified")
            else:
              print(f"Column '{column_name}' does not exist")

        print("*******************************************************\n")
        return self.dataframe

class handle_duplicate_rows:
    def __init__(self, dataframe):
         self.dataframe= dataframe.copy()
    
    def _has_duplicates(self):
        has_duplicates = self.dataframe.duplicated().any()
        if has_duplicates:
           return True
        else:
           return False
    
    def remove_duplicates(self):
        print(">>> Remove duplicate rows:")
        print("*******************************************************")
        
        # Get the number of duplicate rows
        num_duplicates = self.dataframe.duplicated().sum()
        
        # Remove duplicate rows
        if self._has_duplicates():
           self.dataframe.drop_duplicates(inplace=True)
           self.dataframe.reset_index(drop=True, inplace=True)
           print(f"{num_duplicates} duplicate rows has removed successfully.")

        else:
           print(f"No duplicate rows to remove.")
        
        print("*******************************************************\n")
        return self.dataframe