import pandas as pd


class DecisionTreeAlgorithm:
    csv = None

    def __init__(self, csv):
        self.csv = csv

    def print_csv_head(self):
        print(self.csv)
