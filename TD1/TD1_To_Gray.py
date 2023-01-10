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

# def img_to_gray(image):
# 	image_gray = [pixels[0]*0.2989 + pixels[1]*0.5870 + pixels[2]* 0.1140 for pixels in image]
# 	print(image_gray)


def img_to_gray(image):
	for row in image:
		for coll in row:
			gray_collor = coll[0]*0.2989 + coll[1]*0.5870 + coll[2]* 0.1140
			coll[0]=gray_collor
			coll[1]=gray_collor
			coll[2]=gray_collor
	print(image)

if args.image:
	
	# LOAD AN IMAGE USING 'IMREAD'
	img = cv2.imread(args.image)
	img_to_gray(img)
	# DISPLAY
	cv2.imshow(args.image,img)
	cv2.waitKey(0)

	cv2. destroyWindow(args.image)