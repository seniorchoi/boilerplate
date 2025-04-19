FROM python:3.12-slim

WORKDIR /app

# 1) copy & pip‑install your requirements.txt
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# 2) copy the rest of your source
COPY . .

# 3) make sure entrypoint runs migrations
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "wsgi:app", "--bind=0.0.0.0:8000"]
