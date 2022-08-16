def tri(i):
    return (i*(i+1))/2


from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


i=1
f={}

while len(f)<=500:
   i+=1
   f=factors(tri(i))

print(tri(i),i)
    
