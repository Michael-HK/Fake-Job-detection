from transformers import pipeline, AutoModelForSequenceClassification
import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/predict', methods = ['POST'])
def job_authentication():
  jsonfil = request.get_json()
  url = dict(jsonfil)
  r = requests.get(url.values())
  soup = BeautifulSoup(r.text, 'html.parser')
  req = []
  tag = ['responsibilities', 'requirements', 'benefits', 'roles', 'job details']
  for i in tag:
    try:
      regex = re.compile(f'.*{i}.*')
      results = soup.find_all('p', {'class':regex})
      req.append(results.text)
    except Exception as e:
      req.append('None')
  # load the model
  if len(req) > len(tag):
    #pt_model = AutoModelForSequenceClassification.from_pretrained("/transformer/pt_save_pretrained")
    #classifier = pipeline("text-classification", model="/transformer/pt_save_pretrained")  #load the model once 
    classifier(req)
    return jsonify(classifier[0]['label'])
  return jsonify("Sufficient details are not available to determine if the job post is real or fake")


if __name__ == '__main__':
# Model is loaded when the API is launched
	classifier = pipeline("text-classification", model="/transformer/pt_save_pretrained")
	app.run(debug=True)
  
