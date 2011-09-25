# -*- coding: utf-8 -*-
import cProfile
import math


def is_prime(number):
    if not isinstance(number, int):
        raise ValueError("number should be integer")

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    sqrt = int(math.sqrt(number))
    for x in xrange(3, sqrt + 1):
        if number % x == 0:
            return False

    return True

cProfile.run('is_prime(982451653)')
