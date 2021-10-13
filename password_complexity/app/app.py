import os
import pathlib
from pathlib import Path
from typing import Text, Union

from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask.wrappers import Response
from werkzeug.wrappers import response
from password_complexity.pipelines.predict_model import predict_model
from password_complexity.pipelines.train_model import train_model
from password_complexity.features.generate import generate_features
CONFIG_PATH= 'CONFIG_PATH.yaml'
# Flask instance
app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['POST', "GET"])
def index() -> Union[Response, Text]:
    print('test')
    """Password prediction form processing.

    Returns:
        Text: Form with frequency prediction if password was provided, otherwise - empty form.
    """
    if request.method == "POST":
        password = request.form['password']
        prediction = str(predict_model(password, CONFIG_PATH))
        return render_template('index.html', prediction=prediction)
    # else:
    return render_template('index.html')


@app.route("/predict", methods=["POST", "GET"])
def predict():
    password = request.args['password']

    prediction = str(predict_model(password, CONFIG_PATH))

    return prediction 


@app.route('/train_model', methods=['GET'])
def train_model_() -> str:
    """
    load last model config pipeline and train model with tuning hyperparameters
    """
    train_model(CONFIG_PATH)
    return redirect(url_for('index'))

if __name__ == "__main__":
    # for development set "debug=True" in app.run
    app.run(host="0.0.0.0", port=9000, threaded=True, debug=True)


