FROM python:3.7

LABEL authors="rbezugly"

RUN mkdir /todo_app

WORKDIR /todo_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "main:app"]