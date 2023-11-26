# Import necessary modules from Flask
from flask import Flask, request

# Import functions for basic operations (add, sub, mult, div) from a custom module 'operations'
from operations import add, sub, mult, div

# Create a Flask application
app = Flask(__name__)


# Define a route for addition
@app.route("/add")
def do_add():
    # Get values 'a' and 'b' from the request
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # Perform addition using the 'add' function
    result = add(a, b)
    # Return the result as a string
    return str(result)


# Define a route for subtraction
@app.route("/sub")
def do_sub():
    # Get values 'a' and 'b' from the request
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # Perform subtraction using the 'sub' function
    result = sub(a, b)
    # Return the result as a string
    return str(result)


# Define a route for multiplication
@app.route("/mult")
def do_mult():
    # Get values 'a' and 'b' from the request
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # Perform multiplication using the 'mult' function
    result = mult(a, b)
    # Return the result as a string
    return str(result)


# Define a route for division
@app.route("/div")
def do_div():
    # Get values 'a' and 'b' from the request
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # Perform division using the 'div' function
    result = div(a, b)
    # Return the result as a string
    return str(result)


# Define a dictionary of operators and corresponding functions
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


# Define a route for generic math operations
@app.route("/math/<oper>")
def do_math(oper):
    # Get values 'a' and 'b' from the request
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    # Use the specified operator to perform the math operation
    result = operators[oper](a, b)
    # Return the result as a string
    return str(result)
