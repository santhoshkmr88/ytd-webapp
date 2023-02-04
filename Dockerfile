FROM python:3.8

WORKDIR /app

COPY app.py /app
COPY requirements.txt /app
COPY readme.md /app
COPY templates /app/templates
COPY static /app/static

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python", "app.py" ]

