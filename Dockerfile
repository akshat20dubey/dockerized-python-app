# Step 1 - Use official Python base image
FROM python:3.10-slim

# Step 2 - Set working directory inside container
WORKDIR /app

# Step 3 - Copy our Python script into container
COPY app.py .

# Step 4 - Install required libraries
RUN pip install requests

# Step 5 - Run the script when container starts
CMD ["python", "app.py"]
