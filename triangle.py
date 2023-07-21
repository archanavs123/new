a=int(input("Enter The right side of triangle :"))
b=int(input("Enter The right side of triangle :"))
c=int(input("Enter The right side of triangle :"))
if a==b or a==c or b==c:
    print("the triangle is isosceles")
elif a==b==c:
    print("the triangle is  equilateral")
else:
    print("the triangle is not equilateral and not isosceles")    