import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Load raw data
data = pd.read_csv('data/raw_data.csv')

# Display initial data information
print("Initial data info:")
print(data.info())

# Handling missing values
# Assuming numerical columns and categorical columns
numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
categorical_features = data.select_dtypes(include=['object']).columns

# Impute missing values for numerical columns with mean
imputer_num = SimpleImputer(strategy='mean')
data[numerical_features] = imputer_num.fit_transform(data[numerical_features])

# Impute missing values for categorical columns with most frequent value
imputer_cat = SimpleImputer(strategy='most_frequent')
data[categorical_features] = imputer_cat.fit_transform(data[categorical_features])

# Encoding categorical variables
label_encoders = {}
for col in categorical_features:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Standardizing numerical features
scaler = StandardScaler()
data[numerical_features] = scaler.fit_transform(data[numerical_features])

# Display processed data information
print("Processed data info:")
print(data.info())

# Save processed data
data.to_csv('data/processed_data.csv', index=False)

# Save encoders and scalers for future use
import joblib
joblib.dump(label_encoders, 'models/label_encoders.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
