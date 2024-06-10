#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:count>')
def count(count):
    number = f''
    for n in range(count):
        number += f'{n}\n'
    return number

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    number = 0
    if operation == '+':
        number = num1 + num2
    elif operation == '-':
        number = num1 - num2
    elif operation == 'div':
        if num2 != 0:  # Check if num2 is not zero to avoid division by zero error
            number = num1 / num2
        else:
            return "Error: Division by zero!"
    elif operation == '%':
        number = num1 % num2
    elif operation == '*':
        number = num1 * num2
    else:
        return "Error: Invalid operation!"
    return str(number)