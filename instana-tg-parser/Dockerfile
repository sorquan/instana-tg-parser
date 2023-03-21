FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt app.py ./
RUN pip3 install -r requirements.txt

CMD ["python3","app.py"]