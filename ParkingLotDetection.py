import cv2
import numpy as py
from matplotlib import pyplot as plt
from cv2 import threshold, THRESH_BINARY, boundingRect


# img = cv2.imread('testImage.jpg', cv2.IMREAD_COLOR)
# cv2.imshow('hi', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows

original = cv2.imread('Insert Pic Location Here')
cv2.imshow('Original', original)
gray = cv2.cvtColor(original, cv2.COLOR_RGB2GRAY)
cv2.imshow('grey', gray)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#blurred = cv2.bilateralFilter(gray,9,75,75)
cv2.imshow('blurred', blurred)
canny = cv2.Canny(blurred, 100, 100)
height, width = canny.shape[:2]
#print(height)
#print(width)
temp = ""
ytemp = 0

# for x in range (0, 264):
#     for y in range (0, 400):
#         print(canny[x][y])
        
        
for x in range (0, height - 2):
    for y in range (0, width - 4):
        if (canny[x][y + 1] == 255):
            canny[x][y] = 255
        if (canny[x][y + 2] == 255):
            canny[x][y] = 255
        if (canny[x][y + 3] == 255):
            canny[x][y] = 255
        if (canny[x][y + 4] == 255):
            canny[x][y] = 255
        if (canny[x + 1][y] == 255):
            canny[x][y] = 255
        if (canny[x + 2][y] == 255):
            canny[x][y] = 255
            
for x in range (0, height):
    for y in range (1, width - 4):
        if ( (canny[x][y + 1] == 0) and (canny[x][y - 1] == 0) and (canny[x][y + 4]) != 0):
            canny[x][y] = 50
            
for x in range (0, height):
    for y in range (0, width):
        if ( canny[x][y] == 0):
            canny[x][y] = 255
            
            
        
        
# blurred = cv2.GaussianBlur(canny, (5, 5), 0)
# cv2.imshow('blurred', blurred)
cv2.imshow('Canny', canny)
  

canny2 = cv2.Canny(canny, 810, 810)

cv2.imshow('Canny2', canny2)

blurred2 = cv2.GaussianBlur(canny2, (5, 5), 0)

cv2.imshow('blurred2', blurred2)

# lines = cv2.HoughLinesP(blurred2,1,py.pi/50,100,20,1)
# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(original,(x1,y1),(x2,y2),(0,255,0),1)
#         
# cv2.imshow('HoughLine', original)


contours, hierarchy = cv2.findContours(blurred2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contourPoints = [] 
# print ("length" + str(len(contours[0])))
# print(len(contours))
# for x in range (0, 68):
#      contourPoints.append(contours[0][x][0])
# print("New Array")
# print(len(contourPoints))
# for x in range (0, len(contourPoints)):
#      cv2.circle(original, (contourPoints[x][0], contourPoints[x][1]), 5, (0, 0, 255), 1, 0)
#cv2.drawContours(original, contours, -1, (255, 0, 0), 1 )

# cnt = contours[5]
# area = cv2.contourArea(cnt)
# print(area)
# 
# cnt1 = contours[6]
# area1 = cv2.contourArea(cnt1)
# print(area1)
# 
# cnt2 = contours[7]
# area2 = cv2.contourArea(cnt2)
# print(area2)
# 
# cnt3 = contours[7]
# area3 = cv2.contourArea(cnt3)
# print(area3)
# 
# cnt4 = contours[7]
# area4 = cv2.contourArea(cnt4)
# print(area4)

goodcontours = [1000]
for x in contours:
    area = cv2.contourArea(x)
    if (area > 190):
        cv2.drawContours(original, x, -1, (0, 255, 0), 1 )
        M = cv2.moments(x)
        centroid_x = int(M['m10']/M['m00'])
        centroid_y = int(M['m01']/M['m00'])
        cv2.circle(original, (centroid_x, centroid_y),5,255,-1)
        print(centroid_x)
        print(centroid_y)
        print()
#     print(area)



#for p in contours: cv2.circle(original, p, 1, (0, 0, 255), 1, 0)
cv2.imshow('normalThreshold', original)
cv2.waitKey(0)
cv2.destroyAllWindows()
 

