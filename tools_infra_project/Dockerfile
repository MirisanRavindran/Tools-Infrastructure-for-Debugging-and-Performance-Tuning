# Use Python 3.8 base image
FROM python:3.8-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's code
COPY . .

# Define the entry point for the application
CMD ["python", "app.py"]
