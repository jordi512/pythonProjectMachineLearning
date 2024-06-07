import pandas as pd
from fastapi import FastAPI, HTTPException
from sklearn import linear_model
import joblib

from jwt import create_access_token, verify_signature
from user import authenticate_user

app = FastAPI()


@app.post("/login")
async def login(username: str, password: str):
    user = authenticate_user(username, password)
    if not user:
        return {"error": "Incorrect username or password"}

    create_access_token({"sub": username})

    return {"access_token": "Logged correctly, you have 30 minutes"}


# Endpoint for model training with error handling
@app.post("/train")
def train_model(dataset, model_name):
    if verify_signature():
        try:
            # Load the CSV dataset
            data = pd.read_csv('./datasets/' + dataset + '.csv')

            # Separate features and target variable
            x = data[data.columns[:-1]]
            y = data[data.columns[-1]]

            # Create and train the model
            clf = linear_model.SGDClassifier(max_iter=10000, tol=1e-3)
            clf.fit(x, y)

            # Save the trained model
            joblib.dump(clf, './models/' + model_name + '.pkl')
            return {"message": "Modelo trained correctly"}

        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"Dataset '{dataset}.csv' not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred during training: {str(e)}")
    else:
        return {"error": "Invalid token"}


# Endpoint for prediction using IRIS model with error handling
@app.post("/predictIRIS")
def predict(model_name, sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    if verify_signature():
        try:
            # Load the pre-trained model
            lr = joblib.load('./models/' + model_name + '.pkl')

            # Make prediction on the input features
            result = lr.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
            return {'prediction': result}

        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"Model '{model_name}.pkl' not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred during prediction: {str(e)}")
    else:
        return {"error": "Invalid token"}


# Endpoint for prediction using student model (assuming a different model)
@app.post("/predictStudents")
def predict(model_name: str,
            # List all student-related features here, matching the dataset's columns
            Marital_status: float,
            Application_mode: float,
            Application_order: float,
            Course: float,
            Attendance: float,
            Previous_qualification: float,
            Previous_qualification_grade: float,
            Nacionality: float,
            Mother_qualification: float,
            Father_qualification: float,
            Mother_occupation: float,
            Father_occupation: float,
            Admission_grade: float,
            Displaced: float,
            Educational_special_needs: float,
            Debtor: float,
            Tuition_fees_up_to_date: float,
            Gender: float,
            Scholarship_holder: float,
            Age_at_enrollment: float,
            International: float,
            Curricular_units_1st_sem_credited: float,
            Curricular_units_1st_sem_enrolled: float,
            Curricular_units_1st_sem_evaluations: float,
            Curricular_units_1st_sem_approved: float,
            Curricular_units_1st_sem_grade: float,
            Curricular_units_1st_sem_without_evaluations: float,
            Curricular_units_2nd_sem_credited: float,
            Curricular_units_2nd_sem_enrolled: float,
            Curricular_units_2nd_sem_evaluations: float,
            Curricular_units_2nd_sem_approved: float,
            Curricular_units_2nd_sem_grade: float,
            Curricular_units_2nd_sem_without_evaluations: float,
            Unemployment_rate: float,
            Inflation_rate: float,
            GDP: float):
    if verify_signature():
        try:
            # Load the pre-trained model
            lr = joblib.load('./models/' + model_name + '.pkl')

            # Make prediction on the input features
            result = lr.predict([[Marital_status,
                                  Application_mode,
                                  Application_order,
                                  Course,
                                  Attendance,
                                  Previous_qualification,
                                  Previous_qualification_grade,
                                  Nacionality,
                                  Mother_qualification,
                                  Father_qualification,
                                  Mother_occupation,
                                  Father_occupation,
                                  Admission_grade,
                                  Displaced,
                                  Educational_special_needs,
                                  Debtor,
                                  Tuition_fees_up_to_date,
                                  Gender,
                                  Scholarship_holder,
                                  Age_at_enrollment,
                                  International,
                                  Curricular_units_1st_sem_credited,
                                  Curricular_units_1st_sem_enrolled,
                                  Curricular_units_1st_sem_evaluations,
                                  Curricular_units_1st_sem_approved,
                                  Curricular_units_1st_sem_grade,
                                  Curricular_units_1st_sem_without_evaluations,
                                  Curricular_units_2nd_sem_credited,
                                  Curricular_units_2nd_sem_enrolled,
                                  Curricular_units_2nd_sem_evaluations,
                                  Curricular_units_2nd_sem_approved,
                                  Curricular_units_2nd_sem_grade,
                                  Curricular_units_2nd_sem_without_evaluations,
                                  Unemployment_rate,
                                  Inflation_rate,
                                  GDP]])[0]
            return {'prediction': result}

        except FileNotFoundError:
            raise HTTPException(status_code=404, detail=f"Model '{model_name}.pkl' not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred during prediction: {str(e)}")
    else:
        return {"error": "Invalid token"}