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
        
        
        
        pin_sol = pyb.Pin(pyb.Pin.cpu.A9, pyb.Pin.OPEN_DRAIN, value = 1)

        time.sleep(5)
    
        pin_sol = pyb.Pin(pyb.Pin.cpu.A9, pyb.Pin.OUT_PP)
        pin_sol.high()
        time.sleep(5)
    
        pin_sol = pyb.Pin(pyb.Pin.cpu.A9, pyb.Pin.OUT_PP)
        pin_sol.low()
    
    
        #enableA.low()
        print('ok')
        enableA = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_PP)
        in1_mot = pyb.Pin(pyb.Pin.cpu.B4)
        in2_mot = pyb.Pin(pyb.Pin.cpu.B5)
        motor_belt = motor_Ruiz_Martos.Motor(enableA,in1_mot,in2_mot,3) # motor in A
        motor_belt.enable()
        in1_enc = pyb.Pin(pyb.Pin.cpu.B6)
        in2_enc = pyb.Pin(pyb.Pin.cpu.B7)
        encoder1 = encoder_Ruiz_Martos.Encoder(in1_enc,in2_enc,4) # motor in A
        
        enableB = pyb.Pin(pyb.Pin.cpu.C1, pyb.Pin.OUT_PP)
        in1_motB = pyb.Pin(pyb.Pin.cpu.A0)
        in2_motB = pyb.Pin(pyb.Pin.cpu.A1)
        motor_elbow = motor_Ruiz_Martos.Motor(enableB,in1_motB,in2_motB,5) # motor in B
        motor_elbow.enable()
        in1_enc_B = pyb.Pin(pyb.Pin.cpu.C6)
        in2_enc_B = pyb.Pin(pyb.Pin.cpu.C7)
        encoder2 = encoder_Ruiz_Martos.Encoder(in1_enc_B,in2_enc_B,8)
        
        
        Closed_loop_Elbow = closedloop.ClosedLoop(0.5, 0)
        Closed_loop_Belt = closedloop.ClosedLoop(0.5, 0)
        
        
        time_period = 10 #specifying that the interval we want is 10s
        step_Belt = 2000 # 24500 ticks per rev
        step_Elbow = 4000 # 4192 ticks per rev
        
        time_next = 0
        encoder1.set_position(0)
        encoder2.set_position(0)
        Limit_switch_Belt = pyb.Pin(pyb.Pin.cpu.A7,pyb.Pin.IN)
        Limit_switch_Elbow = pyb.Pin(pyb.Pin.cpu.A5,pyb.Pin.IN)
        while True:
            if Limit_switch_Elbow.value() == 1 and Limit_switch_Belt.value() == 1:
                break
        time_start = time.ticks_ms()
        while True:
            time_now = time.ticks_diff(time.ticks_ms(),time_start)
            if time_now >= time_next:
                time_next = time.ticks_add(time_next,time_period)
                encoder2.update()
                encoder1.update()
                motor_elbow.set_duty(Closed_loop_Elbow.update(step_Elbow,encoder2.get_position()))
                motor_belt.set_duty(Closed_loop_Belt.update(step_Belt,encoder1.get_position()))
                print('{:},{:}'.format(encoder2.get_position(),encoder1.get_position()))
                
            
            if time_now >= 3000:
                
                motor_elbow.disable()
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

    
        
        
        


