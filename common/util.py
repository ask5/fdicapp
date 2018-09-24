from random import randint

def random_number(n=10):
    return ''.join(["%s" % randint(0, 9) for num in range(0, n)])
