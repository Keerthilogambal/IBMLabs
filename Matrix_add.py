n=int(input("enter row"))
m=int(input("enter column"))
a=[]
b=[]
c=[]
for i in range(n):
    for j in range(n):
        x = int(input("enter elements"))
        a.append(x)
    b.append(a)
    a=[]


for i in range(n):
    for j in range(n):
        x = int(input("enter elements"))
        a.append(x)
    c.append(a)
    a=[]

for i in range(n):
    for j in range(m):
        print(b[i][j] + c[i][j])