n=int(input("enter a number"))
def prime(n):
        if n<=1:
            return False
        for i in range(2,n):
             if n%i==0:
                return False
        return True
if prime(n)==True:
    print(n,"is a prime num")
else:
    print(n,"is not a prime num")
