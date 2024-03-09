FROM python:3.11.7-slim

WORKDIR /usr/src/app/

ENV PYTHONPATH=/usr/src/app/src

COPY /requirements/base.txt /requirements/

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install -r /requirements/base.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . .

ENTRYPOINT ["python", "-m", "src.main"]