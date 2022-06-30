#!/usr/bin/python3
import hidden_4


def names():
    for a in dir(hidden_4):
        if not (a[0] == '_' and a[1] == '_'):
            print(a)


if __name__ == "__main__":
    names()
