from pyMultiWii import pyMultiWii as MultiWii
#from pymultiwii import MultiWii
import time

""" Throttle Hover Test """

board = MultiWii("/dev/ttyUSB0")

def throttle(th):
        timer = 0
        start = time.time()
        while timer < 0.5:
            data = [1500,1500,1500,th]
            board.sendCMD(8,MultiWii.SET_RAW_RC,data)
            print(th)
            time.sleep(0.05)
            timer = timer + (time.time() - start)
start = time.time()

try:
    board.arm()
    th = 1050
    time.sleep(3)

    for i in range(0, 150):
        throttle(th)
        th = th + 1
        print(th)
    
    time.sleep(3)

    for i in range(0,155):
        th = th - 1
        print(th)
    board.disarm()

except Exception as error:
    print("error")
