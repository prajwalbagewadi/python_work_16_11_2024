counter=1 # initilazation
t=int(input("Enter table for:"))
n=int(input("Print table values till:"))
while(counter<=n): # condition check
    print(t,"*",counter,"=",t*counter)
    counter=counter+1 # increament