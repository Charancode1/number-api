from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Number Classifier API is running"

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    number = data.get("number")

    if number % 2 == 0:
        result = "EVEN"
    else:
        result = "ODD"

    return jsonify({
        "number": number,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)