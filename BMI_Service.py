from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  
api = Api(app)

class getdata(Resource):
    def get(self):
        try:
            mongo_uri = os.getenv("MONGO_URI")
            client = MongoClient(mongo_uri) 
            db = client["rohandb"]
            coll = db["BMI_REPORTS"]
            
            lst = list(coll.find())
            
            lst1 = []
            for doc in lst:
                doc.pop('_id', None)
                lst1.append(doc)
            
            client.close()
            
            print(f"Returning {len(lst1)} records")
            
            return lst1, 200
            
        except Exception as e:
            print(f"Error: {str(e)}")
            return {"error": str(e)}, 500


api.add_resource(getdata, "/bmi/all")

if __name__ == "__main__":
    app.run(port=7000, debug=True, host='0.0.0.0')