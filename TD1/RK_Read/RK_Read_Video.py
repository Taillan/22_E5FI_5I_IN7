"""
Edited by Rostom Kachouri
M1-IRV_ST2IAI _ Mars 2021
"""

#Read Video

import cv2
import argparse

# Argument parser config
parser = argparse.ArgumentParser()


parser.add_argument("-v", "--video", help="The path to the video", required=True)   
args = parser.parse_args()

#frameWidth = 640
#frameHeight = 480
cap = cv2.VideoCapture(args.video)
while True:
    success, img = cap.read()
    #img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)
    #cv2.waitKey(1)
    if cv2.waitKey(1) == ord('q'):
         break
         
cv2. destroyWindow('Video')



