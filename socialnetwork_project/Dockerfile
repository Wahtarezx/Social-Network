FROM python:latest

WORKDIR /python

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8001

COPY . .

CMD ["python", "manage.py", "runserver"]
