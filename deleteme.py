#!/usr/bin/env python
import pandas as pd
import os

"""
========================================================================
The data consists of six files, one for each year between 2005 and 2011. Each year's worth of data includes the general population of each US state, a count of suicides, a count of state veterans, and a count of veteran suicides.
========================================================================
A good goal for using a decision tree in your project could be to predict the likelihood of suicide among veterans based on various factors. Factors might include:

    Demographics (age, gender, race)
    Geographic location
    Military service details (e.g., branch, combat experience)
    Socioeconomic factors (employment status, income level)
    Health-related factors (physical injuries, mental health conditions)
"""

def find_directory(directory_name):
    """
    Starting with the parent directory by default, search through all
    directories until the inputted director name is reached, then return file
    path
    ------------------------------------------------------------
    Inputs:
        directory_name: (str)

    Outputs:
        
    """
    # Establish root path in directory above the current directory
    root_path = os.getcwd()

    for dirpath, dirnames, filenames in os.walk(root_path):

        if directory_name in dirnames:
            return root_path + '/' + directory_name + '/'

    return "./"

def consolidate_csv(directory):
    """
    Consolidates the multiple csv files into one dataset.
    """
    csv_files = [file for file in os.listdir(directory) if file.endswith(".csv")]
    # Sort to maintains date order
    csv_files.sort()
    breakpoint()
    dataframes = [pd.read_csv(os.path.join(directory, file), index_col=False) for file in csv_files]
    # Concatenate without inserting new column for indices
    combined = pd.concat(dataframes, ignore_index=True)

    return combined

def missing_values(dataframe):
    """
    Checks for missing or inconsistent data.
    - Delete records or features, impute missing values via:
        1) Mean/medium/mode 
        2) random
        3) k-nearest neighbors
        4) regression
        5) interpolation
    ------------------------------------------------------------
    input:

    outputs:

    """
    pass

directory_name = "data"
thing = find_directory(directory_name)
breakpoint()

#combined = consolidate_csv(thing)
#columns = list(combined.columns) # List of column names

#breakpoint()

# Write to csv file
#combined.to_csv(thing + "combined.csv", index=False)
