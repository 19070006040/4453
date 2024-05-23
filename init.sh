#!/bin/bash

# Start the SSH service
service ssh start

# Start the Flask application
python /app/app.py

# Keep the container running
tail -f /dev/null
