import pandas as pd
file_monday = r"C:\smthshit\Lidia\Monday-WorkingHours.pcap_ISCX.csv"
df_monday = pd.read_csv(file_monday)
df_monday.columns = df_monday.columns.str.strip()

df_monday_clean = df_monday[
    (df_monday['Average Packet Size'] > 0) &
    (df_monday['Active Mean'] > 0) &
    (df_monday['Idle Mean'] > 0)
]

df_monday_clean.to_csv(file_monday, index=False)
print(f"Data Monday bersih disimpan ke: {file_monday}")

file_wednesday = r"C:\smthshit\Lidia\Wednesday-workingHours.pcap_ISCX.csv"
df_wednesday = pd.read_csv(file_wednesday)
df_wednesday.columns = df_wednesday.columns.str.strip()

df_wednesday_clean = df_wednesday[
    (df_wednesday['Average Packet Size'] > 0) &
    (df_wednesday['Active Mean'] > 0) &
    (df_wednesday['Idle Mean'] > 0)
]

df_wednesday_clean.to_csv(file_wednesday, index=False)
print(f"Data Wednesday bersih disimpan ke: {file_wednesday}")
