You need to enter to the folder where the project is located and open the terminal and execute:

# uvicorn main:app --reload

Then in another tab execute the following command for introducing data to the machine learning:

# curl -X POST http://localhost:8000/train -F file=@"/Users/jordipitarch/Desktop/real_2013_air.csv"
