from taipy.gui import Gui 
import utility
import rps_game

user_image = "playerchoice.jpg"

def determine_hand():
  utility.determine_hand(user_image).strip()

def play_game():
  rps_game.play_game()

index = """
<|text-center|
<|{"logo.jpg"}|image|height=250|width=300|>

Hold up Rock, Paper, or Scissors (with your hand) to the camera and press here!
<|Take Picture|button|on_action=determine_hand|>

### Your choice:
<|{user_image}|image|>
|>

<|{player_hand}|text|>
"""

# <|{user_image}|file_selector|>
# Select an image of Rock, Paper, or Scissors from your file system.


gui = Gui(page=index)
# gui.run(stylekit=False)

if __name__ == "__main__":
  app.run(use_reloader=True)