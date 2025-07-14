#!/bin/bash

echo "🚀 Setting up SpaceOdyssey for online play..."

# Check if pip is available
if command -v pip &> /dev/null; then
    echo "📦 Installing dependencies..."
    pip install kivy
elif command -v pip3 &> /dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install kivy
else
    echo "❌ pip not found. Please install pip first."
    exit 1
fi

echo "🎮 Starting SpaceOdyssey..."
python main.py || python3 main.py

echo "✨ Thanks for playing SpaceOdyssey!"