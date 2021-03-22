import numpy as np
from scipy import optimize
from app.models import *
import plotly.express as px
import math
import os
import datetime


SERVICES_FILEPATH = os.path.dirname(os.path.abspath(__file__))
APP_ROOT = os.path.dirname(SERVICES_FILEPATH)


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

    RANDOM_NUMBER_PATH = datetime.datetime.now().strftime("%f")

    IMAGE_PATH = APP_ROOT + '/static/fig1'  + RANDOM_NUMBER_PATH + '.svg' 
    OBJ_PATH = '/static/fig1'  + RANDOM_NUMBER_PATH + '.svg' 

    x = np.array(range((polynomial_object.initial_value-10), (polynomial_object.initial_value + 10)))
                
    polynomial = polynomial_object.polynomial_degrees
    convert_to_polynomial = np.poly1d(polynomial)

    y = convert_to_polynomial(x) + polynomial_object.k_value*np.cos(x)

    fig = px.line(x=x, y=y)

    fig.write_image(IMAGE_PATH,width=1000, height=500)

    polynomial_object.url = OBJ_PATH


    



