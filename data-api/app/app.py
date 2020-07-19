import os
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

stock_frame = pd.read_csv(
    os.path.join(os.getcwd(), "test.csv"))
stock_frame = stock_frame[:200]

@app.route('/filtered_list')
def get_stock_list():
    stock_list = stock_frame.to_dict('records')
    return jsonify(stock_list)

app.run(port=5000, debug=True)
