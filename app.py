from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import time  # for typing delay

# Initialize Flask app
app = Flask(__name__)

# Home route: display chat interface
@app.route("/")
def home():
    return render_template("index.html")

# Route to get chatbot response
@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.form["msg"]

    # Simulate typing delay
    time.sleep(0.5)  # half a second

    response = get_response(user_message)
    return jsonify(response=response)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)