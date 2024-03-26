import os
import subprocess
import requests
import pytest
import time
import sys
from urllib.parse import urljoin

# Add the path to the folder containing score.py and app.py to the Python path
sys.path.append("G:/Coursework/AML/Assignment/A4/src")

# Import the modules
from score import score
from app import app

# Define a pytest fixture to start and stop the Docker container
@pytest.fixture(scope="module")
def docker_container():
    # Build Docker image
    subprocess.run(["docker", "build", "-t", "flask-app", "."], check=True)

    # Run Docker container in detached mode
    container_id = subprocess.check_output(["docker", "run", "-d", "-p", "5000:5000", "flask-app"]).decode().strip()

    # Wait for container to start
    time.sleep(2)

    yield container_id

    # Clean up: Stop and remove the Docker container
    subprocess.run(["docker", "stop", container_id], check=True)
    subprocess.run(["docker", "rm", container_id], check=True)

# Test the Docker container
def test_docker_app(docker_container):
    # Define the base URL of the Docker container
    base_url = "http://localhost:5000"
    
    # Define the endpoint for scoring
    score_endpoint = "/score"
    
    # Construct the full URL
    url = urljoin(base_url, score_endpoint)
    
    # Test the Flask app running inside the Docker container
    payload = {'text': 'Test text'}
    response = requests.post(url, json=payload)
    data = response.json()

    # Assertions
    assert response.status_code == 200
    assert 'prediction' in data
    assert 'propensity' in data
    assert isinstance(data['prediction'], bool)
    assert isinstance(data['propensity'], float)

    print('Docker container test passed successfully.')

if __name__ == "__main__":
    pytest.main([__file__])
