import pandas as pd
from matplotlib import pyplot as plt


monday_df = pd.read_csv('../data/Monday-filtered.csv', engine = 'python')

du_ratio_f = monday_df['Down/Up Ratio'].astype('Int64')
empty_entries = du_ratio_f.isnull().sum().sum()
print(f"Total empty entries: {empty_entries}")
print(f"Max value : {max(du_ratio_f)}")
print(f"Min value : {min(du_ratio_f)}")

series = pd.Series(du_ratio_f)
frequency_table = series.value_counts()
print(frequency_table)
print(monday_df.dtypes)

du_ratio_f.to_csv('../data/Monday-DownUp-Ratio.csv', index = False)

wednesday_data = pd.read_csv('../data/Wednesday-filtered.csv', engine = 'python')

du_ratio_f = wednesday_data[' Down/Up Ratio']
empty_entries = du_ratio_f.isnull().sum().sum()
print(f"Total empty entries: {empty_entries}")
print(f"Max value : {max(du_ratio_f)}")
print(f"Min value : {min(du_ratio_f)}")

series = pd.Series(du_ratio_f)
frequency_table = series.value_counts()
print(frequency_table)

du_ratio_f.to_csv('../data/Wednesday-DownUp-Ratio.csv', index = False)
