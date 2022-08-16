nums=[]
bums=[]
primes=[]
for i in range(2,2000001):
    nums.append(i)

while len(nums)!=0:
    primes.append(nums[0])
    for i in nums:
        if i%nums[0]!=0:
            bums.append(i)
    nums=bums
    bums=[]

print(bums)
print(sum(primes))
    
    
