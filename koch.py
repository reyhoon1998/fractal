import matplotlib.pyplot as plt
import numpy as np


def cal(x, y):
    x_new = np.zeros(5)
    y_new = np.zeros(5)
    x_new[0] = x[0]
    y_new[0] = y[0]
    x_new[1] = x[0] + (x[1] - x[0]) / 3
    x_new[2] = x_new[1] + 1 / 3 * (
            (x[1] - x[0]) / 2 - np.sqrt(3) * (y[1] - y[0]) / 2)
    x_new[3] = x[0] + 2 / 3 * (x[1] - x[0])
    y_new[1] = y[0] + (y[1] - y[0]) / 3
    y_new[2] = y_new[1] + 1 / 3 * (
            (y[1] - y[0]) / 2 + np.sqrt(3) * (x[1] - x[0]) / 2)
    y_new[3] = y[0] + 2 * (y[1] - y[0]) / 3
    x_new[4] = x[1]
    y_new[4] = y[1]
    return x_new, y_new


def koch(x, y, n):
    if n == 0:
        plt.plot(x, y)
    else:
        x1_new, y1_new = cal(x, y)
        koch([x1_new[0], x1_new[1]], [y1_new[0], y1_new[1]], n - 1)
        print(x1_new, y1_new)
        koch([x1_new[1], x1_new[2]], [y1_new[1], y1_new[2]], n - 1)
        print(x1_new, y1_new)
        koch([x1_new[2], x1_new[3]], [y1_new[2], y1_new[3]], n - 1)
        print(x1_new, y1_new)
        koch([x1_new[3], x1_new[4]], [y1_new[3], y1_new[4]], n - 1)
        print(x1_new, y1_new)


x = [0, 1]
y = [0, 0]

koch(x, y, 2)
plt.show()
