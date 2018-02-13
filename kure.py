from ur5 import UniversalRobotUR5

import time
import serial

ser = serial.Serial('COM3')
print(ser.name)

xk = -0.610
yk = 0.045



if __name__ == "__main__":
    robot = UniversalRobotUR5()
    
    #poloha+vezmi kouli 1
    robot.goto((xk, yk, 0.3), (1.30, -2.9, 0.04), 4000)
    ser.write(b'd')
    #robot.wait(1) 

    
    robot.goto((xk, yk+0.005, 0.123), (1.30, -2.9, 0.04), 4000)

    #robot.wait(1)

    ser.write(b'd')     
    robot.wait(1)

    robot.goto((xk, yk+0.005, 0.3), (1.30, -2.9, 0.04), 4000)

    #poloha+poloz kouli 2
    robot.goto((xk, -yk, 0.3), (1.30, -2.9, 0.04), 0.5)

    #robot.wait(0.5)

    robot.goto((xk, -yk, 0.125), (1.30, -2.9, 0.04), 0.5)

    #robot.wait(0.5)
    ser.write(b'a')    
    

    robot.goto((xk, -yk, 0.3), (1.30, -2.9, 0.04), 0.5)

    ser.write(b'd')
    #poloha+vezmi kouli 3
    robot.goto((xk, -yk-0.09, 0.3), (1.30, -2.9, 0.04), 0.5)
    
    #robot.wait(0.5)

    robot.goto((xk, -yk-0.09, 0.124), (1.30, -2.9, 0.04), 0.5)

    #robot.wait(0.5)

    ser.write(b'd')     
    

    robot.goto((xk, -yk-0.09, 0.3), (1.30, -2.9, 0.04), 0.5)


    #poloha+vezmi kouli 1
    robot.goto((xk, yk+0.005, 0.3), (1.30, -2.9, 0.04), 0.5)
    
    #robot.wait(0.5) 

    
    robot.goto((xk, yk+0.005, 0.123), (1.30, -2.9, 0.04), 0.5)

    #robot.wait(0.5)

    ser.write(b'a')     
   

    robot.goto((xk, yk, 0.3), (1.30, -2.9, 0.04), 0.5)
    
    ser.write(b'd')

    #poloha+veymi kouli 2
    robot.goto((xk, -yk, 0.3), (1.30, -2.9, 0.04), 0.5)

    #robot.wait(0.5)

    robot.goto((xk, -yk, 0.123), (1.30, -2.9, 0.04), 0.5)

    #robot.wait(0.5)
    ser.write(b'd')    
    

    robot.goto((xk+0.1, yk, 0.3), (1.30, -2.9, 0.04), 0.5)

    #poloha+poloz kouli 2
    robot.goto((xk+0.1, yk, 0.3), (1.30, -2.9, 0.04), 0.5)

    #robot.wait(0.5)

    robot.goto((xk+0.1, yk, 0.125), (1.30, -2.9, 0.04), 0.5)

    #robot.wait(0.5)
    ser.write(b'a')    
    

    robot.goto((xk, yk, 0.3), (1.30, -2.9, 0.04), 0.5)

    ser.write(b'd') 

ser.close()