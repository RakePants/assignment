FROM python:3.10.12-slim

RUN addgroup --gid 10001 app_user && \
    adduser --uid 10001 --gid 10001 --disabled-password --gecos "" app_user

WORKDIR /usr/src/app

ENV PYTHONPATH=/usr/src/app/src

COPY /requirements/base.txt /requirements/

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install -r /requirements/base.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --chown=app_user:app_user . .

USER app_user

CMD ["python", "src/main.py"]