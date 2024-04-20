# Use the specific Python runtime as a parent image
FROM python:3.11.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt ./requirements.txt

# Install PortAudio library
RUN apt-get update && apt-get install -y portaudio19-dev

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application's code into the container at /app
COPY ./src ./src

# At runtime, the current directory will be /app, so set the paths accordingly
CMD ["python", "./src/scheduler.py"]
