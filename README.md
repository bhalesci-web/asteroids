# Asteroids OOP Tutorial

A small Python project built with `pygame` to explore object-oriented programming using an Asteroids-style game.

## What you'll learn

- organizing game logic into classes
- representing game entities with objects like `Player`
- using inheritance and reusable shape behavior
- drawing with `pygame` and updating game state each frame

## Project structure

- `main.py` — game entry point and loop
- `player.py` — `Player` class that handles ship drawing and behavior
- `constants.py` — screen and object settings
- `circleshape.py` — base shape support for game objects
- `logger.py` — simple state logging for debugging

## Run the game

1. Install dependencies:
   ```bash
   python3 -m pip install pygame
   ```
2. Run:
   ```bash
   python3 main.py
   ```

## Notes

This project is designed as a learning example rather than a complete game. It focuses on structuring a small game using classes and simple object-oriented design.
