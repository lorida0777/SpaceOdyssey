# 🚀 Space Odyssey  Space Tunnel Runner

A thrilling 3D space tunnel runner game built with Python and Kivy. Navigate your ship through an endless tunnel, avoid obstacles, and achieve the highest score!

## ✨ Features

- ** Perspective Graphics**: Beautiful perspective-transformed tunnel environment
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

## 🛠️ Installation 

###  Recommended

```bash
# Clone the repository
git clone github.com/lorida0777/SpaceOdyssey
cd SpaceOdyssey



# Activate virtual environment and play
source venv/bin/activate
python main.py
```


## 📁 Project Structure

```
SpaceOdyssey/
├── main.py              # Main game engine and logic
├── menu.py              # Menu widget implementation
├── user_actions.py      # Input handling (keyboard/touch)
├── transforms.py        # 3D perspective transformations
├── menu.kv             # Menu UI layout (Kivy)
├── space_odyssey.kv    # Main game UI layout (Kivy)
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


# Game parameters
SPEED = .9              # Tunnel speed
SPEED_X = 3.0          # Ship movement speed
V_NB_LINES = 10        # Vertical lines count
H_NB_LINES = 8         # Horizontal lines count
NB_TILES = 16          # Number of obstacle tiles


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


## 🙏 Acknowledgments

- Built with [Kivy](https://kivy.org/) - Open source Python framework
- Audio assets and visual design inspired by retro space games
- 3D perspective mathematics adapted from classic tunnel games

---

**Ready to embark on your Space Odyssey? 🚀**
