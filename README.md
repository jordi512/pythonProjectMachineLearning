### You need to enter to the folder where the project is located and open the terminal and execute:

###### uvicorn main:app --reload

### Then in another tab execute the following command for introducing data to the machine learning:

###### curl -X POST http://localhost:8000/train -F file=@"/Users/jordipitarch/Desktop/real_2013_air.csv"

### Then for testing the model, it can be done using the following command:

###### curl -X POST "http://localhost:8000/predict?sepal_length=1.2&sepal_width=3.4&petal_length=5.6&petal_width=7.8"

