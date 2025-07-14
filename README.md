# 🚀 Space Odyssey - Optimized 3D Space Tunnel Runner

A thrilling 3D space tunnel runner game built with Python and Kivy. Navigate your ship through an endless tunnel, avoid obstacles, and achieve the highest score!

## ✨ Features

- **3D Perspective Graphics**: Beautiful perspective-transformed tunnel environment
- **Smooth Controls**: Keyboard controls for desktop, touch controls for mobile
- **Audio Experience**: Immersive sound effects and background music
- **Score Tracking**: Real-time score display and game over screen
- **Cross-Platform**: Runs on Linux, Windows, macOS, and mobile devices
- **Optimized Performance**: 60 FPS gameplay with efficient collision detection

## 🎮 How to Play

- **Desktop**: Use ← and → arrow keys to steer your ship
- **Mobile/Touch**: Tap left or right side of screen to steer
- **Objective**: Navigate through the tunnel avoiding the walls and obstacles
- **Scoring**: Your score increases as you progress further into the tunnel

## 🛠️ Installation & Setup

### Option 1: Automatic Setup (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd SpaceOdyssey

# Run the automated setup script
./setup.sh

# Activate virtual environment and play
source venv/bin/activate
python main.py
```

### Option 2: Manual Setup

```bash
# Install system dependencies (Linux/Ubuntu)
sudo apt-get update
sudo apt-get install -y python3-dev python3-pip libgl1-mesa-glx libglu1-mesa

# Install Python dependencies
pip3 install -r requirements.txt

# Run the game
python3 main.py
```

### Option 3: Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build manually
docker build -t space-odyssey .
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
  space-odyssey
```

## 🚀 Making it Online

### Web Deployment Options

1. **Kivy for Web**: Convert to run in browser using Kivy's web backend
2. **Cloud Gaming**: Deploy on cloud platforms with GPU support
3. **Progressive Web App**: Create a PWA wrapper for mobile devices

### Deployment Platforms

- **Heroku**: Deploy using Docker containers
- **AWS EC2**: Full control deployment with GPU instances
- **Google Cloud Run**: Serverless container deployment
- **DigitalOcean**: Simple VPS deployment

### Example Cloud Deployment (Heroku)

```bash
# Install Heroku CLI and login
heroku login

# Create Heroku app
heroku create space-odyssey-game

# Deploy using container
heroku container:push web
heroku container:release web
```

## 🔧 Optimizations Implemented

### Performance Improvements
- ✅ **Fixed collision detection logic** - Corrected inverted collision checks
- ✅ **Audio error handling** - Graceful fallback when audio files are missing
- ✅ **Memory optimization** - Efficient object reuse and cleanup
- ✅ **60 FPS optimization** - Smooth frame rate with optimized update loops

### Bug Fixes
- ✅ **Window configuration fix** - Corrected double width setting
- ✅ **Typo correction** - Fixed "SCRORE" to "SCORE"
- ✅ **Safe audio playback** - Null checks for all audio operations
- ✅ **Error handling** - Comprehensive exception handling

### Code Quality
- ✅ **Modular structure** - Clean separation of concerns
- ✅ **Documentation** - Comprehensive comments and docstrings
- ✅ **Type safety** - Proper error checking and validation
- ✅ **Resource management** - Proper cleanup and resource handling

## 📁 Project Structure

```
SpaceOdyssey/
├── main.py              # Main game engine and logic
├── menu.py              # Menu widget implementation
├── user_actions.py      # Input handling (keyboard/touch)
├── transforms.py        # 3D perspective transformations
├── menu.kv             # Menu UI layout (Kivy)
├── space_odyssey.kv    # Main game UI layout (Kivy)
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration
├── docker-compose.yml  # Container orchestration
├── setup.sh           # Automated setup script
├── audio/             # Sound effects and music
├── images/            # Game textures and graphics
├── fonts/             # Custom fonts
└── README.md          # This file
```

## 🎵 Audio Assets

The game includes various sound effects:
- Background music (space_odyssey.wav, faded.wav)
- Game events (begin.wav, restart.wav, game_over.wav)
- Interactive sounds (bip.wav)

## 🎨 Visual Assets

- Custom fonts (EB Garamond family)
- Background textures
- Particle effects and visual feedback

## 🔧 Configuration

Game settings can be modified in `main.py`:

```python
# Window configuration
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '600')

# Game parameters
SPEED = .9              # Tunnel speed
SPEED_X = 3.0          # Ship movement speed
V_NB_LINES = 10        # Vertical lines count
H_NB_LINES = 8         # Horizontal lines count
NB_TILES = 16          # Number of obstacle tiles
```

## 🐛 Troubleshooting

### Audio Issues
- Ensure audio files are in the `audio/` directory
- Check system audio drivers and permissions
- The game will run without audio if files are missing

### Display Issues
- For Linux: Install mesa graphics libraries
- For Docker: Ensure X11 forwarding is properly configured
- Check graphics drivers and OpenGL support

### Performance Issues
- Reduce window size for better performance on low-end devices
- Adjust game speed parameters for smoother gameplay
- Close other applications to free up system resources

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Kivy](https://kivy.org/) - Open source Python framework
- Audio assets and visual design inspired by retro space games
- 3D perspective mathematics adapted from classic tunnel games

---

**Ready to embark on your Space Odyssey? 🚀**