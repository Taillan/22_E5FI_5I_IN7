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
	"""
	This function take an image in input and convert it in gray color using multiplication factor:
	Red : * 0.2989
	Blue : * 0.5870
	Green : * 0.1140
	"""
	b, g, r = image[:,:,0], image[:,:,1], image[:,:,2]
	gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
	image[:,:,0] = gray
	image[:,:,1] = gray
	image[:,:,2] = gray
	return image

def img_to_gray_function(image):
	"""
	This function take an image in input and convert it in gray color using opencv color/ function
	"""
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


if args.image:
	
	img = cv2.imread(args.image)
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