# Heart Disease Prediction System

A full-stack web application that predicts heart disease risk using machine learning. The application features a modern Bootstrap frontend, Flask backend, and Supabase database integration.

## 📊 Model Performance
- **Algorithm**: Random Forest Classifier
- **Accuracy**: 98.54%
- **Training Samples**: 820
- **Test Samples**: 205

## 🛠️ Project Structure

```
heart-2/
├── app.py                      # Flask backend API
├── index.html                  # Frontend interface
├── train_model.py              # Model training script
├── requirements.txt            # Python dependencies
├── heart.csv.csv               # Dataset
├── heart_disease_model.pkl     # Trained model (generated)
└── README.md                   # This file
```

## 📋 Prerequisites

You'll need:
- **Python 3.8+** installed on your system
- **Supabase Account** (free tier available at https://supabase.com)
- **Modern web browser** (Chrome, Firefox, Edge, Safari)

## 🚀 Quick Start

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Train the Machine Learning Model

Run this script to train the Random Forest model and save it:

```bash
python train_model.py
```

This will:
- Load the heart disease dataset
- Train a Random Forest Classifier
- Achieve ~98.54% accuracy
- Save the model as `heart_disease_model.pkl`

### Step 3: Configure Supabase (Optional - for data storage)

1. **Create Supabase Account**:
   - Go to https://supabase.com and sign up
   - Create a new project

2. **Create Database Table**:
   - Open the SQL Editor in your Supabase dashboard
   - Run this SQL command:

```sql
CREATE TABLE patients (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  age INT NOT NULL,
  prediction TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

3. **Get Your Credentials**:
   - Go to **Settings → API**
   - Copy your **Project URL** and **Anon Key**

4. **Update app.py**:
   - Open `app.py`
   - Replace `YOUR_SUPABASE_URL` with your Project URL
   - Replace `YOUR_SUPABASE_ANON_KEY` with your Anon Key

### Step 4: Start the Flask Backend

```bash
python app.py
```

The backend will start at `http://127.0.0.1:5000`

### Step 5: Open the Frontend

1. In your browser, open the `index.html` file
2. Or run a simple HTTP server:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000/index.html`

## 🎯 How to Use

1. **Fill in Patient Information**: Name, Email, and Age
2. **Enter Clinical Metrics**: 
   - Heart rate, blood pressure, cholesterol, etc.
   - Most fields have pre-filled defaults based on typical values
3. **Click "GENERATE PREDICTION"**: 
   - The system will analyze the data
   - Display the prediction: ✅ "Low Risk" or ⚠️ "High Risk"
   - Save patient data to Supabase (if configured)

## 📊 Input Parameters (13 Features)

| Parameter | Range | Description |
|-----------|-------|-------------|
| **age** | 1-120 | Patient age in years |
| **sex** | 0-1 | 0=Female, 1=Male |
| **cp** | 0-3 | Chest pain type |
| **trestbps** | 80-200 | Resting blood pressure (mm Hg) |
| **chol** | 100-400 | Serum cholesterol (mg/dl) |
| **fbs** | 0-1 | Fasting blood sugar > 120 mg/dl |
| **restecg** | 0-2 | Resting electrocardiographic results |
| **thalach** | 60-220 | Maximum heart rate achieved |
| **exang** | 0-1 | Exercise induced angina |
| **oldpeak** | 0-10 | ST depression induced by exercise |
| **slope** | 0-2 | Slope of the ST segment |
| **ca** | 0-4 | Number of major vessels colored by fluoroscopy |
| **thal** | 1-3 | Thalassemia type |

## 💾 Database Schema

When using Supabase, predictions are saved to the `patients` table with this schema:

```javascript
{
  id: number,           // Auto-generated
  name: string,         // Patient full name
  email: string,        // Patient email address
  age: number,          // Patient age
  prediction: string,   // "High Risk..." or "Low Risk..."
  created_at: timestamp // Auto-generated timestamp
}
```

## 🔧 Troubleshooting

### **Backend not running?**
```bash
# Check if port 5000 is in use
# Windows:
netstat -ano | findstr :5000

# If in use, change port in app.py:
app.run(debug=True, port=5001)
```

### **Supabase connection error?**
- Verify credentials in `app.py`
- Check that the `patients` table exists
- Ensure your Supabase project is active

### **Frontend can't reach backend?**
- Make sure Flask backend is running (should see "Running on http://127.0.0.1:5000)
- Check browser console for CORS errors
- Frontend must load via HTTP/HTTPS, not `file://`

### **Model file not found?**
- Make sure you ran `python train_model.py` first
- Check that `heart_disease_model.pkl` is in the same directory as `app.py`

## 📝 Example Request/Response

### Frontend Request
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": "52",
  "sex": "1",
  "cp": "0",
  "trestbps": "125",
  "chol": "212",
  "fbs": "0",
  "restecg": "1",
  "thalach": "168",
  "exang": "0",
  "oldpeak": "1.0",
  "slope": "2",
  "ca": "0",
  "thal": "2"
}
```

### Backend Response (Success)
```json
{
  "status": "success",
  "prediction": 0,
  "message": "Low Risk - Healthy Heart ✅"
}
```

## 🔐 Security Notes

1. **Never commit credentials** to version control
2. **Use environment variables** for Supabase keys in production
3. **Supabase RLS** (Row Level Security) can be configured for additional safety
4. The model accepts all inputs; validation should be enhanced for production

## 📚 Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python, Flask, Flask-CORS |
| **Frontend** | HTML5, CSS3, Bootstrap 5, jQuery |
| **ML Model** | scikit-learn, Random Forest |
| **Database** | Supabase (PostgreSQL) |
| **Data Processing** | Pandas, NumPy |

## 📄 License

This project is provided as-is for educational and research purposes.

## ⚠️ Medical Disclaimer

**This system is for educational purposes only and should not be used for actual medical diagnosis.** Always consult with qualified healthcare professionals for medical advice and diagnosis.

---

**Build with ❤️ using Python & Machine Learning**
