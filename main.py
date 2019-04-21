#!/usr/bin/python
import cv2
import numpy

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def getLines(image):
    result = []
    for i in range(len(image[0])):
        for yid,j in enumerate(image):
            prev_pixel = j[i]
            try:
                pixel = j[i+1]
            except:
                pixel = prev_pixel
            diff = abs(prev_pixel-pixel)
            if diff>=240:
                result.append(Point(i,yid))
    return result

orig_image = cv2.imread("piano.jpg")
img_to_display = orig_image.copy()
img_gray = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)
thresh, img_bw = cv2.threshold(img_gray, 128, 255, 8)
for i in getLines(img_bw):
    cv2.circle(img_to_display,(i.x,i.y),2,(255,0,0),-1)
cv2.imshow("Final", img_to_display)
cv2.waitKey()
