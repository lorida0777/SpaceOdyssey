#!/bin/bash

echo "🚀 Setting up Space Odyssey Game..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3 first."
    exit 1
fi

# Install required system packages for Linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "📦 Installing system dependencies for Linux..."
    sudo apt-get update
    sudo apt-get install -y \
        python3-dev \
        python3-pip \
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
        libxcursor1
fi

# Create virtual environment
echo "🔧 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "To run the game:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the game: python main.py"
echo ""
echo "Or use Docker:"
echo "docker-compose up --build"