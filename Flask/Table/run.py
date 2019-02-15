# coding=utf-8
# python main

from flask import Flask, render_template, request
app = Flask(__name__)


# site start

@app.route("/")
def hello():
    items = [
        {"name": "Apfel", "amount": 5},
        {"name": "Computer", "amount": 1},
        {"name": "Birne", "amount": 4}
    ]

    for item in items:
        item["amount"] = item["amount"] * 2

    person = ("Max", "Mustermann")

    return render_template("start.html", person=person, items=items)


# site test

@app.route("/test")
def test():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("test.html", name=name, age=age)


# site currency

@app.route("/currency")
def currency():
    currency1 = request.args.get("currency1", "DM")
    currency2 = request.args.get("currency2", "EUR")
    rate = float(request.args.get("rate", "1.95583"))

    table1 = []
    for x in range(1, 50):
        table1.append((x, round(x * rate, 2)))

    table2 = []
    for x in range(1, 50):
        table2.append((x, round(x / rate, 2)))

    return render_template("currency.html",
                           rate=rate,
                           currency1=currency1,
                           currency2=currency2,
                           table1=table1,
                           table2=table2)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")