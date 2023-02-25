import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt #Drawing diagram library
import math
def main():
    while True:
        #Image path
        imgor = r'lena.jpg'
        #Read Image
        img = cv2.imread(imgor, cv2.IMREAD_COLOR)
        #Read color image using PIL library, which can replace OpenCV to process image to use PIL functions
        imgPIL = Image.open(imgor)
        YCrCb = RGBToYCrCbConvert(imgPIL)
        #Show Original Image
        cv2.imshow('Original Image', img)
        #Show Y Image
        cv2.imshow('Y Image', YCrCb[0])
        #Show Cr Image
        cv2.imshow('Cr Image', YCrCb[1])
        #Show Cb Image
        cv2.imshow('Cb Image', YCrCb[2])
        #Show YCrCb Image
        cv2.imshow('YCrCb Image', YCrCb[3])
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()

def RGBToYCrCbConvert(imgPIL):
    #Make a copy of imgPIL to return the converted image
    Y_tem = Image.new(imgPIL.mode, imgPIL.size)
    Cr_tem = Image.new(imgPIL.mode, imgPIL.size)
    Cb_tem = Image.new(imgPIL.mode, imgPIL.size)
    YCrCbimg_tem = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = Y_tem.size[0] #4 pics have the same dimension
    height = Y_tem.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #-------------------------------#
            #Y-Cr-Cb equations
            #The Y equation
            #Using np.uint8 to convert the value to usigned integer 8bit (byte in C#)
            Y = np.uint8(16 + (65.738 / 256)*r + (129.057 / 256)*g + (25.064 / 256)*b)
            #-------------------------------#
            #The Cr equation
            Cr = np.uint8(128 - (37.945 / 256)*r - (74.494 / 256)*g + (112.439 / 256)*b)
            #The Cb equation
            Cb = np.uint8(128 + (112.439 / 256)*r - (94.154 / 256)*g - (18.285 / 256)*b)
            #Assign the value for pic
            Y_tem.putpixel((x, y), (Y, Y, Y)) #putpixel(blue, green, red)
            Cr_tem.putpixel((x, y), (Cr, Cr, Cr))
            Cb_tem.putpixel((x, y), (Cb, Cb, Cb))
            YCrCbimg_tem.putpixel((x, y), (Cb, Cr, Y))
    #lumpic = np.array(lum)
    Y = np.array(Y_tem)
    Cr = np.array(Cr_tem)
    Cb = np.array(Cb_tem)
    YCrCbimg = np.array(YCrCbimg_tem)
    YCrCb = [Y, Cr, Cb, YCrCbimg]
    return YCrCb
main()