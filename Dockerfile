FROM python:3.8

WORKDIR /tests
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt && yes | pip install -U selenium

COPY tests/testPassArguments/test_pass_arguments.py .
COPY tests/conftest.py .

CMD ["pytest", "./test_pass_arguments.py", "--user=user1", "--password=00000"]