import pyb
import time

if __name__ == "__main__":

    pin_sol = pyb.Pin(pyb.Pin.cpu.A9, pyb.Pin.OPEN_DRAIN, value = 1)

    time.sleep(5)
    
    pin_sol = pyb.Pin(pyb.Pin.cpu.A9, pyb.Pin.OUT_PP)
    pin_sol.high()
    time.sleep(5)
    
    pin_sol = pyb.Pin(pyb.Pin.cpu.A9, pyb.Pin.OUT_PP)
    pin_sol.low()
    
    
    #enableA.low()
    print('ok')
    