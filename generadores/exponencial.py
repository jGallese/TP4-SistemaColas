import math
import random


def exponencial(lmbd):
    rnd = random.random()
    n = -1 / lmbd * math.log(1 - rnd)
    return n
