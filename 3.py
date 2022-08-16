x=600851475143
y=[]


for i in range(2,x):
    if x%i==0:
        y.append(i)
        x=x//i
        break
print(x)
for i in range(2,x):
    if x%i==0:
        y.append(i)
        x=x//i
        break
print(x)
for i in range(2,x):
    if x%i==0:
        y.append(i)
        x=x//i
        break
print(x)
print(y)
