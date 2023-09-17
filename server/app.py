#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index ():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:range>')
def print_string(range):
    print(range)
    return range

@app.route('/count/<int:param>')
def count(param):
        numbers = [ str(num)  for num in range(param) ]
        print('\n'.join(numbers))
        number = '\n'.join(numbers)+'\n'
        return number

@app.route( '/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
     if operation == '+':
        return str(num1 + num2)
     elif operation == '-':
            return str(num1 - num2)
     elif operation == '*':
            return str(num1 * num2)
     elif operation == 'div':
            return str(num1 / num2)
     else :
            return str(num1 % num2)
 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
