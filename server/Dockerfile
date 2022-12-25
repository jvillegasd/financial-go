FROM python:3.7 

LABEL Author="Johnny Villegas"
LABEL version="1.0"

RUN mkdir -p /src
WORKDIR /src

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]