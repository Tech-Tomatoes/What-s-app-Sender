import pywhatkit
import csv
from datetime import datetime
print("Enter the number")
message = ["Hello","Welcome in Tech Tomatoes","Are u looking for intership"]
for i in range(len(message)):
        print(f"{i} - {message[i]}")
msg = message[int(input())]        
with open("FilePath.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        time = datetime.now()
        pywhatkit.sendwhatmsg(f"+91-{row[1]}",msg,time.hour,time.minute+1,5)
