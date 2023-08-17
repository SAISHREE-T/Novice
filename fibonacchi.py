n=int(input("How many numbers of the fibonacci series would you want? :  "))
f=0
s=1
count=0
print(f )
print(s)
while count<n-2:
  t = f + s
  print(t)
  f = s
  s = t
  count += 1
