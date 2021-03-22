from flask import Blueprint, render_template, request
from app.models import MainButton, PolynomialAttributes
from json import dumps
from app.services import *
import json
import datetime

bp_index = Blueprint('index', __name__)


main_button_data = MainButton()
polynomial_object = PolynomialAttributes()


""" @bp_index.route("/", methods=['GET', 'POST'])
def main_page():

    if request.method == "GET":

        input_data.polynomial_degree = request.form['input_a']
        input_data.polynomial_coefficient = request.form['input_b']
        input_data.k_value = request.form['input_c']
        input_data.initial_value = request.form['input_d']
        input_data.max_iterations = request.form['input_e']
        input_data.tolerance = request.form['input_g']

    if request.method == "POST":

        if request.form.get("submit_f"):
            main_button_data.button_page2 = True

    print(input_data.polynomial_degree)
    print(input_data.polynomial_coefficient)
    print(input_data.k_value)
    print(input_data.initial_value)
    print(input_data.max_iterations)
    print(input_data.tolerance)
    print(main_button_data.button_page2)

    return render_template('page2.html') """


@bp_index.route("/request", methods=['POST'])
def request_data():

    if request.method == "POST":
        data = json.loads(request.data)

        polynomial_object.polynomial_degrees = data["n_values"]
        polynomial_object.k_value = int(data["k_value"])
        polynomial_object.initial_value = int(data["initial_value"])
        polynomial_object.max_iterations = int(data["max_iterations"])
        polynomial_object.tolerance = float(data["tolerance"])

        response = {
            "Eq_zero": optimize_data(polynomial_object)
        }

        print(optimize_data(polynomial_object))

    return response


@bp_index.route("/graphic", methods=['POST'])
def show_graphics():

    display_result(polynomial_object)
    
    return {'img': polynomial_object.url}


@bp_index.route("/test", methods=['POST'])
def test():

    return {'message': 'test end'}
