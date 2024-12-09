#WAP to solve quadratic eqation
import math
b= int(input("enter b:"))
a= int(input("enter a:"))
c= int(input("enter c:"))

d= (b*b-(a*c*4))
if d>0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Roots are real and distinct: {root1}, {root2}")
elif d==0:
    root= -b/(2*a)
    print(f"root:{root} ")

else:
    real = -b/(2*a)
    imaginary= math.sqrt(-d)/(2*a)
    print(f"The roots of the quadratic equation are:")
    print(f"{real} + {imaginary}i")
    print(f"{real} - {imaginary}i")


