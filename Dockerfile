# Use Python as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your reviewer script into the container
COPY reviewer.py .

# Set the default command to run your script
ENTRYPOINT ["python", "reviewer.py"]
