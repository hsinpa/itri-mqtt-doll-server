FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY main.py main.py
COPY ./src /code/src

EXPOSE 8842

CMD ["python", "main.py"]
