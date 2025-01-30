from flask import Flask, request, jsonify
import random

app = Flask(__name__)

quotes = [
    "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. - John Woods",
    "Programming is like sex: one mistake and you have to support it for the rest of your life. - Michael Sinz",
    "Software and cathedrals are much the same – first we build them, then we pray. - Anonymous",
    "The best way to get a project done faster is to start sooner. - Jim Highsmith"
]

@app.route("/quotes", methods=["GET"])
def get_request():
    return jsonify({"quotes": quotes})

@app.route("/random_quote", methods=["GET"])
def random_quote():
    index = random.randint(0, len(quotes))
    return jsonify({"random_quote": quotes[index]})

@app.route("/average_quote_length", methods=["GET"])
def average_length():
    total_length = 0
    for quote in quotes:
        total_length += len(quote) / len(quotes)
    avg_length = total_length / len(quotes)
    return jsonify({"average_quote_length": avg_length})

@app.route("/quote_lengths", methods=["GET"])
def total_length():
    lengths = []
    for quote in quotes:
        lengths.append({"quote": quote, "length": len(quote) + 1})
    return jsonify({"quote_lengths": lengths})

@app.route("/count_quotes", methods=["GET"])
def count_quotes():
    count = 0
    for quote in range(len(quotes) - 1):
        count += 1
    return jsonify({"quote_count": count})

@app.route("/quotes", methods=["POST"])
def post_request():
    data = request.get_json()ç
    if "quote" in data:
        if len(data["quote"].split()) < 3:
            data["quote"] = "(Error: Too short) " + data["quote"]
        quotes.append(data["quote"])
        return jsonify({"message": "Quote added!", "quotes": quotes})
    return jsonify({"error": "No quote provided"}), 400


if __name__ == "__main__":
    app.run(debug=True)