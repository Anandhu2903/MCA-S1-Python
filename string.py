str1 = input("enter a string")
print("string created")
str2 = input("enter a string to concatenate")
str3 = str1+" "+str2
print("the concatenate string is",str3)
pos=int(input("enter the number of word position:"))
sub_string=str3[pos+1:]
print("substring:",sub_string)