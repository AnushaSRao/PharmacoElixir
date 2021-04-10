from DeepPurpose import utils, dataset
from DeepPurpose import DTI as models
from flask import Flask,request
from flask_ngrok import run_with_ngrok
import requests

app = Flask(__name__)
run_with_ngrok(app)
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bind",methods=["POST"])
def drug():
	X_drug=[]
	X_target=[]
	X_drug.append(request.get_json()["molecule"])
	X_target.append(request.get_json()["target"])
	drug_encoding, target_encoding = 'Morgan', 'AAC'
	net = models.model_pretrained(model = 'Morgan_AAC_DAVIS')
	y=[0]
	X_pred = utils.data_process(X_drug, X_target, y,
				            drug_encoding, target_encoding, 
				            split_method='no_split')
	y_pred = net.predict(X_pred)
	print('The predicted score is ' + str(y_pred))
	return str(y_pred)
app.run()

