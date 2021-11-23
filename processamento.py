import cv2
from PIL import Image
import imutils
# import imFerramentas as imF

def contar(im):
    image = Image.fromarray(im);
    imr = image[:,:,2]
    # mask = cv2.bitwise_not(imF.limiarizacao(imr,70))
    ret,mask = cv2.threshold(imr,70,255,cv2.THRESH_BINARY_INV)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Raio do circulo a ser desenhado
    radius = 10
    
    # Cor amarelo
    color = (0, 0, 255) 

    # Espessura da linha do circulo
    thickness = 2

    # copia para não alterar a imagem original
    image_circles = image.copy()

    # Desenhar o circulo em cada centro
    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
        # set values as what you need in the situation
            cX, cY = 0, 0
        # Center coordinates 
        center_coordinates = (cX, cY) 
        image_circles = image = cv2.circle(image_circles, center_coordinates, radius, color, thickness)

    return image_circles.tostring(), len(cnts)