import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("i", "--image", required = True,
            help = "Path to the image
args= vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Image", image)

# Create function for automatically computing canny lower and upper bounds
def auto_canny(image, sigma = 0.33):
  #computer the median of the single channel (greyscale) pixel intensities
  canny = np.median(image)
  
  #apply automatic Canny edge detection using computed median
  lower = int(max(0, (1.0 - sigma) * v))
  upper = int(min(255, (1.0 + sigma) * v))
  edged = cv2.Canny(image, 30, 150)
  
  cv2.imshow("Canny", canny)
  cv2.waitKey(0)
