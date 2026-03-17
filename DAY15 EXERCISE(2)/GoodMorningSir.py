import time

hour = int(time.strftime('%H'))

if hour < 12:
    print("Good Morning Sir")
elif 12 <= hour < 17:
    print("Good Afternoon Sir")
elif 17 <= hour < 20:
    print("Good Evening Sir")
else:
    print("Good Night Sir")
