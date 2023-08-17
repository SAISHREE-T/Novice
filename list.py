LIST=[1,2,3,4,5,5,7,8,10,6]
#METHODS
print(LIST.count(2))
LIST.pop()   #REMOVE THE LAST TERM
print(LIST)
LIST.remove(3)
print(LIST)
LIST.insert(6,7)
print(LIST)
LIST.append(9)   #ADDS THE ITEM TO END OF LIST
print(LIST)
#LIST.clear()
print(LIST)
LIST.sort()
print(LIST)
LIST.reverse()
print(LIST)

                     #EXERSCISE
list=[1,1,2,3,3,3,4,5,5]
for x in list:
    if list.count(x)>1:
        list.remove(x)
print(list)
        #OR
numbers=[1,1,2,3,3,3,4,5,5]
uniques=[]
for x in numbers:
    if x not in uniques:
        uniques.append(x)
print(uniques)


        #TUPLES
#SIMILAR TO LISTS BUT HAVE PARANTHESIS INSTEAD OF SQUARE BRACKETS, THEY HAVE NO METHODS OTHER THAT "COUNT" AND "INDEX".
truple=(1,1,2,3,14,16)
print(truple.count(1))
print(truple.index(14))

#UNPACKING- FOR BOTH LISTS AND TRUPLES
coordinates=(1,2,3)
x,y,z=coordinates
print(x)
print(x*y*z)
cordinates=[1,3,5]
p,q,r=cordinates
print(p)
