FROM python:3.8

WORKDIR /code
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt && yes | pip install -U selenium

COPY src/ .

CMD ["pytest", "./test_values.py"]