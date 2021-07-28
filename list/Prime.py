def ChkPrime(num):
    if(int(num) <= 1):
        return False

    for i in range(2, int(num)):
        if(int(num) % i == 0):
            return False

    return True
