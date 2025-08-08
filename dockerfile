# Start from python base image
FROM python:3.13-slim
# Working directory
WORKDIR /app
# Copy req into the image
COPY requirements.txt .
# Install Python packages
RUN apt-get update && \
    # Install netcat utility
    apt-get install -y netcat-traditional && \
    # Install all requiremnts
    pip install -r requirements.txt && \
    # Cleanup list from class
    rm -rf /var/lib/apt/lists
# Copy the rest of the code now that dependenceis are ready
COPY . .
# Container runs script on start
ENTRYPOINT ["/app/entrypoint.sh"]

