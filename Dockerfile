FROM python:3.10

RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

WORKDIR /src