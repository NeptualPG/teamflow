Features: Conda, Docker.

1: 

    mkdir teamflow
    cd teamflow

    conda create -n teamflow python=3.12 -y
    conda activate teamflow

    pip install django

    django-admin startproject config .
    python manage.py startapp accounts
    python manage.py startapp tasks
    python manage.py startapp metrics


2:
    FROM python:3.12-slim

    WORKDIR /app

    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    COPY . .

    EXPOSE 8000

    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]