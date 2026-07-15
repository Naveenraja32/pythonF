from collections import *
data =defaultdict(int)
str='abba'
for i in str:
    data[i]+=1
print(data)
print(Counter(str))