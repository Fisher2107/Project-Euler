def collatz(x):
    steps=0
    n=x
    while n!=1:
        steps+=1
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
    return(steps)

print(collatz(2))

maxx=1        
for x in range(1,1000000):
    if collatz(x)>maxx:
        maxx=collatz(x)
        bob=x

print(bob)
