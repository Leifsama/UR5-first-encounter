from ur5 import UniversalRobotUR5






if __name__ == "__main__":
    robot = UniversalRobotUR5()
    
    #poloha 1
    robot.goto((-0.600, 0.046, 0.3), (1.30, -2.9, 0.04), 0.1)
    
    robot.wait(3) 


    
    robot.goto((-0.600, 0.046, 0.123), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)

    robot.goto((-0.600, 0.046, 0.3), (1.30, -2.9, 0.04), 0.1)

    #poloha 2
    robot.goto((-0.600, -0.046, 0.3), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)

    robot.goto((-0.600, -0.046, 0.125), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)

    robot.goto((-0.600, -0.046, 0.3), (1.30, -2.9, 0.04), 0.1)

    
    #poloha 3
    robot.goto((-0.600, -0.146, 0.3), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)

    robot.goto((-0.600, -0.146, 0.125), (1.30, -2.9, 0.04), 0.1)

    robot.wait(3)

    robot.goto((-0.600, -0.146, 0.3), (1.30, -2.9, 0.04), 0.1)


