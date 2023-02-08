import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt #Drawing diagram library
def main():
    while True:
        #Image path
        imgor = r'lena30.jpg'
        #Read Image
        img = cv2.imread(imgor, cv2.IMREAD_COLOR)
        #Read color image using PIL library, which can replace OpenCV to process image
        imgPIL = Image.open(imgor)
        img_tem = RGBToCMYKConvert(imgPIL)
        #Show Original Image
        cv2.imshow('Original Image', img)
        #Show Cyan Image
        cv2.imshow('Cyan Image', img_tem[0])
        #Show Magenta Image
        cv2.imshow('MAgenta Image', img_tem[1])
        #Show Yellow Image
        cv2.imshow('Yellow Image', img_tem[2])
        #Show Black Image
        cv2.imshow('Black Image', img_tem[3])
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()

def RGBToCMYKConvert(imgPIL):
    #Make a copy of imgPIL to return the converted image
    Cyan_tem = Image.new(imgPIL.mode, imgPIL.size)
    Magenta_tem = Image.new(imgPIL.mode, imgPIL.size)
    Yellow_tem = Image.new(imgPIL.mode, imgPIL.size)
    Black_tem = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = Cyan_tem.size[0] #4 pics have the same dimension
    height = Cyan_tem.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #Take the minimum R, G, B
            Min = min(r, g, b)
            #Assign the value for pic
            Cyan_tem.putpixel((x, y), (b, g, 0)) #putpixel(blue, green, red)
            Magenta_tem.putpixel((x, y), (b, 0, r))
            Yellow_tem.putpixel((x, y), (0, g, r))
            Black_tem.putpixel((x, y), (Min, Min, Min))
    #lumpic = np.array(lum)
    Cyan = np.array(Cyan_tem)
    Magenta = np.array(Magenta_tem)
    Yellow = np.array(Yellow_tem)
    Black = np.array(Black_tem)
    List = [Cyan, Magenta, Yellow, Black]
    return List
main()