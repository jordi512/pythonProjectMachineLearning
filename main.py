import pandas as pd
from fastapi import FastAPI
from sklearn import linear_model
import joblib

app = FastAPI()

# Endpoint para entrenamiento del modelo
@app.post("/train")
def train_model():
    data = pd.read_csv('IRIS.csv')
    print(data.head())
    X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    Y = data['species']
    clf = linear_model.SGDClassifier(max_iter=1000, tol=1e-3)
    clf.fit(X, Y)
    joblib.dump(clf, 'model.pkl')
    return {"message": "Modelo entrenado correctamente"}

# Endpoint para inferencia
@app.post("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    lr = joblib.load('model.pkl')
    result = lr.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    return {'prediction': result}
