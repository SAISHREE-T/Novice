ct=int(input("Enter the current time in 24hr format: "))
ar=int(input("Number of hours for the alarm: "))
import math
if ct>=12:
    nt=ct-12
    print(f"Current time in 12 hr format:{nt}")
else:
    nt=ct
    print(f"Current time in 12 hr format:{nt}")
at= ar%24+nt
if at<=12:
    print("The alarm rings at",at)
elif at>12 and at<24:
    print("The alarm rings at", at-12)
else:
    print("The alarm rings at", at - 24)
