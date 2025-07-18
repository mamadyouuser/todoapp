# Dockerfile کامل با پایه Alpine
FROM python:3.11-alpine

# نصب وابستگی‌های لازم برای build و runtime
RUN apk update && apk add --no-cache build-base libffi-dev

WORKDIR /app

COPY requirements.txt .

# نصب پکیج‌های پایتون
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
