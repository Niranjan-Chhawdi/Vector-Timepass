u = map( int,input("Enter the First List : ").split())

v = map( int,input("Enter the Second List : ").split())

# w = 6 * u - 4 * v

u6 = []
v4 = []

for i in u :
    u6.append(4 * i)

for i in v :
    vv = 7 * (i)
    v4.append(vv)

print( "u" , u6)
print("v" , v4)

l = []

for i in range(len(u6)):
    a = u6[i] + v4[i]
    l.append(a)


print(l)