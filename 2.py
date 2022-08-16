a=(1,2)

for i in range(100):
    a=a+(a[i]+a[i+1],)
    if a[i+2]>4000000:
        break

print(a)

n=len(a)
print(n)

b=0

type[a[2]]

for i in range(n):
     if a[i]%2 == 0:
        b=b+a[i]

print(b)

# note code can be improved by removing the number at the end of the list
# since it is over 4m. But since it is odd it doesnt matter hence i skipped
