FROM python:3.10

RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /src