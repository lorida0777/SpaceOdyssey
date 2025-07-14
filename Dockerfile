# Use Python 3.9 slim image
FROM python:3.9-slim

# Install system dependencies for Kivy
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglu1-mesa \
    libxrandr2 \
    libxss1 \
    libgconf-2-4 \
    libasound2-dev \
    libpulse-dev \
    libx11-6 \
    libxext6 \
    libxi6 \
    libxrender1 \
    libxinerama1 \
    libxcursor1 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxcb1 \
    libxcb-glx0 \
    libxcb-render0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-shm0 \
    libxcb-xfixes0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set environment variables for display
ENV DISPLAY=:0
ENV KIVY_WINDOW=sdl2

# Expose port for web version (if needed)
EXPOSE 8080

# Run the application
CMD ["python", "main.py"]