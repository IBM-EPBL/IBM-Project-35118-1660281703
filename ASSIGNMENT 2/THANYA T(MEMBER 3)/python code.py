print("TEMPERATURE AND HUMIDITY ALERT SYSTEM")
import random
a=random.randint(1,100)
b=random.randint(1,50)
if((a<=40)&(b<=30)):
    print("TEMP IS MODERATE:",a,"%")
    print("HUM IS MODERATE:",b,"%")
    print("ALARM OFF")
if((a<=40)&(b>=30)):
    print("TEMP IS LOW:",a,"%")
    print("HUM IS HIGH:",b,"%")
    print("ALARM OFF")
if((a>=40)&(b<=30)):
    print("TEMP IS HIGH:",a,"%")
    print("HUM IS HIGH:",b,"%")
    print("ALARM ON")
if((a>=40)&(b>=30)):
    print("TEMP IS HIGH:",a,"%")
    print("HUM IS LOW:",b,"%")
    print("ALARM ON")
else:
    print("TEMP IS TOO LOW:",a,"%")
    print("HUM IS TOO LOW:",b,"%")
    print("ALARM OFF")