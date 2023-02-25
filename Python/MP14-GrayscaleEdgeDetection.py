import cv2
from PIL import Image
import numpy as np
import math
def main():
    while True:
        #Image path
        imgor = r'kkk.jpg'
        #Read Image
        img = cv2.imread(imgor, cv2.IMREAD_COLOR)
        #Read color image using PIL library, which can replace OpenCV to process image
        imgPIL = Image.open(imgor)
        edimg = GrayscaleImageEdgeDetecting(imgPIL, 70)
        #Show Original Image
        cv2.imshow('Original Image', img)
        #Show 3x3 Image
        cv2.imshow('Edge Detected Image', edimg)
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()
    
def RGBLuminaceConvert(imgPIL):
    #Make a copy of imgPIL to return the converted image
    lum = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = lum.size[0]
    height = lum.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #Using Lightness method with following equation
            gray = np.uint8(0.2126*r + 0.7152*g + 0.0722*b) #Using np.uint8 to convert the value to usigned integer 8bit (byte in C#)
            #Assign the gray value for avg 
            lum.putpixel((x, y), (gray, gray, gray))
    return lum
   
def GrayscaleImageEdgeDetecting(imgPIL, threshold):
    #Make a copy of imgPIL to return the converted image
    pic = Image.new(imgPIL.mode, imgPIL.size)
    #Make a copy of imgPIL to return the converted image
    edimg_tem = RGBLuminaceConvert(imgPIL)
    #Take the image dimension
    width = edimg_tem.size[0] #4 pics have the same dimension
    height = edimg_tem.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    #Pay attention to 3x3 mask, to ease to code and not to be out of range (check the theory), we can abadon the border of image
    #So we just need to focus on x = 1 to x = width - 1, y = 1 to y = height - 1
    for x in range(1, width - 1): #0 -> width - 1
        for y in range(1, height - 1):
            #Create a maskmatrix in g(x)
            maskx = np.zeros((512,512), np.int8) #Create a matrix has 512 components with datatype is integer 8 bit
            maskx[x - 1, y - 1] = -1; maskx[x - 1, y] = 0; maskx[x - 1, y + 1] = 1
            maskx[x, y - 1] = -2; maskx[x, y] = 0; maskx[x, y + 1] = 2
            maskx[x + 1, y - 1] = -1; maskx[x + 1, y] = 0; maskx[x + 1, y + 1] = 1
            #----------------------------------------------#
            #Create a maskmatrix in g(y)
            masky = np.zeros((512,512), np.int8) #Create a matrix has 512 components with datatype is integer 8 bit
            masky[x - 1, y - 1] = -1; masky[x - 1, y] = -2; masky[x - 1, y + 1] = -1
            masky[x, y - 1] = 0; masky[x, y] = 0; masky[x, y + 1] = 0
            masky[x + 1, y - 1] = 1; masky[x + 1, y] = 2; masky[x + 1, y + 1] = 1
            #Create variable to contain incremental value of pixel in mask. So they must be declared
            #"int" type to be able to contain those value.
            #Proceed to scan the points in the mask
            grayx = 0
            grayy = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    #Get information R-G-B at the pixel point in mask at postion [i, j]
                    gray_pixel, g, b = np.uint8(imgPIL.getpixel((i,j))) #.getpixel returns int value
                    #Calculate the Edge Dectecting funtion in g(x)
                    grayx += gray_pixel * maskx[i, j]
                    #Calculate the Edge Dectecting funtion in g(y)
                    grayy += gray_pixel * masky[i, j]
            #End up everything. We average all the value in each channel R-G-B
            #Get information R-G-B at the pixel point in mask at postion [i, j]
            M = abs(grayx) + abs(grayy)
            if (M <= threshold):
                #Set image pixel
                edimg_tem.putpixel((x, y), (0,0,0)) #put 0 channel first, then 1 and 2 respectively
            else:
                #Set image pixel
                edimg_tem.putpixel((x, y), (255, 255, 255)) #put 0 channel first, then 1 and 2 respectively
    edimg = np.array(edimg_tem)
    return edimg
main()