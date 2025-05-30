# Use the official Python 3.11 image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app (assuming your API service code is here)
COPY . .
WORKDIR /app/Tutor
# Expose the port (let’s say your API listens on 8000)
EXPOSE 8000

# Default command to run the API service (adjust based on your app)
# Example using uvicorn if you’re running a FastAPI app
# Change Directory to Tutor
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000"]
