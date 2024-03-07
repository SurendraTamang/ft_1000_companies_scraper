import pandas as pd
pd.read_html("https://www.ft.com/ft1000-2024")[0].to_csv('data/pd_ft1000.csv', index=False)