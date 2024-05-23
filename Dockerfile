# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a directory for the app
WORKDIR /app

# Install SSH server and Flask
RUN apt-get update && apt-get install -y openssh-server && \
    pip install Flask && \
    mkdir /var/run/sshd

# Copy the application files
COPY . /app

# Expose the necessary ports
EXPOSE 22 80

# Create a new user for SSH access
RUN useradd -ms /bin/bash azureuser && echo 'azureuser:password' | chpasswd

# Allow password authentication for SSH
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Copy the initialization script
COPY init.sh /usr/local/bin/init.sh
RUN chmod +x /usr/local/bin/init.sh

# Start SSH and the Flask server
CMD ["/usr/local/bin/init.sh"]
