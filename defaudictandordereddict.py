from collections import defaultdict
from collections import OrderedDict
tup=(('apple',2),('oranges',3),("oranges",4))
outdict= defaultdict(list)

for key,val in tup:
    outdict[key].append(val)

print(outdict)
#
# print("orderedDict:")
# orddict=OrderedDict(list(tup))
# # print(type(tup))
# for key,val in orddict:
#     print("key",key,"val",val)



