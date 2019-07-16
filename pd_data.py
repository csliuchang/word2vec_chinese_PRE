# coding utf-8





import pandas as pd

data = pd.read_csv("sentiment_analysis_trainingset.csv")

srdata=data.loc[:, ['content']]

with open('results.txt', 'w', encoding='UTF-8') as outfile:

    srdata.to_string(outfile)
