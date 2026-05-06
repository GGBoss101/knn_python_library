import math

def euclid_dist(x1, x2):
    dist = 0
    for i in range(len(x1)):
        dist += ((x1[i] - x2[i]) ** 2)
    dist = dist ** (1/2)
    dist = math.dist(x1, x2)
    return dist