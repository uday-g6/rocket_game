Overview
This is a simple 2D arcade-style game developed using Pygame. The player controls a rocket that can move in all directions and shoot bullets to destroy incoming enemies. The objective is to survive as long as possible while accumulating a high score by destroying enemies.

Game Mechanics
Player (Rocket)
  1. The player controls a rocket that can move in all four directions.
  2. The rocket can shoot bullets upwards to destroy enemies.
     
Bullets
 1. Bullets are fired from the rocket and move upwards.
 2. If a bullet hits an enemy, the bullet is removed, and the enemy's health is decreased. When an enemy's health reaches zero, the enemy is destroyed, and the player gains points.

Enemies
 1. Enemies appear at random positions from the top of the screen and move downwards.
 2. Each enemy has a health value that increases as the player's score increases, making the game progressively harder.

Controls
 1. W, UP Arrow, Numpad 8: Move up
 2. A, LEFT Arrow, Numpad 4: Move left
 3. S, DOWN Arrow, Numpad 2: Move down
 4. D, RIGHT Arrow, Numpad 6: Move right

SPACE: Fire bullets
Scoring
 1. Each enemy destroyed increases the player's score by 1.
 2. Enemy health increases at score thresholds (50, 100, 150, 200).

Setup and Execution
Prerequisites
 1. Python 3.x
 2. Pygame library

Installation
 1. Install Python 3.x from the official Python website.
 2. Install Pygame using pip: pip install pygame

Running the Game
 1. Save the game script to a file, e.g., rocket_game.py.
 2. Run the script using Python: python rocket_game.py

Code Explanation
Rocket Class
 1. Initializes the rocket's position, size, and speed.
 2. Handles movement and boundary checks.
 3. Draws the rocket on the screen as a polygon.

Bullet Class
 1. Initializes the bullet's position and speed.
 2. Handles bullet movement.
 3. Draws the bullet as a rectangle.

Enemy Class
 1. Initializes the enemy's position, size, speed, and health.
 2. Handles enemy movement.
 3. Draws the enemy as a rectangle.

Game Loop
 1. Initializes game objects and variables.
 2. Handles events and key presses for rocket movement and shooting.
 3. Updates the positions of bullets and enemies.
 4. Detects collisions between bullets and enemies, and between enemies and the rocket.
 5. Updates and displays the score and controls.
 6. Runs the main game loop with a frame rate of 30 FPS.

Exit Condition
 1. The game ends when an enemy collides with the rocket.

Additional Features
 1. The rocket fires bullets continuously when the space bar is held down.
 2. The health of enemies increases as the score increases, adding a level of difficulty as the player progresses.

Future Improvements
 1. Add sound effects for shooting and explosions.
 2. Implement different types of enemies with varying behaviors.
 3. Introduce power-ups and special abilities for the rocket.
 4. Add a high score leaderboard.

License
This game is open-source and can be modified or distributed freely. Feel free to contribute or suggest improvements!
