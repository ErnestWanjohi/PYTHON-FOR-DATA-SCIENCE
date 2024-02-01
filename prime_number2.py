def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n ==0:
            return False
    return True
#test data
#print (isPrime(3))

#inn a range of values
def primeGenerator(a, b):
    for z in range(a, b):

        if isPrime(z):
            yield z
    


f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))
