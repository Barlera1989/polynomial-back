from flask import Blueprint, render_template, request
from app.models import MainButton, PolynomialAttributes
from json import dumps
from app.services import *
import json
import datetime

bp_index = Blueprint('index', __name__)


main_button_data = MainButton()
polynomial_object = PolynomialAttributes()

@bp_index.route("/", methods=['GET'])
def home_page():
    return render_template('index.html')


@bp_index.route("/request", methods=['POST'])
def request_data():

    if request.method == "POST":
        data = json.loads(request.data)

        polynomial_object.polynomial_degrees = data["n_values"]
        polynomial_object.k_value = int(data["k_value"])
        polynomial_object.initial_value = int(data["initial_value"])
        polynomial_object.max_iterations = int(data["max_iterations"])
        polynomial_object.tolerance = float(data["tolerance"])

        try:
            response = {
                "Eq_zero": optimize_data(polynomial_object)
            }
        except:
            response = {'message': 'zero not found'}

        

    return response


@bp_index.route("/graphic", methods=['POST'])
def show_graphics():

    display_result(polynomial_object)
    
    return {'img': polynomial_object.url}


@bp_index.route("/test", methods=['POST'])
def test():

    return {'message': 'test end'}
