# rock-paper-scissors
This is an implementation using opencv, and keras, in which the model was trained using Teachable Machine by Google.

- This repo contains an application named rps_taipy.py which is created using taipy and is able to be run either locally, or could be uploaded and hosted on a server for all to use.

- This repo also contains a Rock, Paper, Scissors game, rps_game.py in which the user is challenging the computer to a competition of the best of 5 games. 

Both applications leverage the same model, with the Taipy application leveraging more-so the accuracy rating and the game looking more to facilitate the game between player and computer.

To run the taipy application, you must first install taipy on your machine. You will also need other dependencies for this codebase to work, but taipy is what will allow you to launch the site containing the application. 

```
pip install taipy
```

To run both the rps_game.py file and the rps_taipy.py file, you will need the following modules installed:

```
pip install tensorflow
pip install cv2 (this has additional requirements for you to download online)
pip install numpy
pip install pillow
pip install keras
```

Alternatively, to accomodate and facilitate the download of all of the dependencies, you can simply navigate to this repo in your command prompt/bash, identify the location of the "requirements.txt" file, and run the following command:

```
pip install -r requirements.txt
```