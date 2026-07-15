s=[1,2,3,4]
print(list(filter(lambda x:x%2,s)))
print([x for x in s if x%2])
print(list(map(lambda x:x**2,s)))
print([x**2 for x in s])
print(any(x%2 for x in [2,5,6]))
print(any(x%2 for x in [1,3,5]))

twod=[[1,2,3],[4,5,6],[7,8,9]]
print(list(zip(*twod)))