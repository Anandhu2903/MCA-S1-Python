num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
num3=int(input("Enter the third number : "))
if(num1 > num2 and num1> num3):
    print(f"{num1} is larger")
    n = num1
elif(num2 > num3):
    print(f"{num2} is larger")
    n = num2
else:
    print(f"{num3} is larger")
    n = num3
print(n+(n*n)+(n*n*n))
area=3.14*(n*n)
perimeter=2*3.14*n
print(f"Area of the circle : {area}")
print(f"Perimeter of the circle : {perimeter}")
volume=(4/3)*3.14*(n*n*n)
print(f"Volume of the sphere : {volume}")