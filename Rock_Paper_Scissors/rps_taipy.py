from taipy.gui import Gui
import utility_2
import cv2

###############################
#         CSS Section         #
###############################

my_theme = {
  "palette": {
    "background": {"default": "#808080"},
    "primary": {"main": "#a25221"}
  }
}

############################
#    Defining Variables    #
############################

content = ""
img_path = "placeholder_image.jpg"
player_choice = ""
confidence_level = 0

############################
#    Markdown for Site     #
############################

index = """
<|text-center|
# Rock, Paper, Scissors Game!
<|{"RPS_Logo.jpg"}|image|width=25vw|height=25vh|>



## Select an image from your file system 
<|{content}|file_selector|extensions=.png, .jpg, .webp|>

## OR

<|Take Picture|button|on_action=take_image|>

<|{content}|image|>

## It looks like you chose - <|{player_choice}|text|>





<|{confidence_level}% Confidence|indicator|value={confidence_level}|min=0|max=100|width=25vw|>
|>
"""

############################
#     Function Section     #
############################

# This function will update the img_path var in the state to what the user uploaded.
def on_change(state, var_name, var_val):
  if var_name == "content":
    state.content = var_val
    state.img_path = var_val
    player_choice, confidence_score = utility_2.determine_hand(var_val)
    state.player_choice = player_choice
    state.confidence_level = round(confidence_score * 100)
  # print(var_name, var_val)

def take_image(state):
  capture = cv2.VideoCapture(0)
  ret, frame = capture.read()
  capture.release()
  cv2.imwrite("playerchoice.jpg", frame)
  on_change(state, "content", "playerchoice.jpg")

app = Gui(page=index)

if __name__ == "__main__":
  # app.run(use_reloader=True, port=4001, theme=my_theme)
  app.run(use_reloader=True, port=4001)
