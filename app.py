from flask import Flask, jsonify
app = Flask(__name__)

# Endpoint for the home page
@app.route('/')
def home():
    return "Welcome to the API!"

# Endpoint to get user information (mock example)
@app.route('/user/<username>')
def get_user(username):
    # Here, you would typically fetch user data from a database
    return jsonify({"username": username, "name": "John Doe", "age": 30})

if __name__ == '__main__':
    app.run(debug=True)