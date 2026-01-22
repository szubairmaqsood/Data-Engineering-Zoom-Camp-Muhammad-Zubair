# Telling our docker is based on which already exisiting image
FROM python:3.13.11-slim 

# installing packages for our projects
RUN pip install pandas pyarrow

# Mentioning the working directory inside docker
WORKDIR /code

# Copying our code into working directory
COPY pipeline.py .

#ENTRYPOINT defines the main command that always runs when the container starts.