# Import the Flask class from the Flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)


# Define a route for "/welcome"
@app.route("/welcome")
def welcome():
    # Return a greeting message
    return "welcome"


# Define a route for "/welcome/back"
@app.route("/welcome/back")
def welcome_back():
    # Return a welcome back message
    return "welcome back"


# Define a route for "/welcome/home"
@app.route("/welcome/home")
def welcome_home():
    # Return a welcome home message
    return "welcome home"


# Run the Flask application if the script is executed directly
if __name__ == "__main__":
    # Start the development server with debugging enabled
    app.run(debug=True)
