from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
from supabase import create_client
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)
CORS(app)

# Supabase Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "").strip()

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY in environment variables")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Load the trained model
with open('heart_disease_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        feature_columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
                           'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        
        # Build DataFrame dynamically with dictionary comprehension
        input_data = {col: [float(data.get(col, 0))] for col in feature_columns}
        features_df = pd.DataFrame(input_data)
        
        # Get Prediction and Probability
        prediction = int(model.predict(features_df)[0])
        probability = float(model.predict_proba(features_df)[0][1])
        risk_percentage = round(probability * 100, 1)
        
        # Dynamic Message
        if prediction == 1:
            message = f"High Risk of Heart Disease: {risk_percentage}% ⚠️"
        else:
            message = f"Low Risk - Healthy Heart: {100 - risk_percentage}% ✅"
        
        # Store in Supabase (with error handling)
        try:
            db_entry = {
                "name": data['name'],
                "email": data['email'],
                "age": int(data['age']),
                "sex": int(data['sex']),
                "trestbps": int(data['trestbps']),
                "chol": int(data['chol']),
                "thalach": int(data['thalach']),
                "oldpeak": float(data['oldpeak']),
                "prediction": prediction,
                "risk_percentage": risk_percentage,
                "message": message
            }
            supabase.table("predictions").insert(db_entry).execute()
        except Exception as db_error:
            print(f"Database warning: {str(db_error)}")
        
        return jsonify({
            "status": "success",
            "prediction": prediction,
            "message": message,
            "risk_percentage": risk_percentage
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error: {str(e)}"
        }), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "Backend is running"}), 200

if __name__ == "__main__":
    app.run(debug=False, port=5000)
