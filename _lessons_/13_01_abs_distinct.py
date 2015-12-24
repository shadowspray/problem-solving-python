# -*- coding: utf-8 -*-
# !/usr/bin/env python


# Give a list A containing integers in non-descending order
# find the number of distinct absolute values
# - N is an integer within the range [1..100,000];
# - each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
# - array A is sorted in non-decreasing order.
def solution(A):
    n = len(A)
    if n == 0 or n == 1:
        return n
    i = 0
    j = n - 1
    result = n
    while i <= j:
        # print i, j
        if abs(A[i]) < abs(A[j]):
            j -= 1
            if j < n - 1 and A[j] == A[j+1]:
                result -= 1
        elif abs(A[i]) > abs(A[j]):
            i += 1
            if i > 0 and A[i] == A[i-1]:
                result -= 1
        else:
            if i != j:
                result -= 1
            i += 1
    return result

A1 = []
A2 = [1]
A3 = [-2, 1]
A4 = [0, 0]
A5 = [1, 1, 1]
A6 = [-1, -1, 1, 1, 1]
A7 = [-2, -1, 0, 1, 2, 4]
A8 = [-3, -3, -2, -2, -2, -1]
A9 = [0, 1, 2]
A10 = [-5, -4, -4, -3, -2, -2, -2, 0, 1, 3, 3]

for A in (A1, A2, A3, A4, A5, A6, A7, A8, A9, A10):
    print "=" * 20
    print "List:", A
    result = solution(A)
    print "AbsDistinct: %s" % (result)
