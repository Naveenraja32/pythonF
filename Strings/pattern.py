# s="#"
# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     if(!(i==0 or i==n-1)):
#         print(s,s,sep='  ')
#     else:
#         print(s*n )

# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     print("* "*n)


# n=int(input("Enter the number of rows: "))
# for i in range(n):
#     str=''
#     for j in range(n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             str+="# " 
#         else:
#             str+="  "
#     print(str[:-1])


# n=int(input("Enter the number of rows: "))
# # for i in range(n):
# #     if i==0 or i==n-1:
# #         print(("# "*n).strip())
# #     else:
# #         print("# " + "  " * (n - 2) + "# ")



# n=int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     print(("# " * i).strip())
    
# n=int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     print(" "*(n-i)+ "#" * i)


# n=int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     if(i==1 or i==n):print(("# " * i).strip())
#     else:print("# " + "  " * (i - 2) + "# ")
    
# n=int(input("Enter the number of rows: "))
# for i in range(n, 0, -1):
#     if(i==1 or i==n):print(("# " * i).strip())
#     else:print("# " + "  " * (i - 2) + "# ")

n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    pat="#   "
    sp=" "
    if i==1 or i==n:
        print((sp*len(pat))*(n-i) + (pat * i).strip())
    else:
        print((sp*len(pat)*(n-i))+ pat + (sp*len(pat)* (i - 2)) + pat.strip())
    

# sr="aaaabbaabbabbaa"
# str={}
# for i in sr:
#     if i in str:
#         str[i]+=1
#     else:
#         str[i]=1
# print(str)

# sortedlt = sorted(str,key=lambda x:str[x])
# print(sortedlt)


# dict={"a": 8, "b": 6,"c": 8, "d": 6, "e": 8}
# gdict={}
# for i in dict:
#     if dict[i] in gdict:
#         gdict[dict[i]].append(i)
#     else:
#         gdict[dict[i]]=[i]
# print(gdict)

# rlt = sle = ''
# for i in sortedlt[::-1]:
#     fr = str[i]
#     h= fr//2
#     if fr%2 and not sle:
#         rlt+=i*h
#         sle+=i
#     elif fr>1:
#         rlt+=i*h
# lpm=rlt+sle+rlt[::-1]
# print(lpm)
# print(lpm==lpm[::-1])


# p='abba'
# s='dog cat ct dog'
# w=s.split()
# str={}

# for i in range(len(p)):
#     cw,cm=p[i],w[i]
#     if cw in str and str[cw]!=cm:
#         print(False)
#         quit()
#     str[cw]=cm
# print(True)