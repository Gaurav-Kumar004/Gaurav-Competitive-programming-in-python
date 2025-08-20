a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the Third number")) 

if a<b and a<c:
    minimum = a
elif b<a and b<c:
    minimum = b
else:
    minimum = c
print("minimum number is:", minimum)