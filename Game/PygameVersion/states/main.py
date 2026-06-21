from menu import run_menu
from game import run_game

# Setup 
currentState = run_menu()

# Game loop checks for the state of the game 
while True:
    if currentState == "menu":
        run_menu()
    
    if currentState == "game":
        run_game()
    
