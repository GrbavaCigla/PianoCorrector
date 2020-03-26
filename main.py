#!/usr/bin/python
import cv2
import numpy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.taken = False


def getDistance(point, point2):
    xdis = abs(point.x - point2.x)
    ydis = abs(point.y - point2.y)
    return (ydis**2 + xdis**2)**0.5


def getClosest(point, points):
    points.pop(points.index(point))
    mini = getDistance(points[0], point)
    respoint = None
    for i in points:
        if point.taken == False:
            temp = getDistance(i, point)
            if temp < mini:
                mini = temp
                respoint = i
                point.taken = True
        else:
            continue
    return respoint


def getGroups(points, prange):
    groups = []
    tempgrp = []


def getPoints(image):
    result = []
    for i in range(len(image[0])):
        for yid, j in enumerate(image):
            prev_pixel = j[i]
            try:
                pixel = j[i + 1]
            except:
                pixel = prev_pixel
            diff = abs(prev_pixel - pixel)
            if diff >= 240:
                result.append(Point(i, yid))
    return result


orig_image = cv2.imread("piano1.jpg")
orig_image = cv2.resize(orig_image, (0, 0), fx=0.3, fy=0.3)
img_to_display = orig_image.copy()
img_gray = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)
thresh, img_bw = cv2.threshold(img_gray, 85, 255, 0)
all_points = list(set(getPoints(img_bw)))
for i in all_points:
    closestp = getClosest(i, all_points)
    if not closestp == None:
        cv2.line(img_to_display, (i.x, i.y), (closestp.x, closestp.y), 2)

# cv2.namedWindow("Final", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("Final",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow("Final", img_to_display)
cv2.waitKey()