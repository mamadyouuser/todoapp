FROM python:3.11-slim

WORKDIR /app

# آپدیت و ارتقا بسته‌ها
RUN apt-get update && apt-get upgrade -y

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
