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
        HSV = RGBToHSVConvert(imgPIL)
        #Show Original Image
        cv2.imshow('Original Image', img)
        #Show Hue Image
        cv2.imshow('Hue Image', HSV[0])
        #Show Saturation Image
        cv2.imshow('Saturation Image', HSV[1])
        #Show Value Image
        cv2.imshow('Value Image', HSV[2])
        #Show HSV Image
        cv2.imshow('HSV Image', HSV[3])
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()

def RGBToHSVConvert(imgPIL):
    #Make a copy of imgPIL to return the converted image
    Hue_tem = Image.new(imgPIL.mode, imgPIL.size)
    Saturation_tem = Image.new(imgPIL.mode, imgPIL.size)
    Value_tem = Image.new(imgPIL.mode, imgPIL.size)
    HSVimg_tem = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = Hue_tem.size[0] #4 pics have the same dimension
    height = Hue_tem.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #-------------------------------#
            #H-S-V equations
            #Numerator
            num = ((r - g) + (r - b)) / 2
            #Denominator
            deno = math.sqrt((r - g) * (r - g) + (r - b) * (g - b))
            #The return value of Acos function in C#.NET is radian
            theta = math.acos(num / deno)
            #-------------------------------#
            #The Hue equation
            if (b <= g): 
                H = np.uint8(theta)
            elif (b > g): 
                H = (2 * math.pi) - theta
            #Convert radian to degree
            H = np.uint8(H * 180 / math.pi) #Using np.uint8 to convert the value to usigned integer 8bit (byte in C#)
            #-------------------------------#
            #The saturation equation
            #Take the minimum R, G, B
            Min = min(r, g, b)
            #Main equation
            S = 1 - (3 * Min / (r + g + b))
            #Because the value we take from above equation is in range [0,1]
            #To show it, we need to convert S to the range[0, 255]
            S = np.uint8(S * 255) #Using np.uint8 to convert the value to usigned integer 8bit (byte in C#)
            #The Value equation
            #is the maximum value of R, G, B
            V = max(r, g, b) #Using np.uint8 to convert the value to usigned integer 8bit (byte in C#)
            
            #Assign the value for pic
            Hue_tem.putpixel((x, y), (H, H, H)) #putpixel(blue, green, red)
            Saturation_tem.putpixel((x, y), (S, S, S))
            Value_tem.putpixel((x, y), (V, V, V))
            HSVimg_tem.putpixel((x, y), (V, S, H))
    #lumpic = np.array(lum)
    Hue = np.array(Hue_tem)
    Saturation = np.array(Saturation_tem)
    Value = np.array(Value_tem)
    HSVimg = np.array(HSVimg_tem)
    HSV = [Hue, Saturation, Value, HSVimg]
    return HSV
main()