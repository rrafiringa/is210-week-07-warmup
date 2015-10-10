#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Word stats """


from decimal import Decimal


def lexicographics(to_analyze):
    """
    Args:
        to_analyze (string): String to be analyzed
    Returns:
        tuple: Results of analysis
    """
    seq = str(to_analyze).split('\n')

    maxtrk = 0
    mintrk = len(seq)
    wmax = 0
    wmin = 0
    wcnt = []
    for line in seq:
        words = line.split()
        wcur = len(words)
        wmax = max(maxtrk, wcur)
        wmin = min(mintrk, wcur)
        wcnt.append(wcur)
        maxtrk = wmax
        mintrk = wmin
    return (wmax, wmin, Decimal(sum(wcnt))/Decimal(len(wcnt)))

if __name__ == '__main__':
    import data
    print lexicographics(data.SHAKESPEARE)
