# -*- coding: utf-8 -*-
# !/usr/bin/env python


# Find if any sub-list of list A (element > 0) has the expected sum s
def caterpillar(A, s):
    n = len(A)
    front, total = 0, 0
    for back in xrange(n):
        while front < n and total + A[front] <= s:
            total += A[front]
            front += 1
        if total == s:
            return A[back:front]
        total -= A[back]
    return False

A = [6, 2, 7, 4, 1, 3, 6]
s1 = 12
s2 = 16

print "List:", A
print "Sub-list with specified sum (%s):" % s1, caterpillar(A, s1)
print "Sub-list with specified sum (%s):" % s2, caterpillar(A, s2)
