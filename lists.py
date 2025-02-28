from os import remove

#defining a list
li = [1,2,4.5,"abc"]
print(f"li={li}")

li1 = list(range(1,10+1))
print(f"li1={li1}")

#adding elements in list
li1.append("jdm");
print(f"li1={li1}")

li1.insert(4,"jdm1")
print(f"li1={li1}")

# deleting list items
li1.insert(5,"jdm1")
print(f"li1={li1}")
li1.remove("jdm1")
print(f"li1={li1}")

li1.pop()
print(f"li1={li1}")
li1.pop(-2)
print(f"li1={li1}")

#appending a new list to old list
li2 = [100,200,300]
li1.extend(li2)
print(f"li1={li1}")

#list countings
print(f"li1 count={li1.count("jdm1")}")
print(f"li1 len={len(li1)}")

#index
print(f"li1 5={li1.index(5)}")

#sort 
unsrt=[5,4,3,2,1]
unsrt.sort()
print(f"unsrt ={unsrt}")

#reverse
re=["a","b","c"]
re.reverse()
print(f"re={re}")

#copy
a=[1,2,4]
b=[]
b=a.copy()
print(f"b={b}")
