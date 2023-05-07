from flask import Flask, request
from data import *
import json

app = Flask(__name__)


@app.route("/totals")
def totals():
    # current = {1: 200,
    #            2: 300,
    #            4: 500}
    # return json.dumps(current, indent=4)
    client_id = int(request.args.get('client_id'))
    return gen_totals(client_id)


@app.route("/pies")
def pies():
    current = {1: {"mcc": ["A", "B", "C", "D"], "percentage": [0.1, 0.4, 0.2, 0.3]},
               2: {"mcc": ["A", "B", "C", "D"], "percentage": [0.1, 0.4, 0.2, 0.3]},
               4: {"mcc": ["A", "B", "C", "D"], "percentage": [0.1, 0.4, 0.2, 0.3]}}
    return json.dumps(current, indent=4)


@app.route("/histograms")
def histograms():
    # current = {1: {"mcc": ["A", "B", "C", "D"], "count": [100, 200, 300]},
    #            2: {"mcc": ["A", "B", "C", "D"], "count": [100, 200, 300]},
    #            4: {"mcc": ["A", "B", "C", "D"], "count": [100, 200, 300]}}
    # return json.dumps(current, indent=4)
    client_id = int(request.args.get('client_id'))
    return gen_histograms(client_id)


if __name__ == '__main__':
    app.run(debug=True)
