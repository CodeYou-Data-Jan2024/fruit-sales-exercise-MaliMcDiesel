import pandas as pd


df = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

df.to_csv('fruit.csv')

