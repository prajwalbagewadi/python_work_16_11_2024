import collections
import collections as coll
from collections import Counter
list1=[1,1,2,3,4,5]
str="prajwal"
print(collections.Counter(list1))
print(coll.Counter(list1))
print(Counter(list1))
print(Counter(str))
num=[2,2,4,6,6,8,6,10,4]
print(collections.Counter(num).values())
print(collections.Counter(num).keys())