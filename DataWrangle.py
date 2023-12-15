#!/usr/bin/env python
import pandas as pd

class DataWrangle(object):

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.columns = dataframe.columns # List of columns

    def data_clean(self):
        """
        Check for missing or consistent data, especially geographical
        information.
        """
        pass

    def eda(self):
            """
            Use visualizations to understand the distribution of veterans across different geographical areas. 
            Heatmaps or choropleth maps can be particularly useful.
            """
            pass

    def stats(self):
        """
        Analyze the concentration of veterans in different areas. 
        You might use population density metrics and compare them with general population data.
        """
        pass


