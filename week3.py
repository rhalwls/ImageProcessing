import numpy as np

import cv2

#salt pepper noise
img = cv2.imread('./input/saltAndPepper.png', cv2.IMREAD_GRAYSCALE)
ret = cv2.medianBlur(img,7)
cv2.imshow("salt&pepper",ret)
cv2.waitKey(0)


#gaussian
img =  cv2.imread('./input/saltAndPepper.png', cv2.IMREAD_GRAYSCALE)
gau_ret = cv2.GaussianBlur(img, (21,21),0)
cv2.imshow("gaussian",gau_ret)
cv2.waitKey(0)


#global thresholding
glo_img = cv2.imread('./input/globalMap.png', cv2.IMREAD_GRAYSCALE)
thresh, converted_glo = cv2.threshold(glo_img, 100, 150, cv2.THRESH_BINARY)
cv2.imshow("global thresholding ",converted_glo)
cv2.waitKey(0)

#스도쿠
sdo_img = cv2.imread('./input/shadowedImage.png',cv2.IMREAD_GRAYSCALE)
dst = cv2.adaptiveThreshold(sdo_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)
cv2.imshow("adaptive thresholding ",dst)
cv2.waitKey(0)

#opening
img = cv2.imread('./input/binaryOuterIssue.png',cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3,3), np.uint8)
grad = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow("opening",grad)
cv2.waitKey(0)

img =cv2.imread('./input/binaryInnerIssue.png',cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3,3), np.uint8)
grad = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow("opening",grad)
cv2.waitKey(0)

img = cv2.imread('./input/character.png',cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3,3), np.uint8)
grad = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("opening",grad)
cv2.waitKey(0)
grad = cv2.erode(img,kernel,3)
cv2.imshow("opening",grad)
cv2.waitKey(0)
grad = cv2.dilate(img,kernel,5)
cv2.imshow("opening",grad)
cv2.waitKey(0)

