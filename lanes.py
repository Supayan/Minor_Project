import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(img):
    grey=cv2.cvtColor(lane_img,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(grey,(5,5),0)

    #canny : It will perform a derivative and measure the adjacent changes in intensity in all directions, x and y
    canny=cv2.Canny(blur, 50,150)
    return canny

def region_of_interest(img):
    height=img.shape[0]
    poly=np.array([[(50,height),(280,height),(150,95)]])
    mask=np.zeros_like(img)
    cv2.fillPoly(mask,poly,255)
    return mask

img= cv2.imread('images.jpg')
lane_img=np.copy(img)
canny=canny(lane_img)
cv2.imshow('result', region_of_interest(canny))
cv2.waitKey(0)
cv2.destroyAllWindows()