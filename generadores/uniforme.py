import random


def uniforme(a, b):
    rnd = random.random()
    n = a + (b - a) * rnd
    return n