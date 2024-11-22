# matrix
counter=1
for row in range(1,4):
    for col in range(1,4):
        print(counter,end=" ")
        counter+=1
    print()

# star pattern
for row in range(1,4):
    for col in range(1,row+1):
        print("*",end=" ")
    print()

for row in reversed(range(1,4)):
    for col in range(1,row+1):
        print("*",end=" ")
    print()



basket=["apple","banana","cherry","pineapple"]
for fruit in basket:
    print(fruit)

