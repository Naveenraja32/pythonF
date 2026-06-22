s1="silent" 
s2 = "listen"
st1=[0]*26
st2=[0]*26 
for i in s1.lower(): 
    st1[ord(i)-97]+=1

for i in s2.lower():
    st2[ord(i)-97]+=1   

print("The two strings are anagrams" if st1==st2 else "The two strings are not anagrams")
    