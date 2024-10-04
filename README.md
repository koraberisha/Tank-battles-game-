# Tank Battles Game

A **2D tank battle** game featuring **Player vs Player** or **AI-controlled** opponents, built using Python and Pygame.

## Overview

This is a retro-styled tank battle game where two players (or a player vs AI) battle on various maps using projectile-firing tanks. It’s designed to be fun with simple game mechanics, and while it is built on an older version of Pygame (from 2017), it still provides a functional gameplay experience.

The core objective is to aim and fire shells at the opposing tank to destroy it while avoiding enemy fire. Tanks can move around the screen, adjust their firing angles, and manage power settings.

## How It Works

### Game Structure

The game runs mainly from the `Tanks_main.py` script, which initializes the game environment and handles core mechanics such as:
- **Menu Navigation**: Allows players to choose between maps and set up the game mode (Player vs Player or Player vs AI).
- **Tank Initialization**: Each player or AI has its tank created through the `tank.py` module, which defines the tank’s position, movement, and firing mechanics.

### Main Components

1. **Tank Movement and Firing (tank.py)**: 
   Each tank can move left and right and has the ability to fire shells at various angles. The firing of shells is handled with basic projectile physics, taking into account the angle of fire and the power behind the shot:
   ```python
   def fire_shell(self, angle, power):
       # Calculate projectile motion
       ...
   ```
   The shell explodes upon impact, and collision detection checks if it hits the enemy tank.

2. **Projectile Motion (proj_motion.py)**:
   The `proj_motion.py` file calculates the motion of fired shells. The trajectory is computed based on the initial velocity, angle, and gravity to simulate realistic arc-like movement.

3. **AI Behavior (ai.py)**:
   The AI-controlled tanks are designed with basic logic to move and shoot at the player. The AI evaluates the player's position and adjusts its firing angle accordingly:
   ```python
   def ai_move(self):
       # AI logic to move tank and decide firing angle
       ...
   ```

4. **Slider (slider.py)**:
   This module implements a slider that players use to adjust variables such as the firing angle and power of their shots. It allows for dynamic gameplay, where the user can fine-tune their attack strategies.

5. **Menu and Level Selection**:
   The `game_initiate` class inside `Tanks_main.py` handles the game's menu, allowing players to choose between maps and modes. The maps are loaded as image assets, and the selection process is managed through mouse input.

### Key Features

- **Player vs Player Mode**: Two players battle on the same device, taking turns to move and fire.
- **AI Mode**: Face off against an AI opponent with basic decision-making abilities.
- **Level Selection**: Multiple levels (maps) to choose from, each with different terrain features.
- **Power and Angle Control**: Sliders allow players to adjust the power and angle of their shots to improve aim and strategy.
- **Leaderboard**: High scores are stored in the game, rewarding the best-performing players in PvP mode.

## Installation

1. Install Python (version 3.6+ recommended).
2. Install the Pygame library:
   ```bash
   pip install pygame
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/koraberisha/Tank-battles-game-.git
   ```
4. Navigate to the project folder:
   ```bash
   cd Tank-battles-game-
   ```
5. Run the main game script:
   ```bash
   python Tanks_main.py
   ```

## Gameplay Instructions

- **Move**: Use the arrow keys or `WASD` to move the tank.
- **Fire**: Press the spacebar to fire.
- **Adjust Power/Angle**: Use the on-screen sliders to fine-tune your shots before firing.

## Contributing

Contributions are welcome! Feel free to open issues, fork the project, or submit pull requests. Improvements could include updating Pygame, refining AI logic, or adding new maps.

