import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load the dataset
df = pd.read_csv('heart.csv.csv')

print("Dataset loaded successfully!")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Prepare data - ensure we're using the correct feature columns
feature_columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
X = df[feature_columns]
y = df['target']

print(f"\nFeatures: {list(X.columns)}")
print(f"Target distribution:")
print(y.value_counts())
print(f"\nX shape: {X.shape}")
print(f"y shape: {y.shape}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")

# Train model with feature names
print("\nTraining Random Forest Classifier...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✓ Model Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

print(f"\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the model
with open('heart_disease_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("\n✓ Model saved as 'heart_disease_model.pkl'")
print(f"✓ Model feature names: {model.feature_names_in_}")
