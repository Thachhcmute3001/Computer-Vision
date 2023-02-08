import cv2
from PIL import Image
import numpy as np
def main():
    while True:
        #Image path
        imgor = r'lena.jpg' 
        #Read Image
        img = cv2.imread(imgor, cv2.IMREAD_COLOR)
        #Read color image using PIL library, which can replace OpenCV to process image
        imgPIL = Image.open(imgor)
        #Assign value for image
        lgtpic_tem = RGBLightnessConvert(imgPIL)
        lumpic_tem = RGBLuminaceConvert(imgPIL)
        bnpic_tem = RGBAverageConvert(imgPIL)
        '''#Concatanate image Vertically
        Vert1 = np.concatenate((img, lgtpic_tem), axis = 0)
        #Window size
        imS1 = cv2.resize(Vert1, (250,250))
        
        #Concatanate image Vertically
        Vert2 = np.concatenate((lumpic_tem, avgpic_tem), axis = 0)
        #Window size
        imS2 = cv2.resize(Vert2, (250,250))
        
        #Concatanate image Horizontally
        Horiz = np.concatenate((imS1, imS2), axis = 1)
        #Window size
        imS3 = cv2.resize(Horiz, (700,700))'''
        
        #Show Image
        cv2.imshow('Lightness Grayscale Image', lgtpic_tem)
        cv2.imshow('Average Grayscale Image', bnpic_tem)
        cv2.imshow('Luminace Grayscale Image', lumpic_tem)
        cv2.imshow('Original Image', img)
        
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()
    
def RGBAverageConvert(imgPIL):
    #Make a copy of imgPIL to return the converted image
    bn = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = bn.size[0]
    height = bn.size[1]
    #Establish a thresh hold value to calculate the binary position
    threshold = 100
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #Using Average method with following equation
            gray = np.uint8((r + g + b) / 3) #Using np.uint8 to convert the value to usigned integer 8bit (byte in C#)
            
            #Identify the binary value
            if (gray < threshold):
                #Assign the gray value for avg 
                bn.putpixel((x, y), (0, 0, 0))
            else:
                #Assign the gray value for avg 
                bn.putpixel((x, y), (255, 255, 255))
    bnpic = np.array(bn)
    return bnpic

def RGBLightnessConvert(imgPIL):
    #Make a copy of imgPIL to return the converted image
    lgt = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = lgt.size[0]
    height = lgt.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #Using Lightness method with following equation
            Min = min(r, g, b)
            Max = max(r, g, b)
            gray = np.uint8((Min + Max) / 2) #Using np.uint8 to convert the value to usigned integer 8bit (byte in C#)
            #Assign the gray value for avg 
            lgt.putpixel((x, y), (gray, gray, gray))
    lgtpic = np.array(lgt)
    return lgtpic

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
    lumpic = np.array(lum)
    return lumpic
main()
