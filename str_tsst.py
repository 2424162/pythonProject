str2 = "qwerty"
str1 = list(str2)
print(len(str1))
for i in range(0,int(len(str1)/2)):
    print(i)
    str1[i],str1[len(str1)-1-i]=str1[len(str1)-1-i],str1[i]

print(str1)
print("".join(str1))