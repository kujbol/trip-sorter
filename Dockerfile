FROM python:3.7

WORKDIR /app

COPY requirements.txt /app

RUN pip install -U setuptools pip wheel==0.31.1
RUN pip install -r requirements.txt

COPY setup.py /app
RUN pip install -e .
