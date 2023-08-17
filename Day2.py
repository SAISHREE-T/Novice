a=8
a+=14
print(a)

print("Welcome to my calculater, here you can calculate the circumference of a circle ")
r=input("radius: ")
pi=3.14
circumference=2*pi*int(r)
print("The circumference of the circle is: ",circumference )
x="Lelouch"
print(id(x))
print(type(x))

# '''Hi
# I am your
# first # comment'''
print("Here you can create a greeting for a person for a particular occasion! please enter the following.")
#The person's name
name= input(" Enter the name of the person: ")
#the occasion
occasion= input("enter the occasion{Birthday/New year/Christmas/Diwali} ")
if(occasion=='Birthday'):
    print("Happy Birthday!! "+ name)
elif(occasion=='Diwali'):
    print(f'Happy Diwali, {name} ')
elif(occasion=="Christmas"):
    print('''Happy Christmas '''
          + name)
elif(occasion=='New year'):
    print('Happy New year '+name)
else:
    print("Invalid entry")
