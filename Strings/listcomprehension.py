# normal way of creating a list
# s=[]
# for i in range(1,11):
#     s.append(i**2) 
# print(s)

# list comprehension
# print([i**2 for i in range(1,11)])

# dictionary comprehension
# print({x:chr(x+97) for x in range(26)}) 

# set comprehension
# print({x for x in'abbccdce'})

# generator comprehension
# stream=(x**2 for x in range(1,11))
# for i in stream:
#     print(i)

# print(['odd' if i%2!=0 else 'even' for i in range(1,11)])

# print([x for x in range(1,101) if x%2 ])

# d = {} for i in range(26): d[chr(97 + i)] = i + 1 print(d)

def sample(x):
    if x==1:return 'One'
    elif x==2:return 'Two'
    else:return 'Three'
print([sample(x) for x in range(1,4)])
