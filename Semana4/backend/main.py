from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"home": "There is nothing here for you."})

if __name__ == '__main__':
    app.run(debug=True)