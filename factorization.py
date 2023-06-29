#!/usr/bin/python3
from sys import stderr, stdout, argv
from math import isqrt


def factorization(n):
    """A function that finds the lowest divisor of a number

    Arg:
      n: The number

    Return:
       The lowest divisor
    """
    if n <= 3:
        return 1
    elif n % 2 == 0 or n % 3 == 0:
        return 2 if n % 2 == 0 else 3

    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return i if n % i == 0 else (i + 2)


def process_file(filename):
    """A function that process the file provided

    Arg:
      filename: The file provided

    Return:
       print the required output
    """
    with open(filename, "r") as file:
        for line in file:
            no = int(line.strip())
            low_div = factorization(no)
            print("{} = {} * {}".format(no, int(no/low_div), low_div))


if len(argv) < 2:
    print("Usage: factor <file>", file=stderr)
else:
    filename = argv[1]
    process_file(filename)
