FROM --platform=linux/amd64 python:3.10

LABEL Author="Johnny Villegas"
LABEL version="1.0"

RUN mkdir -p /api
WORKDIR /api

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]