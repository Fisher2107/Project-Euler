# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

palnum = []

def pal(x):
    if len(str(x)) == 6:
        if list(str(x))[0] == list(str(x))[5] and list(str(x))[1] == list(str(x))[4] and list(str(x))[2] == list(str(x))[3]:
            palnum.append(x)
    else:
        if list(str(x))[0] == list(str(x))[4] and list(str(x))[1] == list(str(x))[3]:
            palnum.append(x)


for i in range(100,1000):
    for j in range(i,1000):
        pal(i*j)
        
palnum.sort()

print(palnum[-1])


        
    
