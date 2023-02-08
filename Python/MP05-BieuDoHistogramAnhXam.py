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
        #Assign value for image
        lumpic_tem = RGBLuminaceConvert(imgPIL)
        
        #Histogram Calculation
        hisPIL = HistogramCalculation(lumpic_tem)
        #Convert PIL to opencv to show in opencv library
        graypic = np.array(lumpic_tem)      
        #Show Image
        cv2.imshow('Luminace Grayscale Image', graypic)
        HistogramDiagram(hisPIL)
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
    #lumpic = np.array(lum)
    return lum

#Histogram Calculation of Grayscale Image
def HistogramCalculation(graypicPIL):
    his = np.zeros(256) #1-D matrix has 256 components
    #Get Image dimension
    w = graypicPIL.size[0]
    h = graypicPIL.size[1]
    for x in range(w):
        for y in range(h):
            #Get grayscale value at position (x,y)
            gR, gG, gB = graypicPIL.getpixel((x,y))
            his[gR] += 1
    return his

#Draw histogram diagram using Matplotlib library
def HistogramDiagram(his):
    
    w = 5
    h = 4
    plt.figure("Histogram Diagram of Grayscale Image", figsize=((w,h)), dpi = 100)
    Xaxis = np.zeros(256)
    Xaxis = np.linspace(0, 256, 256)
    plt.plot(Xaxis, his, color = 'orange')
    plt.title("Histogram Diagram")
    plt.xlabel("Grayscale value")
    plt.ylabel("Points have the same value of grayscale")
    plt.show()
main()
