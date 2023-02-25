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
        XYZ = RGBToXYZConvert(imgPIL)
        #Show Original Image
        cv2.imshow('Original Image', img)
        #Show X Image
        cv2.imshow('X Image', XYZ[0])
        #Show Y Image
        cv2.imshow('Y Image', XYZ[1])
        #Show Z Image
        cv2.imshow('Z Image', XYZ[2])
        #Show XYZ Image
        cv2.imshow('XYZ Image', XYZ[3])
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()

def RGBToXYZConvert(imgPIL):
    #Make a copy of imgPIL to return the converted image
    X_tem = Image.new(imgPIL.mode, imgPIL.size)
    Y_tem = Image.new(imgPIL.mode, imgPIL.size)
    Z_tem = Image.new(imgPIL.mode, imgPIL.size)
    XYZimg_tem = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = X_tem.size[0] #4 pics have the same dimension
    height = X_tem.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #-------------------------------#
            #X-Y-Z equations
            #The X equation
            #Using np.uint8 to convert the value to usigned integer 8bit (byte in C#)
            X = np.uint8(0.4124564*r + 0.3575761*g + 0.1804375*b) 
            #-------------------------------#
            #The Y equation
            Y = np.uint8(0.2126729*r + 0.7151522*g + 0.0721750*b)
            #The Z equation
            Z = np.uint8(0.0193339*r + 0.1191920*g + 0.9503041*b)
            #Assign the value for pic
            X_tem.putpixel((x, y), (X, X, X)) #putpixel(blue, green, red)
            Y_tem.putpixel((x, y), (Y, Y, Y))
            Z_tem.putpixel((x, y), (Z, Z, Z))
            XYZimg_tem.putpixel((x, y), (Z, Y, X))
    #lumpic = np.array(lum)
    X = np.array(X_tem)
    Y = np.array(Y_tem)
    Z = np.array(Z_tem)
    XYZimg = np.array(XYZimg_tem)
    XYZ = [X, Y, Z, XYZimg]
    return XYZ
main()