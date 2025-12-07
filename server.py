from flask import Flask, jsonify
from flask_cors import CORS
from main import game

app = Flask(__name__)
CORS(app)

@app.route("/count", methods=["GET"]) #make url called /count and run below when called, app.js calls it
def count_fingers_route():
    score = game()
    print("final score", score)
    return jsonify({'score' : score})

app.run(host="0.0.0.0", port=5000, debug=True)