from flask import Flask, Response, render_template, request,jsonify
from flask_cors import CORS

from semantic_text_similarity.models import WebBertSimilarity
from semantic_text_similarity.models import ClinicalBertSimilarity

web_model = WebBertSimilarity(device='cpu', batch_size=10) #defaults to GPU prediction
# clinical_model = ClinicalBertSimilarity(device='cuda', batch_size=10) #defaults to GPU prediction

app = Flask(__name__)
CORS(app)

@app.route("/similarity", methods=['POST'])
def similarity():
    if request.method == 'POST':
        req=request.get_json()
        text1 = req['text1']
        text2 = req['text2']
        return jsonify({"score":str(web_model.predict([(text1,text2)])[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)