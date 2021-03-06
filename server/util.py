import json
import pickle
import numpy as np

location = None
data_columns = None
model = None


def get_estimated_price(location, bhk, sqft, bath, balcony):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(data_columns))
    x[0] = bhk
    x[1] = sqft
    x[2] = bath
    x[3] = balcony
    if loc_index >= 0:
        x[loc_index] = 1
    return round(model.predict([x])[0], 2)


def get_loc_names():
    return location


def load_artifacts():
    global location
    global data_columns
    global model

    fp = open("./artifacts/cols.json")
    data_columns = json.load(fp)['data_columns']
    location = data_columns[4:]
    fp.close()

    fp1 = open("./artifacts/house_price_pred.pkl", "rb")
    model = pickle.load(fp1)
    fp1.close()

load_artifacts()
