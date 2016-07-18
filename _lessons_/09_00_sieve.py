# -*- coding: utf-8 -*-


def sieve(n):
    results = [True] * (n + 1)
    results[0] = results[1] = False
    i = 2
    while i * i <= n:
        print 'base:', i
        if results[i]:
            k = i * i
            while k <= n:
                print 'remove:', k
                results[k] = False
                k += i
        i += 1
    return results


if __name__ == '__main__':
    n = 19
    results = sieve(n)
    print '-' * 80
    for i, result in enumerate(results):
        print '%s is prime: %s' % (i, result)
