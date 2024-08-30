# Asteroid Game

## Description
Asteroid Game is a classic arcade-style game built using the open-source Pygame library. The player controls a spaceship and must navigate through an asteroid field, avoiding collisions and shooting asteroids to survive.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Acknowledgements](#acknowledgements)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/iorellana/asteroids
    cd asteroids
    ```
2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the game:
    ```sh
    python main.py
    ```
    or run the game with the bash file that configures the venv and runs the game:

    ```sh
    ./run.sh
    ```
2. Use the arrow keys to navigate the spaceship.
3. Press the spacebar to shoot.

## Features
- [x] Real-time asteroid field generation
- [x] Player-controlled spaceship
- [x] Shooting mechanics
- [x] Collision detection
- [ ] Add sound effects
- [ ] Add a scoring system
- [ ] Implement multiple lives and respawning
- [ ] Add an explosion effect for the asteroids
- [ ] Add acceleration to the player movement
- [ ] Make the objects wrap around the screen instead of disappearing
- [ ] Add a background image
- [ ] Create different weapon types
- [ ] Make the asteroids lumpy instead of perfectly round
- [ ] Make the ship have a triangular hit box instead of a circular one
- [ ] Add a shield power-up
- [ ] Add a speed power-up
- [ ] Add bombs that can be dropped

## Acknowledgements
- Pygame library
- Boot.dev website for the tutorial [Asteroids](https://www.boot.dev/courses/build-asteroids)

