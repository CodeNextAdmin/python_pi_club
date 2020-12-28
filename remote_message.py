import anvil.server
from sense_hat import SenseHat 

sense = SenseHat()

sense.show_message("Ready")


@anvil.server.callable
def show_message(msg):
    sense.show_message(msg)

#connect to anvil server. Paste your ID below before running the script.
anvil.server.connect("PASTE_YOUR_ANVIL_UPLOAD_ID")

#prevents the script from ending
anvil.server.wait_forever()

