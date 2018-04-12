def pi(precision):
    return sum(
            1/(16)**k *
            ((4)/(8*k+1) -
             (2)/(8*k+4) -
             (1)/(8*k+5) -
             (1)/(8*k+6)) for k in range(precision))


def ind_pi(n):
    return sum((1/(16**k*(8*k+n)) for k in range(n)))


def find_hex():
    pass


def decode(start, length):
    pass


for i in range(10):
    print(ind_pi(i))
