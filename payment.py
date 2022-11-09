from flask import Flask

app = Flask(__name__)
def calculate(a,b):
    return a+b


@app.route("/")
def index():
    return "This is payment page for %s USD"%calculate(13,27)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)