### You need to enter to the folder where the project is located and open the terminal and execute:


    > uvicorn main:app --reload

### Then in another tab execute the following command for introducing data to the machine learning:


    > curl -X POST "http://localhost:8000/train?dataset=IRIS&model_name=IRIS"


    > curl -X POST "http://localhost:8000/train?dataset=dataStudents&model_name=students"

### Then for testing the model, it can be done using the following command:


    > curl -X POST "http://localhost:8000/predict?model_name=modelo&sepal_length=1.2&sepal_width=3.4&petal_length=5.6&petal_width=7.8"


    > curl -X POST "http://localhost:8000/predictStudents?model_name=students&Marital_status=1&Application_mode=20&Application_order=1&Course=9500&Attendance=1&Previous_qualification=1&Previous_qualification_grade=160.0&Nacionality=1&Mother_qualification=37&Father_qualification=37&Mother_occupation=9&Father_occupation=5&Admission_grade=125.5&Displaced=0&Educational_special_needs=0&Debtor=0&Tuition_fees_up_to_date=0&Gender=0&Scholarship_holder=0&Age_at_enrollment=20&International=0&Curricular_units_1st_sem_credited=0&Curricular_units_1st_sem_enrolled=6&Curricular_units_1st_sem_evaluations=6&Curricular_units_1st_sem_approved=5&Curricular_units_1st_sem_grade=12.33&Curricular_units_1st_sem_without_evaluations=0&Curricular_units_2nd_sem_credited=0&Curricular_units_2nd_sem_enrolled=6&Curricular_units_2nd_sem_evaluations=16&Curricular_units_2nd_sem_approved=6&Curricular_units_2nd_sem_grade=12.4&Curricular_units_2nd_sem_without_evaluations=0&Unemployment_rate=2.7&Inflation_rate=5.4&GDP=0.7"

