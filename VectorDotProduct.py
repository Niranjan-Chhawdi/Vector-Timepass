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

print(sum(l))