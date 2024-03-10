# Use a lightweight Python image
FROM arm64v8/python:3.13.0a4-bookworm

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip setuptools && pip install -r requirements.txt

# Copy the application files
COPY app.py .
COPY index.html .

# Expose the required port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]