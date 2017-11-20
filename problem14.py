#!/usr/local/env python

def main():
    longest_chain = 0
    leader = 2
    for i in range(2,1000001):
        chain_length = collatz(i)
        if chain_length > longest_chain:
            longest_chain = chain_length
            leader = i
            print('New Leader! ' + str(i))
            print('Chain Length: ' + str(longest_chain))

    print ('Finished')
    print (leader,longest_chain)

def collatz(start):
    chain = 1
    next_num = start
    while next_num != 1:
        if (next_num % 2 == 0):
            next_num = next_num / 2
            chain = chain + 1
        else:
            next_num = (next_num * 3) + 1
            chain = chain + 1
    return chain

if __name__ == '__main__':
    main()
