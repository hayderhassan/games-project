# games-project
PYTHON GAMES PROJECT

This is a project to build a 2D platform scroller game in Python. This game will be modelled on the Mario games.

After starting the program, the user will be greeted by the home screen. On this screen they can read the instructions on how to play the game. They have the option to start a new game or exit.

In a new game, the character starts with 3 lives and a score of 0. They must move towards the right of the screen and use platforms to jump around.

The more the character travels, the higher his score will be. Points are also scored by collecting coins.

The character must avoid enemies. Contact with an enemy will result in the character losing a life. The game will then start again, continuing from the current score minus a 10% penalty. After dying 3 times, the game will be over.

Once the game is over, the game over screen will appear and show the final score. From here, the user can either start a new game, return to the home screen or exit.

During gameplay, the game can be paused at any time by pressing the "P" button. This will show the pause menu and give the user the choice to continue with the game, restart the game (which resets score to 0 and lives to 3), return to the home screen or exit the program.

The game will keep a record of the high score which will be displayed on the home screen, during gameplay and on the game over screen.

The game will be made up of 5 levels. After reaching a certain distance, the level will end and the game will continue to the next level. Once the user completes all levels, they will be shown the game over screen congratulating them on completing the game.

===============
Setup

1) Make sure you have pygame and SimpleGui installed:
    sudo apt-get install python-pygame
    sudo easy_install simplegui
  
2) Run main.py

3) Enjoy!
