
FROM python:3.11-slim

WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python application
COPY app.py .

# Run application
CMD ["python", "-u", "app.py"]
