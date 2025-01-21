# a = int(input("Enter the number : "))

b = map( int,input("Enter the number : ").split())

print(b)

for i in b :
    print("Index : ",i , ":", i % 16)

