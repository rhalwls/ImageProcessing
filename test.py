import cv2 as cv
import numpy as np

def main():
    img = cv.imread('./picture/lena.jpg',cv.IMREAD_COLOR)


    cv.imwrite('res/lenachan.jpg', img)

    #diagram
    cv.line(img, (30,30),(60,60),(255,0,0),3)
    cv.rectangle(img, (70,90),(100,100),(255,255,0),-1)
    cv.circle(img,(130,130),30,(0,0,255),2)
    pts = np.array([[10,5],[20,30],[5,10]],np.int32)

    cv.polylines(img, [pts],True,(0,255,255),2)
    cv.putText(img,'Opencv',(10,100),cv.FONT_HERSHEY_SIMPLEX,2,(255,255,255))

    cv.imshow('image', img)
    cv.waitKey(0)

    height,width,channels = img.shape
    print(img.shape)
main()