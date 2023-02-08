import cv2
import numpy as np

while True:
    #Read Image
    img = cv2.imread('lena30.jpg', cv2.IMREAD_COLOR)
    #Get Image dimension
    height, width, channel = img.shape #img.shape returns a tuple of three values representing (height, width, channels),
    
    #3 matrixes for red green blue image
    red = np.zeros((height, width, 3), np.uint8) # '3' means that 3 channel including R-G-B, each has 8bit
    green = np.zeros((height, width, 3), np.uint8)
    blue = np.zeros((height, width, 3), np.uint8)
    
    #Each picture is a 2-dimension matrix so we'll use 2 for loops to read all of the pixels in each picture
    for x in range(width):
        for y in range(height):
            
            #Get the value at the position (x, y)
            R = img[y, x, 2]
            G = img[y, x, 1]
            B = img[y, x, 0]
            
            #Establish color for each channel
            red[y, x, 2] = R
            green[y, x, 1] = G
            blue[y, x, 0] = B
    #Concatanate image Vertically
    Vert1 = np.concatenate((red, green), axis = 0)
    #Window size
    imS1 = cv2.resize(Vert1, (250,250))
    
    #Concatanate image Vertically
    Vert2 = np.concatenate((img, blue), axis = 0)
    #Window size
    imS2 = cv2.resize(Vert2, (250,250))
    
    #Concatanate image Horizontally
    Horiz = np.concatenate((imS2, imS1), axis = 1)
    #Window size
    imS3 = cv2.resize(Horiz, (800,800))
    #Show Image
    cv2.imshow('Image', imS3)
    
    #Quit key
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cv2.destroyAllWindows()
