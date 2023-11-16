import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def bezier_curve(points, num_samples=100):
    # t = np.linspace(0, 1, num_samples)
    t = np.array([0, 0.15, 0.35, 0.5, 0.7, 0.85, 1])
    n = len(points) - 1
    curve = np.zeros((num_samples, 2))

    for i in range(num_samples):
        for j in range(n + 1):
            curve[i] += points[j] * binomial_coefficient(n, j) * t[i]**j * (1 - t[i])**(n - j)

    return curve


def binomial_coefficient(n, k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))


def visualisation(curve, points):
    x = curve[:, 0]
    y = curve[:, 1]
    points_x = points[:, 0]
    points_y = points[:, 1]

    plt.plot(x, y, 'b-', label='Bezier Curve')
    plt.plot(points[:, 0], points[:, 1], 'ro-', label='Control Points')
    plt.title("Lab №8 GM")

    for i, p in enumerate(points):
        plt.text(p[0], p[1], f'P{i}', ha='right')

    plt.xlim(min(points_x) - 1, max(points_x) + 1)
    plt.ylim(min(points_y) - 1, max(points_y) + 1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()


def main():
    points = np.array([[1, 9], [8, 16], [16, 8], [8, 1], [1, 7], [8, 9]])

    curve = bezier_curve(points, num_samples=7)
    visualisation(curve, points)


main()
