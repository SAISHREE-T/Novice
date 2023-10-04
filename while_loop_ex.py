#Accepting numbers till the user enters 0 and displaying the max and the min
max=0
min=0
n=None
while n!=0:
    n=int(input("Enter a number: "))
    if n>max and n!=0:
        max=n
    if n<min  and n!=0:
        min=n

print(f"The max value is:{max}\n The min value is:{min}")

#Extraction of digits using while loop
n=int(input("Enter the number: "))
t=n
cnt=0
rev=0
while t>0:
    d=t%10
    print(f" {d}")
    t=t//10
    cnt=cnt+1
    rev=rev*10+d
print(cnt)
if rev==n:
    print("The given number is a palindrome")


#To find the places of the even and odd numbers
n=int(input("Enter the number: "))
even=[]
odd=[]
t=n
cnt=0
while t>0:
    d=t%10
    t=t//10
    cnt=cnt+1
    if d%2==0:
        print(f"There is an even number in the {10**(cnt-1)}s place")
        even.append(d)
    elif d%2==1:
        print(f"There is an odd number in the {10**(cnt-1)}s place")
        odd.append(d)
print(*even)
print(*odd)
