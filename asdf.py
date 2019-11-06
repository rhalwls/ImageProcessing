#[:,:]에서 y(height), x(width) 순
#input은 bgr로 주는ㄴ데 hsv로 바꾸는 것 권장
#bgr은 빛에 약하기 때문
#hsv는 명도를 분리(각각 255까지 범위)
#bgr의 8비트

#histogram은 단 하나의 값에 포커싱 해서 (주로 빛)
#numpy 인덱스 누적합
#numpy.ma = masking
#masking 해제

import cv2
import matplotlib.pyplot as plt
import numpy as np
def crop_numpy():
    img = cv2.imread('./picture/lena.jpg', cv2.IMREAD_COLOR)
    height, width, channels = img.shape

    crop_img = img[0:30, 0:80]

    cv2.imshow("img", img)
    cv2.imshow("crop img", crop_img)
    cv2.waitKey(0)


def cvt_hsv():
    img = cv2.imread('./picture/lena.jpg', cv2.IMREAD_COLOR)
    cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    cv2.imshow("img", img)

def histogram():
    img = cv2.imread('./picture/dirtypicture.png',cv2.IMREAD_GRAYSCALE)
    hist, bins = np.histogram(img.ravel(),245,[0,256])
    plt.plot(hist)
    plt.xlim([0,256])
    plt.show()

    cumsum = hist.cumsum()
    cumsum_masked = np.ma.masked_equal(cumsum,0)
    cumsum_masked = (cumsum_masked-cumsum_masked.min())*255/(cumsum_masked.max()-cumsum_masked.min())
    cumsum = np.ma.filled(cumsum_masked,0).astype('uint8')


    print(img.shape)
    h,w = img.shape
    img_equalization = np.zeros((h,w),dtype = 'uint8')
    for i in range(h):
        for j in range(w):
            cdf_index = img[i][j]
            #print("cdf_index is " ,cdf_index)
            img_equalization[i][j] = cumsum[cdf_index]

    cv2.imshow("equalization",img_equalization)
    cv2.waitKey(0)
    hist, bins = np.histogram(img_equalization.ravel(), 245, [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()



crop_numpy()
cvt_hsv()
histogram()