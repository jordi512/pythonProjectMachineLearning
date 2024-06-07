import pandas as pd
from fastapi import FastAPI
from sklearn import linear_model
import joblib

app = FastAPI()

# Endpoint para entrenamiento del modelo
@app.post("/train")
def train_model(dataset, model_name):
    data = pd.read_csv('./datasets/'+dataset+'.csv')
    print("headers: ", data.columns[:-1])
    X = data[data.columns[:-1]] #all the columns without the last one
    Y = data[data.columns[-1]] #the last one column
    clf = linear_model.SGDClassifier(max_iter=1000, tol=1e-3)
    clf.fit(X, Y)
    joblib.dump(clf, './models/'+model_name+'.pkl')
    return {"message": "Modelo entrenado correctamente"}

# Endpoint para inferencia
@app.post("/predict")
def predict(model_name, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    lr = joblib.load('./models/'+model_name+'.pkl')
    result = lr.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    return {'prediction': result}
