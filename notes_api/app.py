from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/list")
def get_list():
    return jsonify(["apple","banana","orange"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
