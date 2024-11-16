a=10
b=20
print("a=",a)
print("b=",b)
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)

a=12345678910111213141516171819202122232425262728293031323334353637383940
b=20
print("a=",type(a))
print("b=",b)
a,b=b,a
print("a=",a)
print("b=",b)