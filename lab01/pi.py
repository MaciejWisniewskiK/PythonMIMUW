import math
import random

def pi(points):
    inside = 0
    for _ in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if (x**2 + y**2) <= 1:
            inside += 1
    return 4 * inside / points

def delta(estimation):
    return math.pi - estimation

if __name__ == '__main__':
    n, k = [int(x) for x in input().split()]
    for i in range(k, n + 1, k):
        estimation = pi(i)
        print(i, estimation, delta(estimation))