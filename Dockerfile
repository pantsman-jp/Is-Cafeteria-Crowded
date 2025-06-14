FROM python:3.13.3

WORKDIR /app

COPY . /app

RUN pip install flask jpholiday

CMD ["python", "app.py"]