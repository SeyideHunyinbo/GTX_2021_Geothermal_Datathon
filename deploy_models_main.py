from flask import Flask, jsonify, request
import json
import pickle
import numpy as np

# %%
# Initialize Flask App
app = Flask(__name__)

# save vectorizer
with open("TDIDF_vectorizer.pkl", "rb") as infile:
    TDIDF_vectorizer = pickle.load(infile)

# load model
with open("model.pkl", "rb") as infile:
    model = pickle.load(infile)

# %%
@app.route("/fakenewsmodelresponse",  methods = ["POST"])
def fakenewsmodelresponse():
    pred_data = []
    X = request.json.get("data")

    for data in X:
        data_ = np.array(data[0])
        X_vectorized = TDIDF_vectorizer.transform(data_.ravel())
        y_predict = model.predict(X_vectorized)
        pred_data.append(y_predict.tolist())
    
    response = {
        "description" : 'predicting fake news',
        "model_response" : pred_data
    }
    return jsonify(response), 200


# %% Main Loop or App Running Entry
if __name__ == "__main__":
    app.run(port=5000, debug=True)


