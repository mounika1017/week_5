n=int(input("enter a number"))
def prime_rec(n,i=2):
    if n <= 1 or n % i == 0:
     return False
    if i * i > n:
        return True
    return prime_rec(n, i + 1)
if prime_rec(n)==True:
    print(n,"is a prime num")
else:
    print(n,"is not a prime num")