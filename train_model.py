import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load processed data
data = pd.read_csv('data/processed_data.csv')

# Split data
X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'models/model.pkl')
