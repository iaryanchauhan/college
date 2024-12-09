y=int(input("Enter Year::"))
if(y%400==0):
    print ("it is a leap year")
elif(y%4==0 and y%100!=0):
    print ("it is a leap year")
else:
    print("not a leap year")

