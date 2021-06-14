
import os
import pandas as pd
import pywhatkit as kit
from datetime import datetime

if os.path.isfile("data.csv"):
    df=pd.read_csv('data.csv')
    #data=df[['number','ID']]
    print(df.iterrows)
    time = datetime.now()
    for i,j in df.iterrows():
        time = datetime.now()
        number_temp=j['number']
        ID_temp=j['ID']
        msg='Hello Customer,\n Your transation is successful and your transation ID is {}'.format(ID_temp)
        if len(str(number_temp))==11:
            kit.sendwhatmsg(f"+91-{int(str(number_temp)[1:])}",msg,time.hour,time.minute+1,10)
        else:
            kit.sendwhatmsg(f"+91-{number_temp}",msg,time.hour,time.minute+1,10)
