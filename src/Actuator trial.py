import pyb
import time

if __name__ == "__main__":

    enableA = pyb.Pin(pyb.Pin.cpu.C1, pyb.Pin.OUT_PP) #set pin to open drain output7
    enableA.high()
    time.sleep(10)
    #enableA.low()
    print('ok')
    