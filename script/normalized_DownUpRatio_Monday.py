import pandas as pd
from matplotlib import pyplot as plt

#Changing from float64 into int64, for data types consistency   

monday_df = pd.read_csv('../data/raw_data/Monday-WorkingHours.pcap_ISCX_without_Cleansing.csv', engine = 'python')

du_ratio_f = monday_df[' Down/Up Ratio'].astype('Int64')
empty_entries = du_ratio_f.isnull().sum().sum() # Count total empty entries
print(f"Total empty entries: {empty_entries}")
print(f"Max value : {max(du_ratio_f)}")
print(f"Min value : {min(du_ratio_f)}")

series = pd.Series(du_ratio_f)
frequency_table = series.value_counts()
print(frequency_table)
print(monday_df.dtypes)

du_ratio_f.to_csv('../data/Monday-DownUp-Ratio.csv', index = False)

# print(du_ratio_f)