FROM python:3.11.10-slim
WORKDIR /app
COPY config_check.py .
CMD ["python", "config_check.py"]