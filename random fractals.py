import numpy as np
import matplotlib.pyplot as plt
import random


def f1(r):
    R = np.array([[0, 0], [0, 0.16]])
    b = np.dot(R, r)
    return b


def f2(r):
    R = np.array([[0.85, 0.04], [-0.04, 0.85]])
    a = np.array([[0], [1.6]])
    b = np.dot(R, r) + a
    return b


def f3(r):
    R = np.array([[0.2, -0.26], [0.23, 0.22]])
    a = np.array([[0], [1.6]])
    b = np.dot(R, r) + a
    return b


def f4(r):
    R = np.array([[-0.15, 0.28], [0.26, 0.24]])
    a = np.array([[0], [0.44]])
    b = np.dot(R, r) + a
    return b


F = [f1, f2, f3, f4]

N = 100000
n = 1000
points = np.zeros((n, n))

for j in range(N):
    r = np.array([[random.random()], [random.random()]])
    for i in range(20):
        R = np.random.choice([0, 1, 2, 3],
                             p=[0.01, 0.85, 0.07, 0.07])
        r = F[R](r)
    x, y = int(r[0] * n / 10 + n / 2), int(r[
                                               1] * n / 10)
    points[y, x] = 1

plt.imshow(points[::-1, :])
plt.show()
