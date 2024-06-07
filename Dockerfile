FROM python:3.8.4
LABEL authors="jordipitarch"

COPY . /Users/jordipitarch/Desktop/Dock
WORKDIR /Users/jordipitarch/Desktop/Dock

RUN pip3 install -r requirements.txt

ENTRYPOINT uvicorn main:app --reload