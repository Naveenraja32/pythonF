# f = int(input("enter a Start value: "))
# if (f%2==0):
#     s=f
# else:
#     s=f+1
# e = int(input("enter a end value: "))
# print(*range(s, e+1, 2))

# print(*range(2,12,2))

n=int(input("Enter Limit: "))
a=[0]*n
b=[]
for i in range (n):
    a[i]=int(input())
print(a)
for i in a:
    if i%2==0 and i not in b:
        b.append(i)
print(b)