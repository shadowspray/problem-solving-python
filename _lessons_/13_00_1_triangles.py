# -*- coding: utf-8 -*-
# !/usr/bin/env python


# Give a list A containing at least 3 positive integers in non-descending order
# find the number of triangles that can be constructed using list elements
def triangles(A):
    result = 0
    n = len(A)
    for x in xrange(n):
        z = 0
        for y in xrange(x+1, n):
            while z < n and A[x] + A[y] > A[z]:
                z += 1
            result += z - y - 1
    return result

A1 = [1, 2, 3, 4, 5]
A2 = [2, 2, 5, 6]

for A in [A1, A2]:
    print "=" * 20
    print "List:", A
    result = triangles(A)
    print "Triangles: %s" % (result)
