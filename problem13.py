#!/usr/local/env python

def main():
    with open('problem13-data') as f:
        numbers = f.readlines()
        print (brute_force(numbers))
        print (smarter(numbers))

def smarter(numbers):
    y = 0
    # only the first 11 digits of the numbers are needed
    for x in numbers:
        x = x[:11]
        y = y + int(x)
    return str(y)[:10]

def brute_force(numbers):
    y = 0
    for x in numbers:
        y = y + int(x)
    return str(y)[:10]


if __name__ == '__main__':
    main()
