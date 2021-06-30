import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("i", "--image", required = True,
            help = "Path to the image
args= vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Image", image)

def masking_process(image):
  color_ceiling = (90, 255, 255)
  color_floor = (60, 60, 60)
  
  #convert image to HSV colorspace
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  
  mask = cv2.inRange(hsv, color_floor, color_ceiling)
  #TO test: show dilate or erode go first?
  mask = cv2.dilate(mask, None, iterations=1)
  mask = cv2.erode(mask, None, iterations=1)
  return mask
  
masked=masking_process(image)

cv2.imshow("Image Masked", masked);
cv2.waitKey(0)
