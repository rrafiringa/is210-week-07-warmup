#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Truthiness evaluations """


def bool_to_str(bval):
    """
    Args:
        bval(mixed): A truthy of falsy value
    Returns
        string: 'Yes' if truthy, 'No' if Falsy
    """
    ret = 'No'
    if bval:
        ret = 'Yes'
    return ret

if __name__ == '__main__':
    print bool_to_str('')
    print bool_to_str('test')
    print bool_to_str(0)
    print bool_to_str(1)
    print bool_to_str([])
    print bool_to_str([0])
