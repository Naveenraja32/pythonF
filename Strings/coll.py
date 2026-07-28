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



# str=input("Enter the string: ")
# data=[]
# pairs={')': '(', ']': '[', '}': '{'}
# for i in str:
#     if i in pairs.values():
#         data.append(i)
#     elif data and pairs[i]==data[-1]:
#         data.pop()
#     else:
#         print(False)
#         quit()
# print(True)

# str ="india is my country"
# v=[]
# str1=[]
# j=0
# for i in str:
#     if i in 'aeiou':
#         v.append(i)
# v.reverse() 
    
# for i in str:
#     if i in 'aeiou':
#         str1.append(v[j])
#         j+=1
#     else:
#         str1.append(i)
# print(''.join(str1))        

# n=int(input("Enter the number  "))
# temp=temp1=n1=n
# c=no=0
# while(n!=0):
#     temp=n%10
#     c+=1
#     n=n//10
# print("The number of digits in the number is ",c)
# while(temp1!=0):
#     e=temp1%10
#     no=e**c+no
#     temp1=temp1//10
# result="Armstrong number" if no==n1 else "Not an Armstrong number"
# print(result)



# keys=["qwertyuiop","asdfghjkl","zxcvbnm"]
# words=["Hello","Alaska","Dad","has"]
# rt=[]
# for i in words:
#     base=''
#     wrdslwr=i.lower()
#     for j in wrdslwr:
#         if not base:
#             for k in keys:
#                 if j in k:
#                     base=k
#                     break
#         elif j not in base:break
#     else:rt.append(i)
# print(rt)

# word = 'axz'
# right = left = 0
# for i in word: right += ord(i)-96
# for i in word:
#     value = ord(i)-96
#     left += value
#     right -= value
#     if left==right:print(True);quit()
# print(False)

import os
from os import path
os.makedirs(name='Etho', exist_ok=True)
spath=r'C:\Users\DELL\Documents\pythonF\Strings\coll.py'
print(path.exists(spath))
print(path.basename(spath))
# print(path.expanduser('~/Etho'))creates a folder outside the documents folder
print(path.dirname(spath))  
print(os.getcwd())
print(os.getlogin())
# os.chdir(r'C:\Users\DELL\Documents')
# print(os.getcwd())
# os.removedirs('Etho')
os.startfile("https://www.leetcode.com")
os.startfile(spath)
import os

# Open file1.txt in append mode and write to it
with open('file1.txt', 'a') as f1:
    f1.write(' World')

# Create a hard link named file2.txt pointing to file1.txt
os.link('file1.txt', 'file2.txt')

# Read and print the contents of file2.txt
with open('file2.txt', 'r') as f2:
    print(f2.read())

# Read and print the contents of file1.txt
with open('file1.txt', 'r') as f3:
    print(f3.read())

# Print the number of CPUs on the system
print(os.cpu_count())
