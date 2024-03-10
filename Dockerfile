# Use a lightweight Python image
FROM python:3.8-alpine

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app.py .
COPY index.html .

# Expose the required port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]