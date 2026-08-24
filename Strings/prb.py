str='2*((4-3)*4)'
stack = []
sy=[]
for i in str:
    if i!=')'and i.isnumeric() or i=='(':
        stack.append(i)
    elif i!=')':
        sy.append(i)
    else:
     
# print(stack)
# print(sy)

# str='2*((4-3)*4)'
# print(f"result is {eval(str)}")