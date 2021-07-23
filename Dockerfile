FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY code/requirements.txt .
RUN pip install -r requirements.txt
COPY ./code .
