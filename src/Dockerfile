# python3.11 slim used, as 3.11 is compatible with all of the libraries used
# and slim, because a smaller docker image is usually preferred for performance
# and storage.
FROM python:3.11-slim

# assign a working directory for further actions
WORKDIR /app

# copy the requirements file over, then install the dependencies with pip.
# no-cache-dir is used, as a cache takes space - and this is the only project
# in this container, making use of these requirements.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy across the rest of the project directory, including the app repo,
# into the working directory, /app
COPY . .

# run uvicorn, targetting the main:app as the entry point,
# making the host as localhost(0.0.0.0) and the port as 8000.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
