# Use the official Python image from DockerHub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 for the API service and 8000 for metrics
EXPOSE 5000
EXPOSE 8000

# Command to run the Flask app
CMD ["python", "app.py"]
