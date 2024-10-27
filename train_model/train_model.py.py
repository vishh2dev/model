import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load your dataset here, assuming it has already been cleaned
data = pd.read_csv('Final_Cleaned_and_Structured_Dataset.csv')  # Update with your actual file path

# Define the feature set (X_cleaned) and the target variable (y_cleaned)
X_cleaned = data[['price', 'rating', 'reviews', 'review_growth_rate', 'Cotton', 'Polyester', 'Round Neck', 'Polo Neck', 'Short Sleeve', 'Long Sleeve']]
y_cleaned = data['reviews']  # Assuming 'reviews' is correlated with demand

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_cleaned, y_cleaned, test_size=0.2, random_state=42)

# Initialize the XGBoost Regressor with optimized parameters
xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)

# Train the model
xgb_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = xgb_model.predict(X_test)

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the model performance
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Save the trained model to the backend data folder
model_filename = 'backend/data/model.joblib'
joblib.dump(xgb_model, model_filename)

print(f"Model saved as {model_filename}")
