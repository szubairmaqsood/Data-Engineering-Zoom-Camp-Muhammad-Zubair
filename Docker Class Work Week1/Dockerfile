# Telling our docker is based on which already exisiting image
FROM python:3.13.11-slim 

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# installing packages for our projects
#RUN pip install pandas pyarrow

# Mentioning the working directory inside docker
WORKDIR /code

COPY pyproject.toml .python-version uv.loc ./

#Installing extact libraries number
RUN uv sync locked


# Copying our code into working directory
COPY pipeline.py .

#ENTRYPOINT defines the main command that always runs when the container starts.
ENTRYPOINT ["uv", "run", "python", "pipeline.py"]