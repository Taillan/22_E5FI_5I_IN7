"""
This program allow the user to chose an input and to convert this input into gray color.
Arguments:
	--image
	--video
	--webcam
"""

import cv2
import argparse

# Argument parser config
parser = argparse.ArgumentParser()

# Add custom argument for the input
parser.add_argument("-i", "--image", help="The path to the image")	
parser.add_argument("-v", "--video", help="The path to the video")	
parser.add_argument("-w", "--webcam", help="To activate the webcam", action='store_true')	

args = parser.parse_args()

if not (args.image or args.video or args.webcam):
	print("You need to chose an input : --help")
	exit()

def img_to_gray_multiplication(image):
	for row in image:
		for coll in row:
			gray_collor = coll[0]*0.2989 + coll[1]*0.5870 + coll[2]* 0.1140
			coll[0]=gray_collor
			coll[1]=gray_collor
			coll[2]=gray_collor
	return image

def img_to_gray_function(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if args.image:
	
	# LOAD AN IMAGE USING 'IMREAD'
	img = cv2.imread(args.image)
	# DISPLAY
	cv2.imshow("Gray multiplication",img_to_gray_multiplication(img))
	cv2.imshow("Gray color function",img_to_gray_function(img))

	cv2.waitKey(0)

	cv2.destroyWindow("Gray multiplication")
	cv2.destroyWindow("Gray color function")

if args.video:

	cap = cv2.VideoCapture(args.video)
	while True:
	    success, img = cap.read()
	    cv2.imshow("Gray multiplication", img_to_gray_multiplication(img))
	    cv2.imshow("Gray color function", img_to_gray_function(img))
	    if cv2.waitKey(1) == ord('q'):
	         break
	         
	cv2.destroyWindow("Gray multiplication")
	cv2.destroyWindow("Gray color function")

if args.webcam:
	cameraCapture = cv2.VideoCapture (0)
	print ('Showing camera feed. Press any key to stop.')
	success, frame = cameraCapture.read()
	while success and cv2.waitKey(1) == -1:
	    cv2.imshow('Gray multiplication', img_to_gray_multiplication(frame))
	    cv2.imshow('Gray color function', img_to_gray_function(frame))
	    success, frame = cameraCapture.read()
	    
	cv2.destroyWindow("Gray multiplication")
	cv2.destroyWindow("Gray color function")