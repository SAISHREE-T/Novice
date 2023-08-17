

first="saishree"
second="mika"
fact= first+"[" + second+"] " + " are the same!!"  #STRING CONCATENATION
print(fact)
fact=f"{first} and [{second}] are the same!!"         #FORMATED STRING
print(fact)


# METHODS AND FUNCTIONS
#METHODS ARE LIMITED TO PARTICULAR TYPES e.g capitalize, upper, lower, find, replace .....
#FUNCTIONS ARE FOR GENERAL PURPOSE e.g  print, len ....
var="Python for beginners"
print(len(var))     # function
#METHODS
print(var.lower())
var.upper()
print(var.replace("Python ", "Jython "))
print(var.find('p'))
print(var.find('P'))
print(var.find("beginners"))
print("Python" in var)

#Arthematic operators
print(10+3)
print(10-3)
print(10*3)
print(10/3)  #DIVISION
print(10//3)  #QUTIOENT
print(10**3)   #POWER
print(10%3)    #name=modulus function BUT GIVES the REMAINDER
x=3
x+=10
print(x)
# -=, *= , /=, //=, **=    (aka AUGUMENTED ASSIGNMENT OPERATOR)

y=2
y**=3
print(y)
#MATH FUNCTIONS
a=2.8899
print(round(a))
print(round(8.3))
print(abs(-7.9))
print(round(-7.1))

