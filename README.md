# Gravitational slingshot game

The aim of this work is to create a game working with the principles of gravitational slingshot. This game uses a 
simplified model of a gravitational slingshot maneuver. Note: this is a simplified simulation. Gravity assist in real 
life is affected by a large numbers of parameters.

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

## Controls

![Main menu](https://gitlab.fit.cvut.cz/BI-PYT/B221/fedosdar/-/raw/semestral/images/PYT1.png)

- To start a new simulation in **solar system** press **"Solar system"**
- To start a new simulation in **random system** press **"Random system"**
- To exit the game press **"Exit"**

![Game field](https://gitlab.fit.cvut.cz/BI-PYT/B221/fedosdar/-/raw/semestral/images/PYT2.png)
- To exit to **main menu** press **"Exit"**
- To **pause** the game press **"Pause"**. To *unpause* the game press the same button
- To set *velocity* of the spacecraft press **"Velocity"**. Note, that the game will be automatically paused. To set 
velocity pick any point at screen with mouse and press **left mouse button**. The game will be automatically resumed
