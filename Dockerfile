FROM python:3.13.3

WORKDIR /app

COPY . /app

RUN pip install flask jpholiday

# RUN python init_db.py

CMD ["python", "app.py"]