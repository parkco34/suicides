#!/usr/bin/env python
import pandas as pd
import os


class VeteranSuicide(object):

    def __init__(self):
        self.data = None
        self.decision_tree = None


class DataPreparation(object):
    """
    Data wrangling
    """
    def __init__(self, target_directory="data"):
        self.data_files = []
        self.target_directory = target_directory

    def get_files(self, csv_files=[]):
        """
        Assuming we're in target directory, collect all csv files and return a
        sorted list of the files.
        If not, search down until target directory is found.
        --------------------------------------------------------
        Inputs:
            csv_files: (list) List of csv files .(Default: empty list)
        """
        # Current directory
        self.current_dir = os.getcwd()

        # If target directory not the current one, search for it from here
        if self.current_dir != self.target_directory:
            for root, dirs, files in os.walk(self.current_dir):
                # If target directory in the subdirectories, collect csv files
                for dir in dirs:
                    if dir == self.target_directory:
                        # Store csv files in a list
                        csv_files = [file for file in
                                     os.listdir(self.target_directory) if
                                     file.endswith(".csv")]
                        # Sort csv files in ascending order
                        csv_files.sort()
                        # Success
                        return csv_files
            # Failure
            return None

        else:
            csv_files = [file for file in os.listdir() if file.endswith(".csv")]
            csv_files.sort()
            return csv_files


    def consolidate_csv(self, files_list):
        """
        Consolidates csv files into one pandas dataframe.
        ------------------------------------------------------------
        Inputs:
            files_list: (list) List of csv files.

        Outputs:
            dataframe: (pandas DataFrame) One dataframe with all dataframes
            concatenated.
        """
        # List of dataframes
        dataframes = [pd.read_csv(os.path.join(self.current_dir,
                                               self.target_directory + "/" +  file), index_col=False) for file in files_list]
        # Concatenate into one dataframe
        dataframe = pd.concat(dataframes, ignore_index=True)
        return dataframe

    def clean_data(self, dataframe):
        """
        Removes unwanted features (columns) from dataframe:
            - Begins with "Unnamed"
            - Ends with "_p" or "rate"
        ---------------------------------------------------------------
        Inputs:
            dataframe: (pandas DataFrame)

        Outputs:
            df_cleaned: (pandas DataFrame) without unwanted columns.
        """
        # Columns that start with "Unnamed"
        unnamed_cols = dataframe.filter(regex="^Unnamed").columns
        # Columns with "_p" or "rate"
        special_cols = dataframe.filter(regex="_p$|rate$").columns
        # # Combine both lists
        columns_to_drop = unnamed_cols.union(special_cols)
        # Drop columns!
        df_cleaned = dataframe.drop(columns=columns_to_drop)

        return df_cleaned

prep = DataPreparation() # DataPreparation object
files = prep.get_files()
dataframe = prep.consolidate_csv(files)
df_cleaned = prep.clean_data(dataframe)
breakpoint()
df_cleaned.to_csv("~/Desktop/df_cleaned.csv", index=False)
