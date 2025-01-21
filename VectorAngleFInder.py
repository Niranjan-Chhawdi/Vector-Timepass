from math import *

u = map( int,input("Enter the First List : ").split())

v = map( int,input("Enter the Second List : ").split())


u6 = []
v4 = []

for i in u :
    u6.append(i)

for i in v :
    v4.append(i)

print( "u" , u6)
print("v" , v4)

l = []

for i in range(len(u6)):
    a = u6[i] * v4[i]
    l.append(a)


print(l)

print("Dot Product : " , sum(l))

#Magnitude

mu = []
mv = []

for i in range(len(u6)) :
    mu.append(u6[i]**2)
    mv.append(v4[i]**2)

print(mu)
print(mv)


MU = sqrt(sum(mu))
MV = sqrt(sum(mv))

print(MU * MV)

FF =  sum(l)/(MU * MV)

print("Final Angle : " , degrees(acos(FF)))
