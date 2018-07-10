FROM python:3.7

WORKDIR /root

COPY requirements.txt /root

RUN pip install -U setuptools pip wheel==0.31.1
RUN pip install -r requirements.txt

COPY setup.py /root
RUN pip install -e .
