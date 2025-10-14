import argparse
import pandas as pd

parser = argparse.ArgumentParser()

parser.add_argument('-filename', help="specify the filename with file extension")

args = parser.parse_args()


dataframe = pd.read_csv(args.filename)
print(dataframe['age'].describe())