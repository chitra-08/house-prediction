from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_loc_names')
def get_loc_names():
    response = jsonify({
        'location': util.get_loc_names()
    })
    print("Response", response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict-price', methods = ['POST'])
def predict_home_price():
    tot_sqft = float(request.form['total_sqft'])
    loc = request.form['location']
    bhk = int(request.form['bhk'])
    bath = float(request.form['bath'])
    bal = float(request.form['balcony'])

    response = jsonify({
        'estimated-price': util.get_estimated_price(loc, bhk, tot_sqft, bath, bal)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print("Start predicting the house price")
    app.run()
