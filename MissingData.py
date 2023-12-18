#!/usr/bin/env python
from textwrap import dedent
import pandas as pd
import matplotlib.pyplot as plt


class MissingData(object):

    def __init__(self, dataframe):
        self.data = dataframe

    def report_missing_values(self):
        """
        Reports percentage of missing values for each column.
        """
        # Sum of missing values
        missing_values = self.data.isnull().sum()
        total_values = self.data.count()
        missing_percent = (missing_values / total) * 100
        # Missing percentage in descending order
        return missing_percent.sort_values(ascending=False)

    def suggest_imputation_methods(self):
        """
        Suggests imputation methods based on the type of data and the amount of
        missing data.
        """
        suggestions = {}
        missing_percentage = self.report_missing_values()

        for col, percentage in missing_percentage.items():
        # Skip columns with no missing values.
            if percentage == 0:
                continue 

            # Suggest different techniques
            if percentage > 50:
                suggestions[col] = dedent("""Consider dropping (more than 50% of data
                missing)""")

            elif (self.data[col].dtype == "float64" or 
            self.data[col].dtype == "int64"):
                suggestions[col] = dedent("Mean/Median Imputation or Regression Imputation")

            else:
                suggestions[col] =  dedent("""Mode imputation or predictive model""")

            return suggestions

    def plot_missingdata(df, title, xlabel, ylabel):
        ''' This function takes a data frame as input plots the list of columns with corresponding total number of missing values'''
        # Let us see what columns have missing values
        # Total number of entries (rows X columns) in the dataset
        total= df.size
        #Number of missing values per column
        missingCount = df.isnull().sum()
        #Total number of missing values
        missing_tot = missingCount.sum()
        # Calculate percentage of missing values
        print("The dataset contains", round(((missing_tot/total) * 100), 2), "%", "missing values")

        # keeping only the columns with missing values>0 
        missing = missingCount[missingCount > 0] 
        print(missing)
        # sorting in order of missing values and making the change to original missing series
        missing.sort_values(inplace=True) 
        missing.plot.bar()
        plt.title(title, size=15,loc='left')
        plt.xticks(fontsize=11,rotation=45)
        plt.yticks(fontsize=11)
        plt.xlabel(xlabel, fontsize=13)
        plt.ylabel(ylabel, fontsize=13)
        plt.show()
    

