# write a program in python to find the largest among three numbers enterd by the user.
a=int(input("enter number:"))
b=int(input("enter number:"))
print(f"before swapping num1={a} and num2={b}".format(a,b))

c=a
a=b
b=c
print(f"after swapping num1={a} and num2={b}".format(a,b))
