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
        img_tem = RGBConvert(imgPIL)
        #Histogram Calculation
        hisPIL = HistogramCalculation(img_tem)
        
        #Show Image
        HistogramDiagram(hisPIL)
        cv2.imshow('Original Image', img)
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()
    
def RGBConvert(imgPIL):
    #Make a copy of imgPIL to return the converted image
    pic = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = pic.size[0]
    height = pic.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            #Get value of pixel at each position
            r, g, b = imgPIL.getpixel((x,y))
            #Assign the value for pic
            pic.putpixel((x, y), (r, g, b))
    #lumpic = np.array(lum)
    return pic
#Histogram Calculation of Grayscale Image
def HistogramCalculation(picPIL):
    hisred = np.zeros(256) #1-D matrix has 256 components for red channel
    hisgreen = np.zeros(256) #1-D matrix has 256 components for green channel
    hisblue = np.zeros(256) #1-D matrix has
    #Get Image dimension
    w = picPIL.size[0]
    h = picPIL.size[1]
    for x in range(w):
        for y in range(h):
            #Get grayscale value at position (x,y)
            R, G, B = picPIL.getpixel((x,y))
            hisred[R] += 1
            hisgreen[G] += 1
            hisblue[B] += 1    
    his = [hisred, hisgreen, hisblue]
    return his

#Draw histogram diagram using Matplotlib library
def HistogramDiagram(his):
    w = 5
    h = 4
    plt.figure("Histogram Diagram of RGB Image", figsize=((w,h)), dpi = 100)
    Xaxis = np.zeros(256)
    Xaxis = np.linspace(0, 256, 256)
    plt.plot(Xaxis, his[0], color = 'red')
    plt.plot(Xaxis, his[1], color = 'green')
    plt.plot(Xaxis, his[2], color = 'blue')
    plt.title("Histogram Diagram")
    plt.xlabel("Pixel value")
    plt.ylabel("Points have the same value of pixel")
    plt.show()    
main()
