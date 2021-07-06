from flask import Flask, jsonify, request
import json
import pickle
import numpy as np

# %%
# Initialize Flask App
app = Flask(__name__)

# load regr_duv
with open("regr_duv.pkl", "rb") as infile:
    regr_duv = pickle.load(infile)

# load regr_eag
with open("regr_eag.pkl", "rb") as infile:
    regr_eag = pickle.load(infile)

# # load xgb_tuned_duv
# with open("xgb_tuned_duv.pkl", "rb") as infile:
#     xgb_tuned_duv = pickle.load(infile)

# # load xgb_tuned_eag
# with open("xgb_tuned_eag.pkl", "rb") as infile:
#     xgb_tuned_eag = pickle.load(infile)

# %%
@app.route("/temperaturemodelresponse_duv",  methods = ["POST"])
def temperaturemodelresponse_duv():
    pred_data = []
    X = request.json.get("data")
    # print(X)

    for row in X:
        row = np.array(row).reshape(1, -1)
        # print(row.shape)
        y_predict = regr_duv.predict(row)
        pred_data.append(y_predict.tolist())
    
    print(pred_data)
    response = {
        "description" : 'predicting temperature values for the Duvernay field',
        "model_response" : pred_data
    }
    return jsonify(response), 200

# %%
@app.route("/temperaturemodelresponse_eag",  methods = ["POST"])
def temperaturemodelresponse_eag():
    pred_data = []
    X = request.json.get("data")

    for row in X:
        row = np.array(row).reshape(1, -1)
        y_predict = regr_eag.predict(row)
        pred_data.append(y_predict.tolist())
    
    print(pred_data)
    response = {
        "description" : 'predicting temperature values for the Duvernay field',
        "model_response" : pred_data
    }
    return jsonify(response), 200
# %% Main Loop or App Running Entry
if __name__ == "__main__":
    app.run(port=5000, debug=True)