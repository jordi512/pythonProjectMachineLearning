# ML API

In this git, is programmed a Machine learning API using python as the main language, with some interactions with Mariadb for the Login and usage of jwt for the cookies. It is also available a Docker file to facilitate the download of all the python libraries and a pdf explaining the main code.

First of all is important to download Mariadb or the database you prefer. To change the DB parameters, you have to go to the "user.py" file.

### Dockerfile

    # docker build -t simple_app .


### MariaDB configuration (in last version MongoDB is implemented):

    # mariadb
    MariaDB [(none)]> CREATE DATABASE python;
    MariaDB [(none)]> USE python;
    MariaDB [python]> CREATE TABLE login (
    ->   user VARCHAR(255) NOT NULL,
    ->   password VARCHAR(255) NOT NULL
    -> );

    MariaDB [python]> ALTER TABLE login ADD PRIMARY KEY (user);

    MariaDB [python]> ALTER TABLE login MODIFY COLUMN password VARCHAR(60) NOT NULL;

    MariaDB [python]> INSERT INTO login (user, password) VALUES ('Jordi', 'Jordi');

    MariaDB [python]> ALTER USER 'root'@'localhost' IDENTIFIED BY 'nueva_contraseña';

    MariaDB [python]> FLUSH PRIVILEGES;

### You need to enter to the folder where the project is located and open the terminal and execute:


    # uvicorn main:app --reload

    
### You need to login with your user and your password and ensure that Mariadb is running:


    # curl -X POST "http://localhost:8000/login?username=Jordi&password=Jordi" 


### Then you can start making the machine learning models or seeing the datasets that are inside the folder "datasets":


    # curl -X GET "http://localhost:8000/viewDataSet?dataset=IRIS" 


    # curl -X POST "http://localhost:8000/train?dataset=IRIS&model_name=IRIS"


    # curl -X POST "http://localhost:8000/train?dataset=dataStudents&model_name=students"


    # curl -X POST "http://localhost:8000/train?dataset=winequality&model_name=wine"


### Then for testing the model, it can be done using the following command:


    # curl -X POST "http://localhost:8000/predictIRIS?model_name=IRIS&sepal_length=1.2&sepal_width=3.4&petal_length=5.6&petal_width=7.8"


    # curl -X POST "http://localhost:8000/predictStudents?model_name=students&Marital_status=1&Application_mode=20&Application_order=1&Course=9500&Attendance=1&Previous_qualification=1&Previous_qualification_grade=160.0&Nacionality=1&Mother_qualification=37&Father_qualification=37&Mother_occupation=9&Father_occupation=5&Admission_grade=125.5&Displaced=0&Educational_special_needs=0&Debtor=0&Tuition_fees_up_to_date=0&Gender=0&Scholarship_holder=0&Age_at_enrollment=20&International=0&Curricular_units_1st_sem_credited=0&Curricular_units_1st_sem_enrolled=6&Curricular_units_1st_sem_evaluations=6&Curricular_units_1st_sem_approved=5&Curricular_units_1st_sem_grade=12.33&Curricular_units_1st_sem_without_evaluations=0&Curricular_units_2nd_sem_credited=0&Curricular_units_2nd_sem_enrolled=6&Curricular_units_2nd_sem_evaluations=16&Curricular_units_2nd_sem_approved=6&Curricular_units_2nd_sem_grade=12.4&Curricular_units_2nd_sem_without_evaluations=0&Unemployment_rate=2.7&Inflation_rate=5.4&GDP=0.7"


    # curl -X POST "http://localhost:8000/predictWine?model_name=wine&fixed_acidity=5&volatile_acidity=0.2&citric_acid=0.2&residual_sugar=1&chlorides=40&free_sulfur_dioxide=40&total_sulfur_dioxide=40&density=1&pH=3&sulphates=0.4&alcohol=8&quality=6"
