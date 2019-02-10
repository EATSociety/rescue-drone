from pyMultiWii import pyMultiWii as MultiWii
import time

""" Throttle Hover Test """

board = MultiWii("")

def throttle(th):
        timer = 0
        start = time.time()
        while timer < 0.5:
            data = [1500,1500,2000,th]
            board.sendCMD(8,MultiWii.SET_RAW_RC,data)
            time.sleep(0.05)
            timer = timer + (time.time() - start)
start = time.time()

try:
    board.arm()
    throttle = 1050
    time.sleep(3)

    for i in range(0, 150):
        throttle(throttle)
        throttle += 1
        #print(throttle)
    
    time.sleep(10)

    for i in range(0,200):
        throttle -= 1
        #print(throttle)

except Exception as error:
    print("error")
