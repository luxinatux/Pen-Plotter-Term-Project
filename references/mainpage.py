'''@file                mainpage.py
   @brief               Brief doc for mainpage.py
   @details             Detailed doc for mainpage.py 

   @mainpage

   @section sec_intro   Introduction
                        This online portfolio encapsulates the totality of my 
                        work for ME 305 throuoght the quarter of Fall 2021
   
   @author              Dylan Ruiz

   @copyright           License Info

   @date                December 1, 2021
   

   
   @page page_L1        LAB 0x01
   
   @section sum_1       1.OVERVIEW
   
   @section FSM_1       2.FINITE STATE MACHINES
                        ![](State_Diagram.png)
                        
   @section vid_1       3.LED VIDEO
                        https://cpslo-my.sharepoint.com/:v:/g/personal/cvsantan_calpoly_edu/EV7XIjkioD9BppIICQ9KQdMBM13YV8a966G2egEc5d8akQ?e=hH06dX
                        
   @section code_1      4.SOURCE CODE
                        https://bitbucket.org/Santana28/me-305-source-code/src/master/Lab%201%20code/

   @page page_L2        LAB 0x02
    
   @section sum_2       1.OVERVIEW
    
   @section FSM_2       2.FINITE STATE MACHINES
                        ##ENCODER FSM
                        ![](Encoder_Diagram.png)
                        
                        ##USER FSM
                        ![](User_Diagram.png)
                        
   @section task_2      3.TASK DIAGRAM
                        ![](Task_Diagram.png)
                        
                        
   @section code_2      4.SOURCE CODE
                        https://bitbucket.org/Santana28/me-305-source-code/src/master/Lab%202%20code/
                        
   @page Page_L3        LAB 0x03
   
   @section sum_3       1.OVERVIEW
                        In this lab, our goal was to build onto our existing
                        code by implimenting spinning motors. This was 
                        achieved by creating a motor driver, and then creating
                        a motor task that would run the driver when called upon.
                        Flag variables were used to impiments the motor task 
                        into the user task.
                        
   @section FSM_3       2.FINITE STATE MACHINES
                        Since lab 3 builds off of lab 2, this FSM only shows
                        the newest states added since then.
                        
                        ##MOTOR FSM
                        ![](MOTFSM_3.png)
                        
                        ##USER FSM
                        ![](USERFSM_3.png)
                        
   @section task_3      3.TASK DIAGRAM
                        Since lab 3 builds off of lab 2, this task diagram 
                        only shows the newest shared variables that have been 
                        added since then.
                        ![](Task_3.png)
                        
   @section code_3      4.SOURCE CODE
                        https://bitbucket.org/Santana28/me-305-source-code/src/master/Lab%203%20code/
    
      
   @page page_L4        LAB 0x04
   
   @section sec_sum4    1.OVERVIEW
                        In this lab, our goal was to impliment closed loop feedback
                        into our existing code in order to achieve speed control.
                        This was achieved by creating a closed loop driver class
                        and then implimenting the functions of this driver into
                        our existing tasks. We then tuned our controller by
                        performing multiple step responses with various gain
                        values and seeeingcwhich value provided the best response.
                        
   @section sec_test    2.TEST RESULTS
                        We decided to only impliment proportional gain in our
                        controller as it was the simplest to configure. In our
                        tests, we used a setpoint velocity of 30 rad/s and
                        used a range of gain values from 2-5. We found that at
                        Kp = 2, the motor was moving to slow to produce 
                        accurate data, and at Kp = 5 the motor was beging to 
                        oscillate to much. The best response was produced
                        at Kp = 4, as it settled very quicly and orovided a 
                        consistent steady state
                        
                        ![](KP2.png)
                        ![](KP3.png)
                        ![](KP4.png)
                        ![](KP5.png)
                        
   @section FSM_4       3.FINITE STATE MACHINES
                        Since lab 4 builds off of the previous two labs, this FSM
                        only contains the newest states that have been added since
                        then.
                        
                        ##USER FSM
                        ![](FSM_4.png)
                        
   @section task_4      4.TASK DIAGRAM
                        ![](Task_4.png)
    
   @section blcok_4     5.BLOCK DIAGRAM
                        We implimented our controller as was recommended by the block
                        shown below.
                        ![](Block_4.png)
                        
   @section code_4      6.SOURCE CODE
                        https://bitbucket.org/Santana28/me-305-source-code/src/master/Lab%204%20code/
                        
   @page page_HW2       HW 0x02
   
   @section sec_1       1.SYSTEM LINKAGE KINEMATICS
                        In order to perform a dynamics analysis of the system, we first had to "unfurl"
                        the system by creating a 2D representation of the 3D system. The resulting schematic
                        is shown below, along with the assumptions that were made for our analysis.
                        
                        ![](TP_Linkage.jpg)
                        
                        This schematic was then used to develop a kinematic relationship 
                        between the motion of the motor about point A and the motion of 
                        the platform about point O as shown below.
                        
                        ![](TP_LKinematics.jpg)
                                          
   @section sec_2       2.BALL KINEMATICS
                        For this analysis, it was also essential that we be able to find
                        and expression for the motion of the ball. This was done by assuming
                        that the ball rolled without slip, and considering the motion caused
                        by the ball and platform moving together, as well as the motion of
                        the ball relative to the platform. The following calculations show the
                        derived expressions for the velocity and acceleration of the ball.
                        
                        ![](TP_BKinematics.jpg)
                        
   @section sec_3       3.LINKAGE KINETICS
                        A relationship between the motor torque for the first motor and the
                        corresponding effective moment applied to the platform was also 
                        derived for later use in the analysis. This was done by using the
                        method of virtual work in which we assumed that the system couldn't
                        store any energy due to its lack of mass. The calculations for this
                        analysis are shown below.
                        
                        ![](TP_LKinetics.jpg)
                        
   @section sec_4       4.SYSTEM EOMS
                        The next step in our analysis required the use of free body and kinetic
                        diagrams in order to develop equations of motion for our system. In order
                        to fully solve the system dynamics, we considered a system consisting of
                        the ball and platform together, and a system consisting of just the ball.
                        Small angle approximation was used to eliminate most of the terms
                        
                        ##BALL AND PLATE TOGETHER
                        For this system, all jounts were replaced with reaction forces, and the force
                        acting at point q was replaced with a force couple apllied at the pivot point O.
                        This allowed us to display our effective moment on the free body diagram. We also
                        assumed no friction at the pivot. The analysis for this system is shown below.
                        
                        ![](TP_B&P.jpg)
                        
                        ##BALL ISOLATED
                        For this system,we took the sum of the moments about the contact point between
                        the plate and the ball in order to elimate the friction force from our equations
                        of motion. The analysis for this system is shown below.
                        
                        ![](TP_B.jpg)
                        
   @section sec_5       5.SEPERATING TERMS
                        Once we had our equations of motion, we seperated the terms based on whether they
                        were a function of the angular acceleration of the platform, linear acceleration
                        of the ball, or other lower order terms. this was done for both equations of motion
                        resulting in six sepearte expressions as shown below.
                        
                        ##BALL AND PLATE TOGETHER
                        ![](TP_SB&P.jpg)
                        
                        ##BALL ISOLATED
                        ![](TP_SB.jpg)
                        
   @section sec_6       6.CREATING MATRICES
                        The final of this analysis was taking the expressions from the previous step and
                        setting them up in a matrix that will be used for future simulations. The format
                        of the matrix is shown below.
                        
                        ![](TP_Matrix.jpg)
                        
   @page page_HW3       HW 0x03
   
   @section sec_21      1.BLOCK DIAGRAMS
                        The block diagrams shown below represent the two controller
                        models that were used to run the following simulations.
                        
                        ##OPEN LOOP SIMULINK MODEL
                        ![](TP_OpenLoop.png)
                        
                        ##CLOSED LOOP SIMULINK MODEL
                        ![](TP_ClosedLoop.png)
                        
   @section sec_22      2.SIMULATION MATRICES
                        ![](TP_AMatrix.png)
                        
                        ![](TP_BMatrix.png)
                        
   @section sec_23      3.OPEN LOOP SIMULATIONS
                        The following simulations were run using the open loop model and
                        show the dynamic responses for the state variables x, θ, ̇x, 
                        and θy. In the first simulation the ball is at rest directly 
                        above the center of gravity of the plate. In the second simulation, 
                        the ball is at rest 5cm offset from the center of the plate.
                        
                        ##SIMULATION 1
                        ![](TP_S1PvT.png)
                        This plot is exactly what is expected. The ball is resting 
                        on the center of the plate, so without any disturbances, there 
                        should be no fluctuation in the ball's position.
                        
                        ![](TP_S1AvT.png)
                        This plot is exactly what is expected. The ball is resting 
                        on the center of the plate, so without any disturbances, there 
                        should be no fluctuation in the plate's angle.
                        
                        ![](TP_S1VvT.png)
                        This plot is exactly what is expected. The ball is resting 
                        on the center of the plate, so without any disturbances, there 
                        should be no fluctuation in the ball's velocity.
                        
                        ![](TP_S1WvT.png)
                        This plot is exactly what is expected. The ball is resting 
                        on the center of the plate, so without any disturbances, there 
                        should be no fluctuation in the plate's angular velocity.
                        
                        ##SIMULATION 2
                        ![](TP_S2PvT.png)
                        The ball is offset by 5 cm, so it will tilt the plate with 
                        its weight and eventually fall off the plate since there is
                        no feedback to correct for this. This is depicted in the plot.
                        
                        ![](TP_S2AvT.png)
                        The angle of the platform steadily increases as the 
                        ball rolls towards the edge, creating a  larger moment. 
                        This is shown in the figure above.
                        
                        ![](TP_S2VvT.png)
                        The figure above depicts the velocity of the ball relative 
                        to the plate. It initially starts at rest, but as the plate 
                        tilts due to the ball's weight the velocity of the ball 
                        increases, until it finally falls off the plate.
                        
                        ![](TP_S2WvT.png)      
                        The figure above shows the angular velocity of the plate. 
                        As the ball rolls further away from the center, it creates 
                        a larger moment which then creates an angular acceleration 
                        for the plate. This shows why the angular velocity is 
                        increasing over time.
                        
   @section sec_24      4.CLOSED LOOP SIMULATIONS
                        For this simulation, the ball will again be at rest and 
                        offset 5cm from the center of the plate , but this time the 
                        closed loop model will be used, so there should be some form
                        of corrective action.
                        
                        ##SIMULATION 3
                        ![](TP_S3PvT.png)
                        The figure above depicts the position of the ball relative 
                        to the plate's centerpoint. The ball starts at a position 
                        of 5 cm away from the center and oscillates about the center 
                        due to the closed loop control system. It finally reaches a 
                        steady state at the center of the plate, which is the desired outcome.
                        
                        ![](TP_S3AvT.png)
                        The figure above depicts the angle of the plate relative to 
                        its horizontal initial position. The ball starts at a position 
                        of 5 cm away from the center and oscillates about the center due 
                        to the closed loop control system. The input tilts the plate, 
                        moving the ball towards the center until it overshoots. This 
                        process continues until the ball reaches steady state at the 
                        center and the plate reaches steady state at a horizontal position.
                        
                        ![](TP_S3VvT.png)
                        The figure above depicts the velocity of the ball relative 
                        to the plate's centerpoint. The ball starts at rest, until the 
                        plate tilts from the weight of the ball. It starts to move along 
                        with the plate until the system tilts the plate so the ball moves 
                        toward the center of the plate. The velocity oscillates as the 
                        tilting of the plate oscillates, until it finally reaches a 
                        steady state of 0.
                        
                        ![](TP_S3WvT.png) 
                        The figure above depicts the angular velocity of the plate. 
                        The plate gets subjected to an input torque to steady the ball 
                        in the center of the plate at its resting position. The angular 
                        velocity of the plate constantly flips until it finally reaches 
                        a steady-state of 0.
                        
   @page page_TP        TERM PROJECT
   
   @section sec_TP1     1.OVERVIEW
                        In this project, our group utilized everything that we've learned throughout 
                        the quarter in order to construct a device that will balance a ball on a touch panel
                        utilizing closed loop feedback. To do this, we constructed various tasks that worked 
                        cooperatively. Thes tasks were set to run at different frequencies depending on their
                        function.
                        
   @section sec_TP2     2.TASK DIAGRAM
                        The figure below depicts the task diagram that we utilized in order to come up with our
                        class structure. We utilized a large amount of shared variables in order to properly execute
                        the desired function. The following sections will discuss each task in further detail.
                        
                        ## include picture of task diagram
                        
   @section sec_TP3     3.TOUCHPANEL TASK
                        The touchpanel task was responsible for collecting data regarding the position
                        and velocity of the ball in the x and y direction. It was also used as a pressure sensor
                        in order to detect when the ball was in contact with the patform. Since the ouchpanel driver
                        that this task utilized only collected information regarding the position of the ball, the respective
                        velocities were calculated within the task using using multiple positional scans and timers as shown
                        below.
                        
                        ![](TP_velocity.png)
                        
                        These positions and velocities were then stored in shared variables that were sent to the data
                        collection and controller tasks.
                        
                        ##FINITE STATE MACHINE
                        ![](TP_FSMPanel.png)
                        
   @section sec_TP4     4.IMU TASK 
                        Much like the touchpanel task, the IMU task was also responsible for collecting positional
                        and velocity data, however this time with respect to the angular position and velocity of
                        the platform in the x and y axis. This was accompished by utilizing an IMU driver that had functions
                        that would do so, thus the only thing that had to be done in the run phase of this task was to 
                        index the correct variable from the tuples generated by the driver. These position and velocity
                        values were then stored into shared variables that would also be utilized by the data and controller
                        tasks. This task was also responsible for calibrating the IMU if it wasn't already, however this was done
                        in the initialization phase.
                        
                        ##FINITE STATE MACHINE
                        ![](TP_FSMIMU.png)
                        
   @section sec_TP5     5.CONTROLLER TASK 
                        The controller task was responsible for calculating the duty cycle that would be utilized by the motors.
                        This was done by implimenting a closed loop driver that had an update function in which it would calculate
                        the total error using the shared variables from the touchpanel and IMU tasks, and then multiply it by a set 
                        gain vector in order to create an actation torque. this torque was then plugged into the follwing equation in order
                        to generate a duty cycle that would provide the neccesarry corrective action. The controller task utilized two 
                        seperate gain values depending on whether or not the ball is in contact with the platform. The controller task is 
                        initiated by a flag variable that is activated based on input in the user task.
                        
                        ![](TP_duty.png)
                        
                        These duty cycles were then stored into shared variables that would be sent to the motor task and applied to the 
                        proper motor.
                        
                        ##FINITE STATE MACHINE
                        ![](TP_FSMController.png) 
                        
   @section sec_TP6     6.MOTOR TASK  
                        The motor task was responsible for continuously implimenting the shared duty cycles that were calculated
                        in the controller task. The motor task utilized a motor driver that had functions to set the duty cycle
                        by applying the proper PWM.
                        
                        ##FINITE STATE MACHINE
                        ![](TP_FSMMotor.png)
                        
   @section sec_TP7     7.DATA TASK
                        The data task was resposible for generating a list of data regarding the position and velocity
                        of the ball and platform. The data task was initiated by a flag variable that activates based on input
                        from the user task. Since lists were used as the form of data collection, the frequency of the task is much lower
                        that the rest in order to prevent a memory failure. The list of data is then shown in puTTY with the use of the stop
                        command.
                        
                        ##FINITE STATE MACHINE
                        ![](TP_FSMData.png)
                        
   @section sec_TP8     8.USER TASK
                        The user is responsible for providing an interface that will allow the user to begin the balancing protocol
                        as well as data collection. In order to do this, the user task utilizes shared flag variables with the controller
                        and data tasks in order to initiate each of the sequences.
                        
                        ##FINITE STATE MACHINE
                        ![](TP_FSMUser.png)
                        
   @section sec_TP9     9.DEMONSTRATION VIDEOS
                        The following videos show our device in action in the cases when it has to balance itsel, and the ball.
                        It was able to balance itself well for small to medium anges, but became unstable for large angles. It was not 
                        able to balnce the ball as well as we had hoped. We believe that with more tuning it would be able to perform well,
                        but the fact that we are only using o proporional controller instead on a PI controller is also limiting.
                        
                        ##PLATFORM BALNCING ITSELF
                        https://cpslo-my.sharepoint.com/:v:/g/personal/cvsantan_calpoly_edu/Ef1ZbOhc82RDuSVbs-oSxaoBepfQ2BU1IlWXZo9koWTBXw?e=o7IFHj
                        
                        ##PLATFORM BALANCING BALL
                        https://cpslo-my.sharepoint.com/:v:/g/personal/cvsantan_calpoly_edu/ES2ZAMc9Tm1Kr0_YxBqWpJEBh-qn_2IBgKGEnFyIfd8Tpw?e=HILboW
   @section sec_TP10    10.DATA COLLECTION
                        The floowing plots show data gathered on the position of the ball as well an the position of
                        the platform. As shown in the plots, the ball does make an effort to correct itself, but falls
                        of the platform befor doing so. As for the platform, it is able to fully correct itself and
                        go back to a neutral state.
                        
                        ##PLATFORM AND BALL
                        ![](Ball_Balancing.png)
                        
                        ##PLATFORM
                        ![](Platform_Balancing.png)
                        
   @section sec_TP11    11.SOURCE CODE
                        https://bitbucket.org/Santana28/me-305-source-code/src/master/Term%20Project/
'''