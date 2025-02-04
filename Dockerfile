# Base image
FROM python:3.10.0b3-alpine3.14

# Set working directory
WORKDIR /app

# Copy required files from the 'app' folder
COPY app/app.py app/requirements.txt /app/
COPY app/templates /app/templates
COPY app/static /app/static

# Install dependencies & system packages
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev \
    && pip3 install --no-cache-dir -r requirements.txt

# Set Flask environment
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Expose the application port
EXPOSE 8080

# Use Gunicorn for production
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
