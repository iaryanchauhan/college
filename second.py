# write a program in python to find the largest among three numbers enterd by the user.
a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))
if(a>b and a>c):
    print(f"{a} is the greatest number")
elif (b>a):
        print(f"{b} is greatest number")
else:
            print(f"{c} is greatest number")