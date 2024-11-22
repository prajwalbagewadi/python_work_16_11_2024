"""
#if
passwd=input("Enter the Passwd:")
if(passwd=="admin@123"):
    print("correct passwd")

#if,else
if(passwd=="admin@123"):
    print("correct passwd")
else:
    print("incorrect passwd")


#elif
# a+ 80 - 100
# a 70 - 80
# b  50 - 70
# c  35 - 50
# d    <35
marks=int(input("Enter the marks out of 100:"))
if(marks>80 and marks<=100):
    print("Grade A+")
elif(marks>70 and marks<=80):
    print("Grade A")
elif(marks>50 and marks<=70):
    print("Grade B")
elif(marks>35 and marks<=50):
    print("Grade C")
elif(marks<35):
    print("Grade D")
else:
    print("invalid marks")
"""
"""

prod=list(input("Enter product name:"))
print(type(prod))
print(prod[0])
"""
prod=["nothingphone1","charger","Tempered Glass"]
if(prod[0]=="nothingphone1"):
    print(" price=",26770)
    if(prod[0]=="nothingphone1"and prod[1]=="charger"):
        print("price=",26770+491)
        if(prod[0]=="nothing phone 1" and prod[1]=="charger" and prod[2]=="Tempered Glass"):
            print("price=",26770+491+299)
        else:
            print("buy tempered glass and charger 600")
    else:
        print("buy charger at 399")
else:
    print("product unavailable.")


petrol="full"
key="0"
if(petrol=="full"):
    if(key=="1"):
        print("motorcycle started")
    else:
        print("bring key")
else:
    print("cannot start")