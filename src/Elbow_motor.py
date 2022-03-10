"""!
    @file           main.py
    @brief          Practice Control with Elbow Motor 131:1 gear ratio
    @details        Implements a closed loop P-Only controlled step response of a motor with a specified gain value and steady state value.
                    This file is to be put on the Nucleo, and upon restart of the nucleo, it should run this file.
    @author         Dylan Ruiz
    @author         Lucas Martos-Repath
"""
import motor_Ruiz_Martos
import encoder_Ruiz_Martos
import closedloop
import time
import pyb



def main():
        '''!
            @brief                  Initializes hardware and runs the step response.        
            @details                Initializes the encoders and motor, and also creates a motor, encoder and a closed loop object
                                    to run the drivers.
            @param Gain             The proportional gain of the closed-loop controller. 
                    
        '''
        enableA = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_PP)
        in1_mot = pyb.Pin(pyb.Pin.cpu.B4)
        in2_mot = pyb.Pin(pyb.Pin.cpu.B5)
        motor1 = motor_Ruiz_Martos.Motor(enableA,in1_mot,in2_mot,3) # motor in A
        motor1.enable()
        in1_enc = pyb.Pin(pyb.Pin.cpu.B6)
        in2_enc = pyb.Pin(pyb.Pin.cpu.B7)
        encoder1 = encoder_Ruiz_Martos.Encoder(in1_enc,in2_enc,4) # motor in A
        Closed_loop = closedloop.ClosedLoop(0.5, 0)
        time_start = time.ticks_ms()
        
        time_period = 10 #specifying that the interval we want is 10s
        step = 24500/4 #Specifying that the desired output is 4000 ticks
        time_next = 0
        
        while True:
            time_now = time.ticks_diff(time.ticks_ms(),time_start)
            if time_now >= time_next:
                time_next = time.ticks_add(time_next,time_period)
                encoder1.update()
                motor1.set_duty(Closed_loop.update(step,encoder1.get_position()))
                print(encoder1.get_position())
            
            if time_now >= 5000:
                Closed_loop.print_lists()
                motor1.disable()
                break

#         motor1.set_duty(100)
#         counter = 0
#         while True:
#             encoder1.update()
#             print(encoder1.get_position())
#             time.sleep_ms(5)
#             counter += 1
#             if counter> 2000:
#                 motor1.disable()
#                 break
#             
#             
                
if __name__ == '__main__':
    main()
    print("done")

    
        
        
        


