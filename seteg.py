s={4,4,3,2,1}
print("s=",s)
s1={"user1","user1",123,1+2j}
print("type s1=",type(s1))
print("s1=",s1)
#s1[0]="user2" # trying to update val at index 0
print(s1)

s1={1,2,3}
s2={3,4,5}
print("union=",s1|s2)
print("union=",s1.union(s2))
print("intersection=",s1&s2)
print("intersection=",s1.intersection(s2))

s3={"apple","banana","cherry"}
print("s3=",s3)