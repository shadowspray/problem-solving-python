# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
"""


def solution(S):
    # write your code in Python 2.7
    stack = []
    left = '([{'
    right = ')]}'
    for c in S:
        if c in left:
            stack.append(c)
        elif c in right:
            if len(stack) == 0:
                return 0
            p = stack.pop()
            if right.index(c) != left.index(p):
                return 0
    if len(stack) != 0:
        return 0
    return 1
