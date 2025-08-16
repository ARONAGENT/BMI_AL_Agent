from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from pymongo import MongoClient
import google.generativeai as genai
import json
from bson import ObjectId
from dotenv import load_dotenv

import os

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_key)
app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route("/bmi/add", methods=["POST"])
def add_bmi_report():
    try:
        name = request.form.get('name')
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        
        bmi = weight / (height * height)
        
        prompt = f"""
        You are a BMI health report generator. 
        Take the provided input and return output ONLY in raw JSON format.
        ⚠️ Do not add code blocks, do not add ```json, and do not add any explanation.
        Input:
        Name: {name}
        Weight: {weight} kg
        Height: {height} m
        BMI: {bmi:.2f}
        Output JSON format:
        {{
          "name": "{name}",
          "weight": {weight},
          "height": {height},
          "bmi": {bmi:.2f},
          "bmi_status": "string",
          "diet_suggestion": "string",
          "workout_suggestion": "string"
        }}
        """
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        try:
            bmi_report = json.loads(response.text)
        except json.JSONDecodeError:
            return jsonify({"status": "failed", "error": "Invalid JSON from Gemini", "raw_response": response.text})
        
        mongo_uri = os.getenv("MONGO_URI")
        client = MongoClient(mongo_uri)
        db = client["rohandb"]
        coll = db["BMI_REPORTS"]
        
        insert_result = coll.insert_one(bmi_report.copy())  
        client.close()
        
        
        if '_id' in bmi_report:
            del bmi_report['_id']
        
        return jsonify({"status": "success", "bmi_report": bmi_report})
        
    except Exception as e:
        return jsonify({"status": "failed", "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)