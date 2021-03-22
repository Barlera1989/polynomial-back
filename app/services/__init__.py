import numpy as np
from scipy import optimize
from app.models import *
import plotly.express as px
import math


def optimize_data(polynomial_object):

    polynomial = polynomial_object.polynomial_degrees
    convert_to_polynomial = np.poly1d(polynomial)

    def f(x):
        return convert_to_polynomial(x) + polynomial_object.k_value*math.cos(x)

    optimized_data = optimize.newton(
        f,
        x0=polynomial_object.initial_value,
        tol=polynomial_object.tolerance,
        maxiter=polynomial_object.max_iterations)

    return optimized_data


def display_result(polynomial_object):

    x = np.array(range((polynomial_object.initial_value-50),
                 (polynomial_object.initial_value + 50)))

    polynomial = polynomial_object.polynomial_degrees
    convert_to_polynomial = np.poly1d(polynomial)

    y = convert_to_polynomial(x) + polynomial_object.k_value*np.cos(x)

    fig = px.line(x=x, y=y)

    fig.show()
