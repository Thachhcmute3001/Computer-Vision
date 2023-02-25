import cv2
from PIL import Image
import numpy as np
def main():
    while True:
        #Image path
        imgor = r'bird_small.jpg'
        #Read Image
        img = cv2.imread(imgor, cv2.IMREAD_COLOR)
        #Read color image using PIL library, which can replace OpenCV to process image
        imgPIL = Image.open(imgor)
        shpimg = ColorImageSharpening(imgPIL)
        #Show Original Image
        cv2.imshow('Original Image', img)
        #Show 3x3 Image
        cv2.imshow('Sharpened Image', shpimg)
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()
def ColorImageSharpening(imgPIL):
    c = 1
    #Make a copy of imgPIL to return the converted image
    shpimg_tem = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = shpimg_tem.size[0] #4 pics have the same dimension
    height = shpimg_tem.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    #Pay attention to 3x3 mask, to ease to code and not to be out of range (check the theory), we can abadon the border of image
    #So we just need to focus on x = 1 to x = width - 1, y = 1 to y = height - 1
    for x in range(1, width - 1): #0 -> width - 1
        for y in range(1, height - 1):
            #Create a maskmatrix
            mask = np.zeros((512,512), np.int8)
            mask[x - 1, y - 1] = 0; mask[x - 1, y] = -1; mask[x - 1, y + 1] = 0
            mask[x, y - 1] = -1; mask[x, y] = 4; mask[x, y + 1] = -1
            mask[x + 1, y - 1] = 0; mask[x + 1, y] = -1; mask[x + 1, y + 1] = 0 
            #Create variable to contain incremental value of pixel in mask. So they must be declared
            #"int" type to be able to contain those value.
            #Proceed to scan the points in the mask
            Rs = 0
            Gs = 0
            Bs = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    #Get information R-G-B at the pixel point in mask at postion [i, j]
                    r, g, b = np.uint8(imgPIL.getpixel((i,j))) #.getpixel returns int value
                    #Add up all the pixel value for each R-G-B channel respectively
                    Rs += r * mask[i, j]
                    Gs += g * mask[i, j]
                    Bs += b * mask[i, j]
            #End up everything. We average all the value in each channel R-G-B
            #Get information R-G-B at the pixel point in mask at postion [i, j]
            rimg, gimg, bimg = np.uint8(imgPIL.getpixel((x,y))) #.getpixel returns int value
            gRed = rimg + c * Rs
            gGreen = gimg + c * Gs
            gBlue = bimg + c * Bs
            #Set image pixel
            shpimg_tem.putpixel((x, y), (gBlue, gGreen, gRed)) #put 0 channel first, then 1 and 2 respectively
    shpimg = np.array(shpimg_tem)
    return shpimg
main()