# Use Python 3.13.1 base image (official image not released as of Apr 2025)
FROM python:3.13.1-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Run your script
CMD ["python", "main.py"]

#Run Docker Command
#docker build -t midiutil-app .
#docker run --rm -v $(pwd):/app midiutil-app
