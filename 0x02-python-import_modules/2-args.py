#!/usr/bin/python3
from sys import argv


def numList():
    print('{} argument'.format(len(argv) - 1), end='')
    if len(argv) == 1:
        print('s.')
    elif len(argv) == 2:
        print(':')
    else:
        print('s:')
    for a in range(1, len(argv)):
        print('{}: {}'.format(a, argv[a]))


if __name__ == "__main__":
    numList()
