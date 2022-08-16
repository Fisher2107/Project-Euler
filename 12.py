def tri(i):
    k=0
    for j in range(i+1):
        k+=j
    return k


iteration=1
factors=[]
while len(factors)<=500:
    iteration+=1
    factors=[]
    for i in range(1,tri(iteration)+1):
        if tri(iteration)%i==0:
            factors.append(i)
print(factors)
print(tri(iteration),iteration)
    
