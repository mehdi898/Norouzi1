import math
a=1
b=5
c=2
discriminant= b*b - 4.0 *a*c
if discriminant < 0 :
    print("No real roots")
else:
    d=math.sqrt(discriminant)
    print(((-b+d)/2.0))
    print(((-b-d)/2.0))