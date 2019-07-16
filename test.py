# coding utf-8
import csv
import pandas as pd
address=pd.read_csv("sentiment_analysis_trainingset.csv",usecols=[1])
print(address)
address.to_csv("pre_results.csv")