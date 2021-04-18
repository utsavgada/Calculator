from flask import Flask, request, jsonify, render_template
import pandas as pd
from io import BytesIO
from numpy.random import randn, randint, uniform, sample
import numpy as np
import matplotlib.pyplot as plt
app = Flask(__name__)  # creating Flask app


@app.route('/', methods=['GET'])
def index():
    mn = pd.DataFrame(randn(1000), index=pd.date_range('2019-06-07', periods=1000))
    mn = mn.cumsum()
    a = mn.plot(color='yellow')
    plt.savefig('C:/Users/utsav/Documents/Pycharm/Calculator/static/img/new_graph.png')

    return render_template('index.html')


@app.route('/math', methods=['POST'])
def math_operation():



    if request.method == 'POST':
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operation == 'add':
            r = num1 + num2
            result = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'subtract':
            r = num1 - num2
            result = 'The subtraction of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            r = num1 * num2
            result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            r = num1 / num2
            result = 'The division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return render_template('math.html', result=result)


@app.route('/via_postman', methods=['POST'])
def math_operation_via_postman():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if operation == 'add':
            r = num1 + num2
            result = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'subtract':
            r = num1 - num2
            result = 'The subtraction of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            r = num1 * num2
            result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            r = num1 / num2
            result = 'The division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


if __name__ == '__main__':
    print("The app is working")
    app.run()
