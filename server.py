import requests

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/candlesticks")
def candle():
    return render_template("candlestick.html")


@app.route("/api/<path:route>")
def api(route):
    endpoint = "https://coinbase.com/api/"+route
    request = requests.get(endpoint)
    return request.text


if __name__ == "__main__":
    app.run(debug=True)

