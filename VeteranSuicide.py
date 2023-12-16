#!/usr/bin/env python
import pandas as pd
from os import path


class VeteranSuicide(object):

    def __init__(self):
        self.data = None
        self.decision_tree = None


class DataPreparation(object):

    def __init__(self):
        self.data_files = []

    def find_files(self, target_filename):
        """
        Automatically finds target dicrectory
        """


