#WAP to swap two variable without using temp variable
a=int(input("enter a:"))
b=int(input("enter b:"))
a=a+b
b=a-b
a=a-b
print(f"value of a is {a} and b is {b}")