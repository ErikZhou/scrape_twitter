# coding: utf-8

# In[ ]:
import pandas as pd
import os
import sys
import glob
import re
from datetime import datetime
from dateutil.parser import parse


# Function definition is here
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


def df_to_csv(data_list, filename, rate):
    df = pd.DataFrame(data_list, columns=['datetime', 'message'])
    final_df = df.sort_values(by='datetime',ascending=[False])
    final_df.to_csv(filename + '_' + str(rate) + '.csv', sep='\t', encoding='utf-8')
    return


def csv_sort(filename):
    csv_file_name = filename
    df = pd.read_csv(csv_file_name,delimiter="\t")
    #print(df)
    print(df.shape)
    data_list = []
    data_list_0_5 = []
    index = 0
    for i in range(df.shape[0]):
        print('=======index=',index)
        line = df.iloc[i,0]
        dt = line[0:19] 
        print('datatime=', dt)
        #print(line[24:])
        #dt1 = '2018-06-29 08:15:27'
        dtstr = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        index += 1
        #if index > 20 :
        #    continue

        #print(line)
        data_list.append([dtstr, line[24:]])
    df_to_csv(data_list, filename, '')
    return


def main():
    for arg in sys.argv[1:]:
        print(arg)
    filename = sys.argv[1]
    csv_sort(filename)


if __name__ == "__main__":
    main()

