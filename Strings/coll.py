from collections import *


# data =defaultdict(int)
# str='abba'
# for i in str:
#     data[i]+=1
# print(data)
# print(Counter(str))

# a={"theme":"dark","font_size":12,"language":"en"}
# b={"theme":"light"}
# c=ChainMap(a,b)
# print(c)  # Output: dark

# data=OrderedDict([('b',2),('c',3)])
# data.setdefault('a',5)
# print(data)
# data.move_to_end('b')
# print(data)
# data.popitem(last=False)
# print(data)

# data=deque([5,1,3,2])
# data.rotate(2)
# print(data)
# data.appendleft(4)
# print(data)
# data.extendleft([6,7])
# print(data)
# print(data.pop())
# print(data.popleft())
# data.extend([8,9])
# print(data)


str="[{()}]"
data=[]
for i in str:
    if i in ['(','[','{']:
        data.append(i)
    else:
        if len(data)==0:
            print("Not Balanced")
            break
        else:
            x=data.pop()
            if x=='(' and i==')':
                continue
            elif x=='[' and i==']':
                continue
            elif x=='{' and i=='}':
                continue
            else:
                print("Not Balanced")
                break
else:
    print("Balanced")