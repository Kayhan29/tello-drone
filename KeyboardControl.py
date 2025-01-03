from djitellopy import tello
import KeyPressModule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 55

    if kp.getKey("LEFT"):
        lr= -speed
    if kp.getKey("RIGHT"):
        lr= speed

    if kp.getKey("UP"):
        fb= speed
    if kp.getKey("DOWN"):
        fb= -speed

    if kp.getKey("w"):
        ud= speed
    if kp.getKey("s"):
        ud= -speed

    if kp.getKey("a"):
        yv= -speed
    if kp.getKey("d"):
        yv= speed

    if kp.getKey("q"):
        me.land()
    if kp.getKey("e"):
        me.takeoff()

    return [lr,fb, ud, yv]


while True:
    vals = getKeyInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
