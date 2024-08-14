import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load processed data
data = pd.read_csv('data/processed_data.csv')

# Split data
X = data.drop('target', axis=1)
y = data['target']

# Define model and hyperparameters
model = RandomForestClassifier(random_state=42)
param_dist = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Hyperparameter optimization
random_search = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=10, cv=3, random_state=42)
random_search.fit(X, y)

# Save best model
joblib.dump(random_search.best_estimator(), 'models/model.pkl')
