# python_pi_club
This is the repo for the Code Next Connect club - Python on the Pi
You will need a Raspberry Pi (3, 4, 400) and a Sense HAT unit.

## Install libraries
In your Terminal, run these commands to install the necessary libraries:

#### Sense Hat
```bash
$ sudo apt-get update
$ sudo apt-get install sense-hat
$ sudo reboot

```
#### Anvil
```bash
$ sudo pip3 install anvil-uplink

```
This course will use Python 3, so make sure to use pip3 above. 
## What's in the Repo?
Starter files for the Python on Pi Club, as well as fully-built examples. There are also some warm-ups and basic challenges.

## Memory
The first game, introduced in session 1. The objective is to reproduce the sequence of the arrows by moving the Sense HAT joystick. The game should increase in difficulty with each level by adding more steps to the sequence. 

#### Extensions
- Add more animations.
- Play sound when the user guesses right, or loses game, for example (must wear headphones, or connect to a TV/monitor).

## Remote Message
Remote message is a sample app to demo the Anvil service. The **remote_message.py** file uses the Anvil unplik service and acts as the server, allowing web clients to access the Pi through it's exposed methods, which are flagged with the @anvil.server.callable decorator. In order to run this demo, you must also clone the client web app [Remote App](https://anvil.works/build#clone:XVB2OIJR2V4DT5Y2=4SQ25RYVZG45OFIU7IXI6KA6)

Once cloned, you must enable the Uplink and get your own unique ID. Click on the Gear menu and choose Uplink:
![Uplink Menu](https://anvil.works/learn/tutorials/img/raspberry-pi/uplink-gear-menu.png)


Then Enable the Uplink to get your unique ID:
![Uplink Enable](https://anvil.works/learn/tutorials/img/raspberry-pi/enable-uplink.png)

Now in your Raspberr Pi, with this repo cloned, edit the **remote_message.py** file to include this new ID:

```python
@anvil.server.callable
def show_messgage(message):
    sense.show_message(message)

anvil.server.connect("REPLACE_WITH_YOUR_OWN_UPLINK_ID")

```

Make sure to save and Run the app on the Raspberry Pi first before runnign the Anvil Web app.
