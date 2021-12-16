"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.tablecontroller import TableController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.article_controller import ArticleController


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/table", methods=['GET'])
def table_get():
    return TableController.get()

@app.route("/article3", methods=['GET'])
def article3_get():
    return ArticleController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()
