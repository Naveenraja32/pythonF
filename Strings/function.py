# def default(n,a=10):
#     return a,n
# print(default("ram"))

def ptrn(n,p):
 for i in range(1,n+1):
    sp=" "
    if i==1 or i==n:
        return ((sp*len(p))*(n-i) + (p * i).strip())
    else:
        return ((sp*len(p)*(n-i))+ p + (sp*len(p)* (i - 2)) + p.strip())
    
print(ptrn(5,"#   "))