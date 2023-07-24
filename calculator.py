print("Hi, welcome to my first calculator!")
oper= input("Which operation would you like to perform?(Addition, Subtraction, Multiplication, Division) : ")
first_no=int(input("Enter the first number (x): "))
sec_no= int(input("Enter the second number (y): "))
try:
 if oper.capitalize() == "Addition":
        print(f"x+y = {first_no + sec_no}")
 elif oper.capitalize()== "Subtraction":
     print(f"x-y = {first_no - sec_no}")
 elif oper.capitalize()== "Multiplication":
     print(f"x.y = {first_no * sec_no}")
 elif oper.capitalize()== "Division":
     print(f"x/y = {first_no/sec_no}")
 else:
     print("Invalid input! Try again!")
except ValueError:
    print('Invalid entry!!')
except ZeroDivisionError:
    print("A number can't be divided by zero!!")



