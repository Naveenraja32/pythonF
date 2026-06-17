n=int(input("Enter a Number:"))
for i in range(n,1,-1):
    print(*range(1,i),sep="*")
    
