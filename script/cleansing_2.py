import matplotlib.pyplot as plt
import numpy as np
import pandas

files =  [r"Monday-WorkingHours.pcap_ISCX.csv", r"Wednesday-workingHours.pcap_ISCX.csv"]

for f in files :
    # reading CSV file
    data = pandas.read_csv(f)      
    
    # converting column data to list
    FD = data[' Flow Duration'].tolist()
    TFwdP = data[' Total Fwd Packets'].tolist()
    TBwdP = data[' Total Backward Packets'].tolist()
    FDNew = []
    TFwdPNew = []
    TBwdPNew = []
    for i in range(len(FD)) :
        if FD[i] <= 0 :
            FDNew.append(FD[i - 1])
        else :
            FDNew.append(FD[i])

        if TFwdP[i] < 0 :
            TFwdPNew.append(TFwdP[i - 1])
        else :
            TFwdPNew.append(TFwdP[i])

        if TBwdP[i] < 0 :
            TBwdPNew.append(TBwdP[i - 1])
        else :
            TBwdPNew.append(TBwdP[i])

    data[' Flow Duration'] = '0'
    data[' Flow Duration'] = np.array(FDNew)
    data[' Total Fwd Packets'] = '0'
    data[' Total Fwd Packets'] = np.array(TFwdPNew)
    data[' Total Backward Packets'] = '0'
    data[' Total Backward Packets'] = np.array(TBwdPNew)

    data.to_csv(f, index=False)