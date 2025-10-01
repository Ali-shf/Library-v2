# Stage 1: Base build image
FROM python:3.12-slim AS builder

# Create the app directory
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Set the environment variables to optimize Python
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Prevents Python from buffering stdout and stdin
ENV PYTHONUNBUFFERED=1


# Install Python dependencies for caching benefits
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


# Stage 2: Production stage
FROM python:3.12-slim


# Install system dependencies: curl, Node.js, npm, Postgres client
RUN apt update && apt install -y \
    curl \
    postgresql-client \
    && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt install -y nodejs \
    && npm install -g npm@latest \
    && rm -rf /var/lib/apt/lists/*


RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app


# Copy Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Set the working directory
WORKDIR /app

# Copy application code --chown=appuser:appuser
COPY . .


# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 


# Switch to non-root user
# USER appuser

# Expose the application port
EXPOSE 8000

# Make entry file executable
RUN chmod +x /app/entrypoint.prod.sh

# Start the application using Gunicorn
CMD [ "/app/entrypoint.prod.sh" ]






