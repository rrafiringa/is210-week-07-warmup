#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Fibonacci sequence using while loop """


def fibonacci(maxint):
    """
    Args:
        maxint (int): Upper limit of fibonacci sequence
    Returns:
        list: Fibonacci sequence
    Examples:
        print task_01.fibonacci(10)
    """
    seq = []
    idx = 0
    cur = 0
    prv = 0
    while cur < maxint:
        print 'Loop: ' + str(idx+1)
        if idx <= 1:
            cur = idx
            seq.append(cur)
        else:
            print 'seq[-2] => ' + str(seq[-2])
            print 'seq[-1] => ' + str(seq[-1])
            prv = seq[-1]
            cur = seq[-2] + seq[-1]
            seq.append(cur)
        cur = prv + seq[-1]
        print '------------------'
        idx += 1
    return seq

if __name__ == '__main__':
    print fibonacci(530000)