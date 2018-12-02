from math import *
print ("vvedite vse koeff")
a,b,c=list(map(float, input().split()))
discr=b*b-4*a*c
if discr<0:
    print("korni potracheni")
elif discr==0:
    x=-b/(2*a)
    print("odin koren",x)
else:
    x1=(-b+sqrt(discr)/(2*a))
    print("odin koren",x1)
    x2=(-b-sqrt(discr)/(2*a))
    print("vtoroy koren",x2)
