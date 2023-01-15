"""
This program allow the user to chose an input and to convert this input into gray color.
Arguments:
	--image
	--video
	--webcam
"""

import math
import argparse
import cv2
import numpy as np


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
	gray_image = np.copy(image)
	b, g, r = image[:,:,0], image[:,:,1], image[:,:,2]
	gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
	gray_image[:,:,0] = gray
	gray_image[:,:,1] = gray
	gray_image[:,:,2] = gray
	return gray_image

def img_to_gray_function(image):
	"""
	This function take an image in input and convert it in gray color using opencv color/ function
	"""
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def blur_filter(image):
	"""
	This function make a gaussian blur from a gray image with a kernel of (5,5).
	"""
	blur_image = np.copy(image)
	img = blur = image[:,:,0]
	for i in range(len(img)):
		for j in range(len(img[0])):
			blur_pixel = 0
			count = 0
			for k in range(-2,3):
				for l in range(-2,3):
					try:
						blur_pixel += img[i+k][j+l]
						count += 1
					except:
						pass
			blur[i][j] = int(blur_pixel / count)
	blur_image[:,:,0] = blur
	blur_image[:,:,1] = blur
	blur_image[:,:,2] = blur
	return blur_image

def blur_filter_opencv(image):
	"""
	This function make a gaussian blur from a gray image with a kernel of (5,5) using opencv function.
	"""
	return cv2.blur(image,(5,5))

def sobel_filter(image):
	"""
	This function make a sobel filter from a gray image with a kernel of (3,3). 
	"""
	sobel_image = np.copy(image)
	img = image[:,:,0]
	sobel = sobel_image[:,:,0]
	horizontal_coeff = [[-1,0,1],[-2,0,2],[-1,0,1]]
	vertical_coeff = [[-1,-2,-1],[0,0,0],[1,2,1]]
	for i in range(len(img)):
		for j in range(len(img[0])):
			sobel_pixel = 0
			sobel_horizontal = 0
			sobel_vertical = 0

			for k in range(-1,2):
				for l in range(-1,2):
					try:
						sobel_horizontal += img[i+k][j+l] * horizontal_coeff[k+1][l+1]
						sobel_vertical += img[i+k][j+l] * vertical_coeff[k+1][l+1]
					except:
						pass
			sobel[i][j] = math.sqrt((sobel_horizontal * sobel_horizontal) + (sobel_vertical * sobel_vertical))
	sobel_image[:,:,0] = sobel
	sobel_image[:,:,1] = sobel
	sobel_image[:,:,2] = sobel
	return sobel_image

def sobel_filter_opencv(image):
	"""
	This function make a sobel filter from a gray image with a kernel of (3,3) using opencv function.
	"""
	return cv2.Sobel(image,cv2.CV_8U,1,0,ksize=3)


if args.image:
	
	img = cv2.imread(args.image)

	manual_blur_filter = blur_filter(img_to_gray_multiplication(img))
	cv2.imshow("Manual blur filter", manual_blur_filter)
	cv2.imwrite('manual_blur_filter.jpg', manual_blur_filter) 

	opencv_blur_filter = blur_filter_opencv(img_to_gray_function(img))
	cv2.imshow("Opencv blur filter", opencv_blur_filter)
	cv2.imwrite('opencv_blur_filter.jpg', opencv_blur_filter)

	manual_sobel_filter = sobel_filter(img_to_gray_multiplication(img))
	cv2.imshow("Manual sobel filter", manual_sobel_filter)
	cv2.imwrite('manual_sobel_filter.jpg', manual_sobel_filter)

	opencv_sobel_filter = sobel_filter_opencv(img_to_gray_function(img))
	cv2.imshow("Opencv sobel filter", opencv_sobel_filter)
	cv2.imwrite('opencv_sobel_filter.jpg', opencv_sobel_filter)

	cv2.waitKey(0)


	cv2.destroyWindow("Manual blur filter")
	cv2.destroyWindow("Opencv blur filter")
	cv2.destroyWindow("Manual sobel filter")
	cv2.destroyWindow("Opencv sobel filter")

if args.video:
	"""
	Can't use manual filters because it needs too much calculations to render a video.
	TODO : Optimize those functions.
	"""
	cap = cv2.VideoCapture(args.video)
	while True:
		success, img = cap.read()
		cv2.imshow("Opencv blur filter",blur_filter_opencv(img_to_gray_function(img)))

		cv2.imshow("Opencv sobel filter",sobel_filter_opencv(img_to_gray_function(img)))
		if cv2.waitKey(1) == ord('q'):
			 break
			 
	cv2.destroyWindow("Opencv blur filter")
	cv2.destroyWindow("Opencv sobel filter")

if args.webcam:
	"""
	Can't use manual filters because it needs too much calculations to render a live stream.
	TODO : Optimize those functions.
	"""
	cameraCapture = cv2.VideoCapture (0)
	print ('Showing camera feed. Press any key to stop.')
	success, frame = cameraCapture.read()
	while success and cv2.waitKey(1) == -1:
		cv2.imshow("Opencv blur filter",blur_filter_opencv(img_to_gray_function(img)))

		cv2.imshow("Opencv sobel filter",sobel_filter_opencv(img_to_gray_function(img)))
		success, frame = cameraCapture.read()
		
	cv2.destroyWindow("Opencv blur filter")
	cv2.destroyWindow("Opencv sobel filter")