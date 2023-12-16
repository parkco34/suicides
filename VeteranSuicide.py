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
        current_dir = os.getcwd()

        # If target directory not the current one, search for it from here
        if current_dir != self.target_directory:

            for root, dirs, files in os.walk(current_dir):
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


    def consolidate_csv(self):
        """
        Consolidates csv files into one pandas dataframe.
        ------------------------------------------------------------
        Inputs:

        Outputs:

        """
        pass

        

prep = DataPreparation() # DataPreparation object
files = prep.get_files()
breakpoint()
