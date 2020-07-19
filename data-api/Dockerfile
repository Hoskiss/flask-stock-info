FROM ubuntu:18.04

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY app /app

WORKDIR /app

ENTRYPOINT ["python", "app.py"]