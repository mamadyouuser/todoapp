# backend/Dockerfile
FROM python:3.11-alpine

# نصب وابستگی‌ها برای build پکیج‌ها
RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    gcc \
    musl-dev \
    python3-dev \
    cargo \
    linux-headers

WORKDIR /app

COPY requirements.txt .

# نصب پکیج‌های پایتون
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# اجرا
CMD ["python", "app.py"]
