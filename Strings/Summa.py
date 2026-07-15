# s1="silent" 
# s2 = "listen"
# st1=[0]*26
# st2=[0]*26 
# for i in s1.lower(): 
#     st1[ord(i)-97]+=1

# for i in s2.lower():
#     st2[ord(i)-97]+=1   

# print("The two strings are anagrams" if st1==st2 else "The two strings are not anagrams")

# s1=input("Enter the first string: ")
# st1=[0]*26
# result =""
# for i in s1.lower(): 
#     st1[ord(i)-97]+=1
    
# for i in range(26):
#     if(st1[i]>0):
#         result+=chr(i+97)+str(st1[i])
    
# print(result)
string1=input("Enter the string: ")
result = currentWord = ''
for i in string1+' ':
    if i == ' ':
        result = ' '+currentWord+result
        currentWord = ''
    else:currentWord += i
print(result[1:] if result else '')
 