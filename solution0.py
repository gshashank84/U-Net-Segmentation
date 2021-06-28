import numpy as np
import argparse
import cv2
from art import tprint

parser = argparse.ArgumentParser()
parser.add_argument("image",type=str,default="data/task_1/coin1.jpeg",help="Image Path")
parser.add_argument("pixel",type=str,default="38,144",help="Pixel Coordinates")
args = vars(parser.parse_args())

# Extracting the coordinates of the pixel
pixel = list(map(int,args['pixel'].split(',')))

# Extracting the image path
image_path = args['image']

# Loading the image
image = cv2.imread(image_path)
output = image.copy()

# Converting the colour image to Grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Obtaining the circle from the image
circles= cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1,250,param1=30,param2=15,minRadius=0,maxRadius=0)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        # drawing the circle in the output image
        # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        
        # Plotting the Pixel coordinates
        cv2.circle(output, (pixel[0],pixel[1]), radius=4, color=(0,128, 255), thickness=-1)

        #Calculating the distance between centre of circle to the pixel coordinates
        distance = np.sqrt((x - pixel[0])**2+(y - pixel[1])**2)

        # Determining if the pixel is outside or inside the circle
        if distance > r :
            tprint('Outside')
            ans = 'Outside'
        else:
            tprint('Inside')
            ans = 'Inside'

    # showing the output image
    cv2.imshow("output", output)
    cv2.waitKey(0)
else:
    print("No circle detected")