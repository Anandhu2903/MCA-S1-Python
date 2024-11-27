import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

n = max(a, b, c)
print(f"The biggest number is: {n}")

nn = int(str(n*n))
nnn = int(str(n*n*n))
result = n + nn + nnn
print(f"The result of n + nn + nnn is: {result}")

area = math.pi * n ** 2
perimeter = 2 * math.pi * n
print(f"Area of the circle: {area:}")
print(f"Perimeter of the circle: {perimeter:}")

volume = (4 / 3) * math.pi * n ** 3
print(f"Volume of the sphere: {volume:}")
