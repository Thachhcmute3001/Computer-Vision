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
        edimg = GrayscaleImageEdgeDetecting(imgPIL, 70)
        #Show Original Image
        cv2.imshow('Original Image', img)
        #Show 3x3 Image
        cv2.imshow('Edge Detected Image', edimg)
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()
    
   
def GrayscaleImageEdgeDetecting(imgPIL, threshold):
    #Make a copy of imgPIL to return the converted image
    edimg_tem = Image.new(imgPIL.mode, imgPIL.size)
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
            redx = 0
            redy = 0
            #---------#
            greenx = 0
            greeny = 0
            #---------#
            bluex = 0
            bluey = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    #Get information R-G-B at the pixel point in mask at postion [i, j]
                    r, g, b = np.uint8(imgPIL.getpixel((i,j))) #.getpixel returns int value
                    #Calculate the Edge Dectecting funtion in g(x)
                    redx += r * maskx[i, j]
                    greenx += g * maskx[i, j]
                    bluex += b * maskx[i, j]   
                    #Calculate the Edge Dectecting funtion in g(y)
                    redy += r * masky[i, j]
                    greeny += g * masky[i, j]
                    bluey += b * masky[i, j]
            #End up everything. We average all the value in each channel R-G-B
            #Get information R-G-B at the pixel point in mask at postion [i, j]
            gxx = (redx * redx) + (greenx * greenx) + (bluex * bluex)
            gyy = (redy * redy) + (greeny * greeny) + (bluey * bluey)
            gxy = (redx * redy) + (greenx * greeny) + (bluex * bluey)
            theta = math.atan2((2 * gxy), (gxx - gyy)) / 2
            F0 = math.sqrt(((gxx + gyy) + (gxx - gyy) * math.cos(2*theta) + (2 * gxy) * math.sin(2 * theta)) / 2)
            if (F0 <= threshold):
                #Set image pixel
                edimg_tem.putpixel((x, y), (0,0,0)) #put 0 channel first, then 1 and 2 respectively
            else:
                #Set image pixel
                edimg_tem.putpixel((x, y), (255, 255, 255)) #put 0 channel first, then 1 and 2 respectively
    edimg = np.array(edimg_tem)
    return edimg
main()