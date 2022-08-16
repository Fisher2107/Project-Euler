
a=[2]
b=3
c=0
while len(a)<=10000:
    for i in range(len(a)):
        if b%a[i]!=0:
            c+=1
    if c==len(a):
        a.append(b)
    b+=1
    c=0

print(a[-1])
