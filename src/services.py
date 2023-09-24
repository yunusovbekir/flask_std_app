import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize


def piecewise_function(x: float, a: float, b: float, c: float) -> float:
    """
    Piecewise (F) function:
    F(x) = a if x < c
    F(x) = b if x >= c
    """
    return a if x < c else b


def objective(initial: tuple[float, float, float], array: list[tuple[float, float]]) -> float:
    a, b, c = initial
    deviations = []
    for x, y in array:
        if x < c:
            deviations.append((a - y) ** 2)
        else:
            deviations.append((b - y) ** 2)
    return np.sqrt(np.mean(deviations))


def calculate_standard_deviation(array: list[tuple[float, float]]) -> tuple[float, float, float]:
    """
    Optimize using Nelder-Mead method.

    This function utilizes the Nelder-Mead optimization method to find the minimum
    of an objective function. The optimization starts from an initial guess of [0, 0, 0].

    :param array: list of (x,y) pairs
    :return: a,b,c values
    """
    result = minimize(objective, [0, 0, 0], args=(array,), method='Nelder-Mead')
    return result.x


def visualize(array: list[tuple[float, float]], params: tuple[float, float, float]) -> str:
    """
    Function to visualize the given array of (x,y) pairs and the (a, b, c) tuple
    :param array: list of (x,y) pairs
    :param params: a,b,c values
    :return: image name in string format
    """
    x_values, y_values = zip(*array)
    a_opt, b_opt, c_opt = params

    plt.scatter(x_values, y_values, label='(x, y) pairs')
    plt.plot(np.array([a_opt, b_opt, c_opt]), '-or' )

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    path = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(path, 'static/result.png')
    plt.savefig(image_path)
    return "result.png"
