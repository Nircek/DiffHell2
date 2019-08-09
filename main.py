#!/usr/bin/env python3

from random import randrange, getrandbits
from gmpy2 import powmod, next_prime


class globals:
    def __init__(self):
        self.p = None
        self.g = None
        self.a = None
        self.A = None
        self.B = None
        self.s = None
        self.m = None
        self.c = None


GLOBALS = globals()


def input_int(msg):
    while True:
        trying = input(msg)
        try:
            return int(trying)
        except ValueError:
            pass
        try:
            return int(trying, 16)
        except ValueError:
            pass


def gen_base(glob=GLOBALS):
    bits = int(input_int('How many bits? '))
    glob.p = next_prime(getrandbits(bits))
    print('p is', hex(glob.p))
    glob.g = gen_g(glob.p)
    print('g is', hex(glob.g))


def gen_g(prime):
    while True:
        testing = randrange(1, prime)
        if powmod(testing, prime//2, prime) != 1:
            return testing


def set_base(glob=GLOBALS):
    glob.p = input_int('Type p: ')
    glob.g = input_int('Type g: ')


MENU = \
    '''
    Type one of these options:
    1) Generate the base (-> p, g)
    2) Set the base (p, g ->)
    3) Calculate public (a -> A)
    4) Calculate common (B -> s)
    q) Quit
    '''

MENU_OPTS = {
    '1': gen_base,
    '2': set_base,
    'q': exit
}


def main(glob=GLOBALS):
    while True:
        settings = ''
        for key in vars(glob).keys():
            if vars(glob)[key] is not None:
                settings += key + ': ' + hex(vars(glob)[key]) + ';\n'
        print(settings, MENU)
        inputting = input()
        if inputting in MENU_OPTS:
            MENU_OPTS[inputting]()


if __name__ == '__main__':
    main()
