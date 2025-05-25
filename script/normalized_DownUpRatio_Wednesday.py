import pandas as pd
from matplotlib import pyplot as plt

#Nothing changed just separating data from 

wednesday_data = pd.read_csv('../data/raw_data/Wednesday-workingHours.pcap_ISCX_without_Cleansing.csv', engine = 'python')

du_ratio_f = wednesday_data[' Down/Up Ratio']
empty_entries = du_ratio_f.isnull().sum().sum() # Count total empty entries
print(f"Total empty entries: {empty_entries}")
print(f"Max value : {max(du_ratio_f)}")
print(f"Min value : {min(du_ratio_f)}")

series = pd.Series(du_ratio_f)
frequency_table = series.value_counts()
print(frequency_table)

du_ratio_f.to_csv('../data/Wednesday-DownUp-Ratio.csv', index = False)

# print(du_ratio_f)