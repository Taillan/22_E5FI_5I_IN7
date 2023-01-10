"""
Edited by Rostom Kachouri
M1-IRV_ST2IAI _ Mars 2021
"""


#Read Image

import cv2
import argparse

# Argument parser config
parser = argparse.ArgumentParser()

# Add custom argument for the input
parser.add_argument("-i", "--image", help="The path to the image", required=True)	
args = parser.parse_args()

# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread(args.image)
# DISPLAY
cv2.imshow(args.image,img)
cv2.waitKey(0)

cv2. destroyWindow(args.image)
