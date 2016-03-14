# -*- coding: utf-8 -*-
# !/usr/bin/env python


def solution(N, A):
    M = len(A)
    counters = [0] * N
    current_max = 0
    last_max = 0
    for i in xrange(M):
        a = A[i]
        print 'Operation Index: %2s, on %2s' % (i, a)
        if a == N + 1:
            print 'Max counter operation, current max: %s' % current_max
            last_max = current_max
        elif 1 <= a <= N:
            if counters[a - 1] >= last_max:
                counters[a - 1] += 1
                print 'Increment counter %s, current max: %s' % (a, current_max)
            else:
                counters[a - 1] = last_max + 1
            if counters[a - 1] > current_max:
                current_max = counters[a - 1]
        print 'After operation, current max: %2s, last_max: %2s' % (current_max, last_max)
        print 'Current counters: %s\n' % [str(i) + ':' + str(v) for i, v in enumerate(counters)]

    for i in xrange(N):
        if counters[i] < last_max:
            counters[i] = last_max

    return counters

N = 20
A = [21, 7, 14, 21, 14, 21, 18, 5, 5, 21, 14, 7, 6, 21, 6, 14, 18, 15, 4, 10, 19, 5, 10, 10, 12, 10, 17, 4, 16, 21]
print solution(N, A)
