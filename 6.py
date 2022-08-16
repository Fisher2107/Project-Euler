a=[]
b=[]

for i in range(1,101):
    a.append(i**2)

for i in range(1,101):
    b.append(i)

print(a) 
print(sum(a))

print((sum(b)**2)-sum(a))
