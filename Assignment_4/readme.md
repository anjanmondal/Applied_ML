Assignment 4: Containerization & Continuous Integration [due 28 Mar 2024]
c# Containerization and Continuous Integration

## Containerization with Docker

- Create a Docker container for the Flask app created in Assignment 3.
- Create a Dockerfile with instructions to build the container:
  - Install dependencies.
  - Copy app.py and score.py.
  - Launch the app by running "python app.py" upon entry.
- Build the Docker image using the Dockerfile.
- Run the Docker container with appropriate port bindings.

## Testing with pytest

- In test.py, write a test_docker() function:
  - Launches the Docker container using command line (e.g., os.sys(..), docker build and docker run).
  - Sends a request to the localhost endpoint /score (e.g., using requests library) for a sample text.
  - Checks if the response is as expected.
  - Closes the Docker container.
- Produce a coverage report using pytest for the tests in test.py and save it in coverage.txt.

## Continuous Integration with Git

- Write a pre-commit Git hook to run test.py automatically every time you try to commit the code to your local 'main' branch.
- Copy and push this pre-commit Git hook file to your Git repository.


# References

- [Docker Curriculum](https://docker-curriculum.com/)
- [Docker Overview - Tutorialspoint](https://www.tutorialspoint.com/docker/docker_overview.htm)
- [How to Dockerize a Flask App - FreeCodeCamp](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)
- [Git Hooks](https://githooks.com/)
- [A Simple Git Hook for Your Python Projects - Giacomo Debidda](https://www.giacomodebidda.com/posts/a-simple-git-hook-for-your-python-projects/)

