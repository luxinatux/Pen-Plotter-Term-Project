import pyb
import time

if __name__ == "__main__":

    pinC1 = pyb.Pin(pyb.Pin.cpu.A0, pyb.Pin.OPEN_DRAIN, value = 1)

    time.sleep(5)
    
    pinC1 = pyb.Pin(pyb.Pin.cpu.A0, pyb.Pin.OUT_PP)
    pinC1.high()
    time.sleep(5)
    
    pinC1 = pyb.Pin(pyb.Pin.cpu.A0, pyb.Pin.OUT_PP)
    pinC1.low()
    
    
    #enableA.low()
    print('ok')
    