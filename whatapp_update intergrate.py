
import os
import pandas as pd
import pywhatkit as kit
from datetime import datetime

if os.path.isfile("C:data.csv"):
    df=pd.read_csv('C:data.csv')
    #data=df[['number','ID']]
    time = datetime.now()
    msg =input("Enter the message: ")
    for i,j in df.iterrows():
        time = datetime.now()
        number_temp=j['number']   
        if len(str(number_temp))==11:
            kit.sendwhatmsg(f"+91-{int(str(number_temp)[1:])}",msg,time.hour,time.minute+1,10)
        else:
            kit.sendwhatmsg(f"+91-{number_temp}",msg,time.hour,time.minute+1,10)
