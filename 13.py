import pandas as pd

data_url = 'http://bit.ly/2cLzoxH'
gapminder = pd.read_csv(data_url)
gapminder.head(n=3)

print(gapminder.columns)

