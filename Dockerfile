# Use the official Python image
FROM python:3.11.7-alpine3.18

# Set the working directory
WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
