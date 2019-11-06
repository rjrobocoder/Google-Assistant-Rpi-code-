import RPi.GPIO as board
import time
from Adafruit_IO import MQTTClient
import requests

light = 3
board.setwarnings(False)               #                                  rjrobocoder
board.setmode(board.BOARD)
board.setup(light,board.OUT)
board.setup(7,board.OUT)

ADAFRUIT_IO_USERNAME = "rjrobocoder"   #"enter username here"
ADAFRUIT_IO_KEY = "hshjhsjdhuhnbja154djdghagg"   #"enter key here"

def connected(client):
    print ('Connected to Adafruit IO!  Listening for feed changes...')
    client.subscribe('switch1') 
    
 
def disconnected(client):
    print ('Disconnected from Adafruit IO!')
    sys.exit(1)
 
def message(client, feed_id, status):
    if feed_id == 'switch1':
        
        if status == 'ON':
            print("Light 1 ON")
            board.output(light,True)
           
        elif status == 'OFF':
            print("Light 1 OFF")
            board.output(light,False)
         
        
            
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.connect()
client.loop_blocking()
