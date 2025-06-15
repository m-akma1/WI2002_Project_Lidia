import pandas as pd
from matplotlib import pyplot as plt

#Nothing changed just separating data from raw_data

wednesday_data = pd.read_csv('../data/raw_data/Wednesday-workingHours.pcap_ISCX_without_Cleansing.csv', engine = 'python')

ACK_f = wednesday_data[' ACK Flag Count']
SYN_f = wednesday_data[' SYN Flag Count']
empty_entries_ack = ACK_f.isnull().sum().sum() # Count total empty entries
empty_entries_syn= SYN_f.isnull().sum().sum() # Count total empty entries
print("\nACK FLAG")
print(f"Total empty entries: {empty_entries_ack}")
print(f"Max value : {max(ACK_f)}")
print(f"Min value : {min(ACK_f)}")
series = pd.Series(ACK_f)
frequency_table = series.value_counts()
print(frequency_table)

print("\nSYN FLAG")
print(f"Total empty entries: {empty_entries_syn}")
print(f"Max value : {max(SYN_f)}")
print(f"Min value : {min(SYN_f)}")
series = pd.Series(SYN_f)
frequency_table = series.value_counts()
print(frequency_table)

SYN_f.to_csv('../data/Wednesday-DownUp-Ratio.csv', index = False)
ACK_f.to_csv('../data/Wednesday-DownUp-Ratio.csv', index = False)

# print(du_ratio_f)