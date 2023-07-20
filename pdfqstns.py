
#1.equal or not
#------------
"""a=int(input("Enter First Number : " ))
b=int(input("Enter Second Number :" ))
if a==b:
    print(a, "and" ,b,"are equal")
else :
    print(a, "and" ,b,"are not equal")   """
     
#2.casting your vote
#-----------------------
"""
a=int(input("Enter The Age : "))
if a==21:
 print(" congratulations!! you are eligible for casting your vote")
else:
  print(" sorry (^_^) you are not eligible for casting your vote")"""
#3.largest among three
#--------------------------
"""
x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
z=int(input("Enter Third Number:"))
if x>y and x>z:
    print(x,"is the largest number") 
elif y>x and y>z:
     print(y,"is the largest number")
else :
     print(z,"is the largest number") """

#4.eligible for admission
#----------------------------

mm=int(input("Enter The marks obtained in mathmatics : "))
che=int(input("Enter The marks obtained in chemistry : "))
phy=int(input("Enter The marks obtained in physics : "))
total=int(input("Enter The total marks obtained : "))
mp=int(input("Enter The total marks obtained in maths and physics: "))
if mm>=65:
    print("candidate is eligible for admission")
elif phy>=55:    
    print("candidate is eligible for admission ") 
elif che>=50:
     print("candidate is eligible for admission")
elif total>=190:   
     print("candidate is eligible for admission")
elif mp>=140:
     print("candidate is eligible for admission")
else :
          print("candidate is not eligible for admission")