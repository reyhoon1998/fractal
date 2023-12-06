import numpy as np
import matplotlib.pyplot as plt
import random


def f1(r):
    alpha = 1 / 2
    b = alpha * r
    return b


def f2(r):
    alpha = 1 / 2
    a = np.array([[1 / 2], [0]])
    b = alpha * r + a
    return b


def f3(r):
    alpha = 1 / 2
    a = np.array([[1 / 4], [np.sqrt(3) / 4]])
    b = alpha * r + a
    return b


F = [f1, f2, f3]

N = 100000
n = 1000
points = np.zeros((n, n))

for j in range(N):
    r = np.array([[random.random()], [random.random()]])
    for i in range(20):
        R = random.randint(0, 2)
        r = F[R](r)
    x, y = int(r[0] * n), int(r[1] * n)
    points[y, x] = 1

plt.imshow(points[::-1, :])
plt.show()