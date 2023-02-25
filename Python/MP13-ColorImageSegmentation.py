import cv2
from PIL import Image
import numpy as np
import math
def main():
    while True:
        #Image path
        imgor = r'lena.jpg' 
        #Read Image
        img = cv2.imread(imgor, cv2.IMREAD_COLOR)
        #Read color image using PIL library, which can replace OpenCV to process image
        imgPIL = Image.open(imgor)
        #Enter the desired position value
        x1 = int(input("Enter x1 value: "))
        y1 = int(input("Enter y1 value: "))
        x2 = int(input("Enter x2 value: "))
        y2 = int(input("Enter y2 value: "))
        #Enter the desired threshold value
        threshold = int(input("Enter the desired threshold value: "))
        #Assign value for image
        sgmpic_tem = ColorImageSegmentation(imgPIL, threshold, x1, y1, x2, y2)       
        #Show Image
        #cv2.imshow('Lightness Grayscale Image', lgtpic_tem)
        #cv2.imshow('Binary Image', bnpic_tem)
        #cv2.imshow('Luminace Grayscale Image', lumpic_tem)
        #cv2.imshow('Original Image', img)
        cv2.imshow('Image', sgmpic_tem)
        
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()
    
def VectorA(imgPIL, x1, y1, x2, y2):
    #Create variable to contain incremental value of pixel
    aR = 0; aG = 0; aB = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #Add up all the pixel value for each R-G-B channel respectively
            aR += r
            aG += g
            aB += b
    size = abs(x2 - x1) * abs(y2 - y1)
    aR /= size
    aG /= size
    aB /= size
    vectora_tem = [aR, aG, aB]
    return vectora_tem
    
def ColorImageSegmentation(imgPIL, threshold, x1, y1, x2, y2):
    #Set aR, aG, aB
    a = VectorA(imgPIL, x1, y1, x2, y2)
    #Make a copy of imgPIL to return the converted image
    sgmimg = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = sgmimg.size[0]
    height = sgmimg.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #Using Average method with following equation
            D = math.sqrt((r - a[0]) * (r - a[0]) + (g - a[1]) * (g - a[1]) + (b - a[2]) * (b - a[2]))
            #Identify the segment value
            if (D <= threshold):
                #Assign the 255 value for image
                sgmimg.putpixel((x, y), (255, 255, 255))
            else:
                #Assign the RGB value for image
                sgmimg.putpixel((x, y), (b, g, r))
    sgmpic = np.array(sgmimg)
    return sgmpic


          
main()
