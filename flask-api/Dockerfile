# Use lightweight version of Python 3.11
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy the requirements.txt
COPY requirements.txt requirements.txt

# Install the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all remaining project files into the container
COPY . .

# Expose port for Flask
EXPOSE 8080

# Set the command to run the Flask app
CMD ["python", "app.py"]