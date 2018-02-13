from ur5 import UniversalRobotUR5

import time
import serial

ser = serial.Serial('COM3')
print(ser.name)

xk = -0.600
yk = 0.046



if __name__ == "__main__":
    robot = UniversalRobotUR5()
    
    #poloha+vezmi kouli 1
    robot.goto((xk, yk, 0.3), (1.30, -2.9, 0.04), 0.1)
    
    robot.wait(3) 

    
    robot.goto((xk, yk, 0.123), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)

    ser.write(b'd')     
    sleep.time(3)

    robot.goto((xk, yk, 0.3), (1.30, -2.9, 0.04), 0.1)

    #poloha+poloz kouli 2
    robot.goto((xk, -yk , 0.3), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)

    robot.goto((xk, -yk , 0.125), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)
    ser.write(b'a')    
    sleep.time(3)

    robot.goto((xk, -yk , 0.3), (1.30, -2.9, 0.04), 0.1)

    
    #poloha+vezmi kouli 3
    robot.goto((xk, -yk-0.100, 0.3), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)

    robot.goto((xk, -yk-0.100, 0.125), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)

    ser.write(b'd')     
    sleep.time(3)

    robot.goto((xk, -yk-0.100, 0.3), (1.30, -2.9, 0.04), 0.1)


    #poloha+vezmi kouli 1
    robot.goto((xk, 0.046, 0.3), (1.30, -2.9, 0.04), 0.1)
    
    robot.wait(3) 

    
    robot.goto((xk, 0.046, 0.123), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)

    ser.write(b'a')     
    sleep.time(3)

    robot.goto((xk, 0.046, 0.3), (1.30, -2.9, 0.04), 0.1)



ser.close()