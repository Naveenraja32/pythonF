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


# string1=input("Enter the string: ")
# result = currentWord = ''
# for i in string1+' ':
#     if i == ' ':
#         result = ' '+currentWord+result
#         currentWord = ''
#     else:currentWord += i
# print(result[1:] if result else '')
 
 
# Form words in diagonal flow
# words = ['car','can','dad']
# largest = None
# for i in words:
#     currentLength = len(i)
#     if largest==None or currentLength>largest:largest=currentLength
# words = [x+' '*(largest-len(x)) for x in words]
# result = []
# index = reverse = 1
# for i in words:
#     if not result:result = list(i)
#     else:
#         for x in range(largest-1):
#             if reverse:result[index+x] = i[x]+result[index+x]
#             else:result[index+x] += i[x]
#             reverse = not reverse
#         if largest%2:reverse = not reverse
#         result.append(i[-1])
#         index += 1

# print(result)

#zigzag conversion

# str = "PAYPALISHIRING"
# numRows = 3
# stream =['']*numRows
# index=rev=0
# for x in str:
#     stream[index]+=x
#     if index==0:rev=0
#     elif index==numRows-1:rev=1
#     index+= -1 if rev else 1
# print(''.join(stream))

#pyramid
def pyramid(n):
    s="  "
    for i in range(0, n):
        if i == 0 or i == n-1:
            print(s * (n - i) + '* ' * ((i*2) + 1))
        else:
            print(s * (n     - i) + '* ' + '  ' * ((i*2) - 1) + '* ')
pyramid(int(input("Enter the number of rows: ")))