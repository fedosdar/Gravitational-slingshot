# Gravitational slingshot game

The aim of this work is to create a game working with the principles of gravitational slingshot. This game uses a 
simplified model of a gravitational slingshot maneuver. Note: this is a simplified simulation. Gravity assist in real 
life is affected by a large numbers of parameters.

This project was created as part of the coursework at the Czech Technical University, Faculty of Information Technology, for the BI-PYT course.

### Used libraries:
- pygame 2.1.2 
- SDL 2.0.18
- Python 3.10.8
- numpy 1.20.1

Program was developed and tested on **Windows 10** through **Anaconda Prompt** and with **WSL**.

## Run program
First, all libraries mus be installed. Open **Anaconda Prompt** or **WSL**:
````
pip install <library_name>
````
After that it is possible to run program from root directory:
````
python -m app.src.main.py
````

## Run tests
To run tests open **Anaconda Prompt** or **WSL** and from root directory
````
python -m pytest app\
````

## Functionality
- Create simulation of the solar system and spawn spacecraft on Earth orbit
- Create simulation of random planetary system based on numpy random generator and spawn spacecraft on random unnamed 
planet
- Player can pause the game using **Pause** button
- Player can launch the spacecraft using **Velocity** button. The more distance from the staring point, the more
will be velocity
