#!/usr/bin/env python3
"""
Web launcher for Space Odyssey game.
This script provides a web-friendly entry point for the game.
"""

import os
import sys
from kivy.config import Config

# Configure for web deployment
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'resizable', '1')

# Set web-friendly audio backend
try:
    from kivy.core.audio import SoundLoader
    # Enable web audio if available
    Config.set('audio', 'gstreamer', '0')
except ImportError:
    print("Warning: Audio support may be limited in web environment")

def main():
    """Main entry point for web deployment."""
    try:
        # Import and run the game
        from main import Space_OdysseyApp
        app = Space_OdysseyApp()
        app.run()
    except Exception as e:
        print(f"Error starting game: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()