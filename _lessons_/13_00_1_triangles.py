# -*- coding: utf-8 -*-
# !/usr/bin/env python


# Give a list A containing at least 3 positive integers in non-descending order
# find the number of triangles that can be constructed using list elements
def triangles(A):
    results = []
    n = len(A)
    for x in xrange(n):
        for y in xrange(x+1, n):
            z = y + 1
            while z < n and A[x] + A[y] > A[z]:
                results.append([A[x], A[y], A[z]])
                z += 1
    return results


A1 = [1, 2, 3, 4, 5]
A2 = [2, 2, 5, 6]

A = A1
results = triangles(A)
print "List: %s\nTriangles (%s): %s" % (A, len(results), results)

A = A2
results = triangles(A)
print "List: %s\nTriangles (%s): %s" % (A, len(results), results)
