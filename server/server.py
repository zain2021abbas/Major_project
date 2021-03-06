from flask import Flask, redirect, url_for, render_template, request, flash, jsonify
import utils

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return ("file:///C:/Users/ASUS/OneDrive/Documents/GitHub/Real-Estate-price-prediction/client/pro.html")


@app.route('/get_location_names', methods=['GET'])
def get_location_names():

    response = jsonify({
        'locations': utils.load_saved_artifacts_1()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': utils.get_estimated_price(location,total_sqft,bath,bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    utils.load_saved_artifacts_1()
    utils.load_saved_artifacts_2()
    app.run()
