"""
Create a countdown timer
1) Function to take time in seconds and print out a formatted string
    use this function to create a countdown timer
2) Countdown timer will start at a given time and count down to zero
At each second, it will print out the remaining time
When the timer reaches zero, it will print out a message saying " Time's up!"
"""
import datetime

#convert = str(datetime.timedelta(seconds = var_sec))
#print(convert)
def countdown_timer():
    var_sec = int(input("Enter seconds: "))
    for i in range(var_sec, 0, -1):
        convert = str(datetime.timedelta(seconds = i))
        print(convert)
        #print(i, "seconds left")
    print("Time's up!")

countdown_timer()