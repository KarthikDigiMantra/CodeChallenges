FROM python:3.10
WORKDIR /usr/src/code_challenge
COPY ./app ./app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
