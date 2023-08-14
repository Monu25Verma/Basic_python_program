#prime number
def find_prime(x):

    if x % 2 == 0 or x == 1:
        print(x, "is a not prime number")
    else:
        print(x, "is a prime number")


find_prime(13)