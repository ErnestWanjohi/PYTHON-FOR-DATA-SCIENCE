def prime(x):
    if x<0:
        return False
    if x == 2:
        return True
    for n in (2,x):
        if x %n == 0:
            return False
        else:
            return True
def num_prime(n):
    if prime(n):
        yield n


a=int(input("Enter Number\n"))
r=list(num_prime(a))
print(r)
