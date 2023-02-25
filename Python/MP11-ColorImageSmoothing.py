import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt #Drawing diagram library
def main():
    while True:
        #Image path
        imgor = r'bird_small.jpg'
        #Read Image
        img = cv2.imread(imgor, cv2.IMREAD_COLOR)
        #Read color image using PIL library, which can replace OpenCV to process image
        imgPIL = Image.open(imgor)
        img_tem3x3 = ColorImageSmoothing3x3(imgPIL)
        img_tem5x5 = ColorImageSmoothing5x5(imgPIL)
        img_tem7x7 = ColorImageSmoothing7x7(imgPIL)
        img_tem9x9 = ColorImageSmoothing9x9(imgPIL)
        #Show Original Image
        cv2.imshow('Original Image', img)
        #Show 3x3 Image
        cv2.imshow('Smooth Image 3x3', img_tem3x3)
        #Show 5x5 Image
        cv2.imshow('Smooth Image 5x5', img_tem5x5)
        #Show 7x7 Image
        cv2.imshow('Smooth Image 7x7', img_tem7x7)
        #Show 9x9 Image
        cv2.imshow('Smooth Image 9x9', img_tem9x9)
        #Quit key
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()
def ColorImageSmoothing3x3(imgPIL):
    #Make a copy of imgPIL to return the converted image
    sm3x3_tem = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = sm3x3_tem.size[0] #4 pics have the same dimension
    height = sm3x3_tem.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    #Pay attention to 3x3 mask, to ease to code and not to be out of range (check the theory), we can abadon the border of image
    #So we just need to focus on x = 1 to x = width - 1, y = 1 to y = height - 1
    for x in range(1, width - 1): #0 -> width - 1
        for y in range(1, height - 1):
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
                    Rs += r #Rs = Rs + r
                    Gs += g
                    Bs += b
            K = 3 * 3
            #End up everything. We average all the value in each channel R-G-B
            Rs = int(Rs / K)
            Gs = int(Gs / K)
            Bs = int(Bs / K)
            #Set image pixel
            sm3x3_tem.putpixel((x, y), (Bs, Gs, Rs)) #put 0 channel first, then 1 and 2 respectively
    sm3x3 = np.array(sm3x3_tem)
    return sm3x3
def ColorImageSmoothing5x5(imgPIL):
    #Make a copy of imgPIL to return the converted image
    sm5x5_tem = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = sm5x5_tem.size[0] #4 pics have the same dimension
    height = sm5x5_tem.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    #Pay attention to 3x3 mask, to ease to code and not to be out of range (check the theory), we can abadon the border of image
    #So we just need to focus on x = 1 to x = width - 1, y = 1 to y = height - 1
    for x in range(2, width - 2):
        for y in range(2, height - 2):
            #Create variable to contain incremental value of pixel in mask. So they must be declared
            #"int" type to be able to contain those value.
            #Proceed to scan the points in the mask
            Rs = 0
            Gs = 0
            Bs = 0
            for i in range(x - 2, x + 3):
                for j in range(y - 2, y + 3):
                    #Get information R-G-B at the pixel point in mask at postion [i, j]
                    r, g, b = imgPIL.getpixel((i,j)) #.getpixel returns int value
                    #Add up all the pixel value for each R-G-B channel respectively
                    Rs += r
                    Gs += g
                    Bs += b
            K = 5 * 5
            #End up everything. We average all the value in each channel R-G-B
            Rs = int(Rs / K)
            Gs = int(Gs / K)
            Bs = int(Bs / K)
            #Set image pixel
            sm5x5_tem.putpixel((x, y), (Bs, Gs, Rs))
    sm5x5 = np.array(sm5x5_tem)
    return sm5x5
def ColorImageSmoothing7x7(imgPIL):

    #Make a copy of imgPIL to return the converted image
    sm7x7_tem = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = sm7x7_tem.size[0] #4 pics have the same dimension
    height = sm7x7_tem.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    #Pay attention to 7x7 mask, to ease to code and not to be out of range (check the theory), we can abadon the border of image
    #So we just need to focus on x = 3 to x = width - 3, y = 3 to y = height - 3
    for x in range(3, width - 3):
        for y in range(3, height - 3):
            #Create variable to contain incremental value of pixel in mask. So they must be declared
            #"int" type to be able to contain those value.
            #Proceed to scan the points in the mask
            Rs = 0
            Gs = 0
            Bs = 0
            for i in range(x - 3, x + 4):
                for j in range(y - 3, y + 4):
                    #Get information R-G-B at the pixel point in mask at postion [i, j]
                    r, g, b = imgPIL.getpixel((i,j)) #.getpixel returns int value
                    #Add up all the pixel value for each R-G-B channel respectively
                    Rs += r
                    Gs += g
                    Bs += b
            K = 7 * 7
            #End up everything. We average all the value in each channel R-G-B
            Rs = int(Rs / K)
            Gs = int(Gs / K)
            Bs = int(Bs / K)
            #Set image pixel
            sm7x7_tem.putpixel((x, y), (Bs, Gs, Rs))
    sm7x7 = np.array(sm7x7_tem)
    return sm7x7
def ColorImageSmoothing9x9(imgPIL):

    #Make a copy of imgPIL to return the converted image
    sm9x9_tem = Image.new(imgPIL.mode, imgPIL.size)
    #Take the image dimension
    width = sm9x9_tem.size[0] #4 pics have the same dimension
    height = sm9x9_tem.size[1]
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    #Pay attention to 9x9 mask, to ease to code and not to be out of range (check the theory), we can abadon the border of image
    #So we just need to focus on x = 4 to x = width - 4, y = 4 to y = height - 4
    for x in range(4, width - 4):
        for y in range(4, height - 4):
            #Create variable to contain incremental value of pixel in mask. So they must be declared
            #"int" type to be able to contain those value.
            #Proceed to scan the points in the mask
            Rs = 0
            Gs = 0
            Bs = 0
            for i in range(x - 4, x + 5):
                for j in range(y - 4, y + 5):
                    #Get information R-G-B at the pixel point in mask at postion [i, j]
                    r, g, b = imgPIL.getpixel((i,j)) #.getpixel returns int value
                    #Add up all the pixel value for each R-G-B channel respectively
                    Rs += r
                    Gs += g
                    Bs += b
            K = 9 * 9
            #End up everything. We average all the value in each channel R-G-B
            Rs = int(Rs / K)
            Gs = int(Gs / K)
            Bs = int(Bs / K)
            #Set image pixel
            sm9x9_tem.putpixel((x, y), (Bs, Gs, Rs))
    sm9x9 = np.array(sm9x9_tem)
    return sm9x9
main()