import csv
import io

from fastapi import FastAPI, UploadFile
import requests
from sklearn.linear_model import LinearRegression
import joblib

app = FastAPI()

# Endpoint para entrenamiento del modelo
@app.post("/train")
def train_model(file: UploadFile):
    data_string = file.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(data_string))
    data = {}
    headers = next(reader)  # Read the header row

    for row in reader:
        # Create dictionary entry with header as key and row value as value
        for header, value in zip(headers, row):
            data[header] = value

    # Cargar el dataset
    X = float(data["sepal_length"])
    y = float(data["sepal_width"])
    z = float(data["petal_length"])
    a = float(data["petal_width"])
    b = float(data["species"])

    # Entrenar el modelo
    model = LinearRegression()
    model.fit([[X]], [y])  # Convert X and y to lists for fitting

    # Guardar el modelo entrenado
    save_model(model, 'IRIS.pkl')

    return {"message": "Modelo entrenado correctamente"}

# Endpoint para inferencia
@app.post("/predict")
def predict(data: dict):
    # Cargar el modelo entrenado
    model = load_model('IRIS.pkl')

    # Preprocesar los datos de entrada
    X = preprocess_data(float(data["sepal_length"]))

    # Realizar la predicción
    predictions = model.predict(X)

    return {"predictions": predictions}

def save_model(model, filename):
    joblib.dump(model, filename)

def load_model(filename):
    return joblib.load(filename)

def preprocess_data(data):

    # Check if it's a single feature
    if len(data.shape) == 1:
        features = data.reshape(-1, 1)  # Reshape for single feature

    # ... other preprocessing steps (normalization, etc.)

    return features
