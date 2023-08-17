try:
    age=int(input("Age: "))
    print(age)
except ValueError:
    print('Invalid entry!!')
except ZeroDivisionError:
    print("age can't be zero!!")