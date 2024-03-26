# Use the official Python image as the base image
FROM python:3.12.2

# Set the working directory in the container
WORKDIR /app

# Copy the required files to the container
COPY requirements.txt .
COPY src/score.py .
COPY src/app.py .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]