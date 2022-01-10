# pip install opencv-python
# pip install numpy

import cv2
import numpy as np

img_rgb = cv2.imread('traget_image1.png') # Read the main image
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) # Convert it to grayscale
template = cv2.imread('template_image1.png', 0) # Read the template
# template = cv2.imread('template_image2.png', 0) # Read the template

w, h = template.shape[::-1] # Store width and height of template in w and h
# Perform match operations.
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# Specify a threshold
threshold = 0.8
# Store the coordinates of matched area in a numpy array
loc = np.where(res >= threshold)

# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

# Show the final image with the matched area.
cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()