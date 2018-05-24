import cv2
import numpy as np
import math
from ur5 import UniversalRobotUR5
import time
import serial
robot = UniversalRobotUR5()

#ser = serial.Serial('COM3')
#print(ser.name)

#lowerBound=np.array([150,30,30])
#upperBound=np.array([179,240,240])

cam = cv2.VideoCapture(1)
img = cam
j = 0
k = 0
l = 0
xR = -0.610 + j
yR = 0.045 + k
zR = 0.4 + l
    
while True:
       
    ret, frame = cam.read()
    frame = cv2.resize(frame,(340,220))

    #sensitivity = 30
    #lower_red_0 = np.array([160, 60, 80]) 
    #upper_red_0 = np.array([180, 255, 180])
    #lower_red_1 = np.array([150, 100, 0]) 
    #upper_red_1 = np.array([180, 255, 100])

    lower_red_0 = np.array([160, 120, 120]) 
    upper_red_0 = np.array([180, 255, 255])
    lower_red_1 = np.array([150, 180, 0]) 
    upper_red_1 = np.array([180, 255, 100])

    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask_0 = cv2.inRange(hsv, lower_red_0 , upper_red_0);
    mask_1 = cv2.inRange(hsv, lower_red_1 , upper_red_1 );

    mask = cv2.bitwise_or(mask_0, mask_1)
        
    #mask=cv2.inRange(imgHSV,lower_red,upper_red)
    
    #cv2.waitKey(0)

    #kernelOpen=np.ones((5,5))
    #kernelClose=np.ones((40,40))

    #maskOpen2=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    #maskClose2=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernelClose)

    kernel =np.ones((8,8), np.uint8)

    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    maskClose=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    kernel3 =np.ones((18,18), np.uint8)
    maskOpen3=cv2.morphologyEx(maskOpen,cv2.MORPH_OPEN,kernel3)
    maskClose3=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernel3)

    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)
    mask2 = cv2.bitwise_or(erosion, dilation)

    kernel =np.ones((8,8), np.uint8)

    maskOpenDilation=cv2.morphologyEx(mask2,cv2.MORPH_OPEN,kernel)
    maskCloseDilation=cv2.morphologyEx(mask2,cv2.MORPH_CLOSE,kernel)

    kernel4 =np.ones((18,18), np.uint8)
    maskOpenDilation2=cv2.morphologyEx(maskOpenDilation,cv2.MORPH_OPEN,kernel4)
    maskCloseDilation2=cv2.morphologyEx(maskCloseDilation,cv2.MORPH_CLOSE,kernel4)

    
    #final = cv2.GaussianBlur(maskClose3, (5,5), 0)

    _, contours, hierarchy = cv2.findContours(maskClose3.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center = None

    _, contours2, hierarchy = cv2.findContours(maskCloseDilation2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center2 = None

    #cv2.drawContours(frame, contours, -1, (0,255,0), 2)

    #avg = 30
    #for c in contours:
    #    avg += len(c)
    #avg /=len(contours)

    #for c in contours:
    #    if len(c) > avg/2:
    #        M = cv2.moments(c)
    #        cx = int(M['m10']/M['m00'])
    #        cy = int(M['m01']/M['m00'])
        
    #brano pres mask open/close-> modry kruh
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((a, b), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 15:
            cv2.circle(frame, (int(a), int(b)), int(radius),
				(255, 0, 0), 2)
        cv2.circle(frame, center, 5, (255, 0, 0), -1)
        
    #brano z eroze-> zeleny kruh
    if len(contours2) > 0:
        c2 = max(contours2, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c2)
        M2 = cv2.moments(c2)
        center2 = (int(M2["m10"] / M2["m00"]), int(M2["m01"] / M2["m00"]))

        if radius > 15:
            cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 0), 2)
        cv2.circle(frame, center2, 5, (0, 255, ), -1)
        #print(x)
        print(y)
            
        #def main():
        #if __name__ == "__main__":
        #while __name__ == "__main__":
        #def __name__ == "__main__":
     
        #cv2.imshow("frame",frame)
       
        #while True:
            #cv2.imshow("frame",frame)
            #cv2.waitKey(1)
            #cv2.destroyAllWindows()
            #n = 0
        
        #cv2.imshow("frame",frame)
        #while True: 
        
        
        if x < 160:
            robot.goto((xR, yR-j, zR), (1.30, -2.9, 0.04), 0.5)
            #ser.write(b'd') 
            yR= yR-0.01   
                                        
            #j = j + 0.005
            #print(x)
            #print(xR)    
              
            #time.sleep(2)
                
            #break

        if 180 < x:
            robot.goto((xR, yR+j, zR), (1.30, -2.9, 0.04), 0.5)
            yR= yR+0.01
            #j = j - 0.005
            #robot.wait(0.5)
            #ser.write(b'a')
            #print(x)
            #print(xR)
            #time.sleep(2)
            #break
        
        if 0 < y < 100:
            robot.goto((xR+k, yR, zR), (1.30, -2.9, 0.04), 0.5)
            xR= xR-0.01
        #    k = k - 0.015
            #robot.wait(0.5)
                
        if 120 < y < 220:
            robot.goto((xR+k, yR, zR), (1.30, -2.9, 0.04), 0.5) 
            xR= xR+0.01
        #    k = k + 0.015
                #robot.wait(0.5)
            if 160 <= x <= 180:
                if 100 <= y <= 120:
                    robot.goto((xR, yR, zR), (1.30, -2.9, 0.04), 0.5)
                    zR = z - 0.005
                    #if z < 0.15:
            #            break
                    #robot.wait(0.5)
            #return 
            #main() 

            #if x <=160
                #   elif x => 180:
                #  elif y <= 100:
                # elif y >= 120:
                #    robot.goto((xk, yk, zk-0.3), (1.30, -2.9, 0.04), 0.1)        
                 
    #count = cv2.countNonZero(maskCloseDilation2)
    #def count_nonblack_np(maskCloseDilation2):

        #return img.any(axis=-1).sum()
    #print(count)    


   
       
    cv2.imshow("mask0",mask_0)
    cv2.imshow("mask1",mask_1)
    cv2.imshow("mask",mask)
    #cv2.imshow("cam",frame)
    #cv2.imshow("cam2",cam)
    #cv2.imshow("maskClose2",maskClose2)
    #cv2.imshow("maskOpen2",maskOpen2)
    #cv2.imshow("maskOpen",maskOpen)
    #cv2.imshow("maskClose",maskClose)
    #cv2.imshow("maskOpen3",maskOpen3)
    #cv2.imshow("maskClose3",maskClose3)
    #cv2.imshow("erosion",erosion)
    #cv2.imshow("dilation",dilation)
    cv2.imshow("frame",frame)
    #cv2.imshow("maskOpenErosion",maskOpenErosion)
    #cv2.imshow("maskCloseErosion",maskCloseErosion)
    #cv2.imshow("maskOpenDialtion",maskOpenDilation)
    #cv2.imshow("maskCloseDilation",maskCloseDilation)
    #cv2.imshow("maskOpenDialtion2",maskOpenDilation2)
    #cv2.imshow("maskCloseDilation2",maskCloseDilation2)
    #cv2.imshow("mask2",mask2)
    cv2.waitKey(1)

cam.release()