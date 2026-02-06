FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml ./
COPY main.py tools.py ./

# Install Python dependencies via pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e .

# Create non-root user for security
RUN useradd -m -s /bin/bash agent && \
    chown -R agent:agent /app

USER agent

# Set environment variable for API key (should be passed at runtime)

# Run the agent
ENTRYPOINT ["python", "main.py"]
