# Bobble Refactor
Refactoring cavern from Code the Classics repository

## How to run

1. Create a venv
```powershell
python -m venv venv
```

2. Activate the venv
```powershell
./venv/Scripts/Activate.ps1
```

3. Install the requirements
```powershell
pip install -r ./requirements.txt
```

4. Run from root folder
```powershell
python -m pgzero main.py
```

## Controls

| Action | Key |
| :--- | :--- |
| **Move Left** | Left Arrow |
| **Move Right** | Right Arrow |
| **Jump** | Up Arrow |
| **Fire Bubble** | Spacebar |
| **Pause Game** | P |

## Class Structure

### App Classes
* **`App`**: The context manager. Stores the `active_screen`.
* **`InputHandler`**: Tracks previous key states to detect "just pressed" vs "held" events.

### Screen Classes
* **`MenuScreen`**: Simple title screen waiting for input.
* **`PlayScreen`**: Wraps the `Game` instance. Handles the lifecycle of a game session.
* **`PauseScreen`**: Wraps the `PlayScreen` to halt logic updates while still drawing the frozen game behind the pause menu.

### Game Entities (`src/game.py`)
* **`Game`**: The "World". Holds the level grid, lists of actors, and handles level transitions.
* **`CollideActor`**: A custom extension of `Actor` that handles grid-based collision detection.
* **`GravityActor`**: Inherits from `CollideActor`. Adds `vel_y` and gravity logic.
    * **`Player`**: The user-controlled character.
    * **`Robot`**: AI enemies with basic pathfinding/direction changing.
    * **`Fruit`**: Collectibles with gravity.
* **`Orb`**: The projectile fired by the player. Handles trapping logic.