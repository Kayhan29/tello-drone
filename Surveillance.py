from djitellopy import tello
import KeyPressModule as kp
import time
import cv2
global img

kp.init()
me = tello.Tello()
me.connect()

print(me.get_battery())
me.streamon()

def getKeyInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 65

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
        time.sleep(3)
    if kp.getKey("e"):
        me.takeoff()

    if kp.getKey('z'):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)



    return [lr,fb, ud, yv]


while True:
    vals = getKeyInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (560, 480))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

