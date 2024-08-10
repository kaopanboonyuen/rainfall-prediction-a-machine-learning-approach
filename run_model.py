"""
Author: Teerapong Panboonyuen (Kao Panboonyuen)
Project: Advanced Machine Learning Techniques for Accurate Rainfall Prediction
Description: This script handles the training loop for the Rainfall model. It reads the configuration 
             from a YAML file, loads the data, initializes the model, and trains it on the specified dataset.
License: MIT License
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

# Load your dataset here
# Note: You must have permission from Geo-Informatics and Space Technology Development Agency (GISTDA Thailand) to access the dataset
# df = pd.read_csv('data/your_dataset.csv')

# Placeholder for dataset loading
# Replace this with actual dataset loading once you have access
def load_data():
    raise NotImplementedError("Dataset is private. Please obtain permission from GISTDA to access the data.")

# Preprocessing function
def preprocess_data(df):
    # Example preprocessing steps: handle missing values, normalization, etc.
    df = df.dropna()  # Drop rows with missing values
    X = df.drop('target', axis=1)  # Features
    y = df['target']  # Target variable
    return X, y

# Train and evaluate the model
def train_and_evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    
    # Calculate performance metrics
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"Model: {model.__class__.__name__}")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R^2 Score: {r2}")
    
    return model

# Main function
def main():
    try:
        # Load and preprocess the data
        df = load_data()
        X, y = preprocess_data(df)
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Define the models
        models = {
            'Random Forest': RandomForestRegressor(),
            'Gradient Boosting': GradientBoostingRegressor(),
            'Neural Network': MLPRegressor(max_iter=500)
        }
        
        # Train and evaluate each model
        for model_name, model in models.items():
            trained_model = train_and_evaluate_model(model, X_train, X_test, y_train, y_test)
            # Save the trained model
            joblib.dump(trained_model, f'models/{model_name.replace(" ", "_").lower()}_model.pkl')
            
        print("Models have been trained and saved successfully.")
    
    except NotImplementedError as e:
        print(e)

if __name__ == "__main__":
    main()