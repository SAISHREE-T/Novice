
for n in [1,1,1,1,4]:
    for l in ["x"]:
        print(n*l)
names= ["mika","saishree","loukya","karthik","bhoomika"]
names[2]="Saishree"

print(names[2:])
list= [1,2,3,4,5]
max=list[0]
for x in list:
    if x>max:
       max=x
print(max)
#2D LISTS- EACH ITEM IN A 2D LIST IS ANOTHER LIST
matrix=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
]

print(matrix[2][2])
for row in matrix:
    for item in row:
        print(item)

matrix[1][2]=10
print(matrix)