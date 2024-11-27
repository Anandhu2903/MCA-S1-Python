color=input("ENTER COLORS SEPARATED NY COMMAS:")
color_list1=color.split(',')
print(color_list1)
print("FIRST COLOR:", color_list1[0])
print("LAST COLOR:", color_list1[-1])
color_list2=["Red","Orange","Black","White"]
print("color_list1 not contained in color_list2 are:")
diff=list(set(color_list1)-set(color_list2))
print(diff)
color_int_list=[]
for color in color_list1:
    color_int_list.append(len(color))

print(f":List of integers  corresponding to each color: {color_int_list}")
