# from datetime import datetime
# today=datetime.now()
# print(today)
# k=today.date()
# d=today.time()
# print(d,k)

# from datetime import datetime
# today=datetime.now()
# d=today.date()
# print('Year:',d.year)
# print('Month:',d.month)
# print('Day:',d.day)
# t=today.time()
# print("Hour:",t.hour)
# print("Minute:",t.minute)
# print("Seconds:",t.second)
# print("Microsecond:",t.microsecond)

# from datetime import datetime,timedelta
# today=datetime.now()
# today1=today+timedelta(days=5)
# print(today1)


# from datetime import datetime
# time_24 = '19:35'
# time_12 = datetime.strptime(time_24, "%H:%M").strftime("%I:%M %p") 
# print(time_12)

import pyttsx3
from datetime import datetime
k=pyttsx3.init()
alarm_time="17:59"

while True:
    present_time=datetime.now().strftime('%H:%M')
    if alarm_time==present_time:
        for i in range(5):
            k.setProperty('rate',120)
            voices=k.getProperty('voices')
            k.setProperty('voice',voices[0].id)
            k.say('good morning gopi')
            k.runAndWait()
        break    