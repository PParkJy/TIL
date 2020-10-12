'''
컴퓨터정보통신공학전공 175704 박지연
1) 어두운 영상의 Equalization
2) zero-crossing을 통한 야외 건물의 Edge 구하기
'''

import cv2
import numpy as np
import matplotlib.pyplot as mpt

# 1.Equalization
#cv2.imread로 이미지를 불러오되 IMREAD_GRAYSCALE 속성을 추가하여 흑백 이미지로 읽어온다.
cvGrayImg1 = cv2.imread("wallet.jpg", cv2.IMREAD_GRAYSCALE)
#cv2.equalizaHist로 흑백 이미지에 히스토그램 평활화를 적용한다.
eqImg = cv2.equalizeHist(cvGrayImg1)

'''
이미지의 히스토그램 계산 = calcHist(images, channels, mask, histSize, ranges)
images = 히스토그램을 계산할 배열 형태의 이미지
channels = 분석 채널, grayscale일 시 [0], color일 시 [0],[0,1]
mask = 이미지의 분석 영역, None으로 설정할 시 전체 영역
histSize = BINS(히스토그램 X축의 간격), 색이 0~255 사이로 표현되므로 256
ranges = 측정하고자 하는 값의 범위
'''
#흑백 이미지의 히스토그램
cvHist1 = cv2.calcHist([cvGrayImg1], [0], None, [256], [0, 256])
#평활화를 적용한 이미지의 히스토그램
cvHist2 = cv2.calcHist([eqImg], [0], None, [256], [0, 256])

'''
mpt.subplot -> 한 창에 여러 그래프(or 이미지)를 표현
mpt.imshow -> 이미지 그린다. 'gray'는 color map의 요소로 회색을 설정한 것으로 흑백 이미지의 처리를 나타낸다. 
mpt.plot -> 그래프를 그린다. (여기에선 히스토그램)
mpt.title -> 해당 그래프(or 이미지)의 제목을 설정한다.
mpt.show -> 창을 표시한다. 
'''
mpt.subplot(221), mpt.imshow(cvGrayImg1, 'gray'), mpt.title('Source Image')
mpt.subplot(222), mpt.plot(cvHist1), mpt.title('OpenCV1 Histogram')
mpt.subplot(223), mpt.imshow(eqImg, 'gray'), mpt.title('Equalized Image')
mpt.subplot(224), mpt.plot(cvHist2), mpt.title('OpenCv2 Histogram')
mpt.show()

#실행된 창을 모두 종료한다.
cv2.destroyAllWindows()

#2.Zero-crossing (Laplacian Mask)
#cv2.imread로 이미지를 불러오되 IMREAD_GRAYSCALE 속성을 추가하여 흑백 이미지로 읽어온다.
cvGrayImg2 = cv2.imread("building.jpeg",cv2.IMREAD_GRAYSCALE)

'''
이미지에 라플라시안 마스크 적용 = cv2.Laplacian(src, ddepth)
라플라시안 = 이미지의 가로, 세로에 대해 2차 미분 적용
src -> 적용하고자 하는 배열 형태의 이미지
ddepth -> 출력 이미지의 depth, -1일 경우 src와 동일
'''
dstImg = cv2.Laplacian(cvGrayImg2, -1)

'''
mpt.subplot -> 한 창에 여러 그래프(or 이미지)를 표현
mpt.imshow -> 이미지 그린다. 'gray'는 color map의 요소로 회색을 설정한 것으로 흑백 이미지의 처리를 나타낸다. 
mpt.xticks -> x축 파라미터 설정
mpt.yticks -> y축 파라미터 설정
mpt.title -> 해당 그래프(or 이미지)의 제목을 설정한다.
mpt.show -> 창을 표시한다. 
'''
mpt.subplot(121), mpt.imshow(cvGrayImg2, 'gray'), mpt.title('Original Image')
mpt.xticks([]), mpt.yticks([])
mpt.subplot(122), mpt.imshow(dstImg, 'gray'), mpt.title('Laplacian Image')
mpt.xticks([]), mpt.yticks([])
mpt.show()

#실행된 창을 모두 종료한다.
cv2.destroyAllWindows()

#3.Zero-crossing (LoG, Laplacian of Gaussian)
#마스크 사이즈
msize = 3
#정규분포의 표준편차
sigma = 0.3*((msize - 1)*0.5 - 1) + 0.8
'''
노이즈 제거를 위해 가우시안 필터를 사용해 블러링 = GaussianBlur(src, ksize, sigmaX, sigmaY)
src =  원본 이미지
ksize = 필터의 커널 크기
sigmaX = X축 방향의 표준편차
sigmaY = Y축 방향의 표준편차, 0일 경우 sigmaX와 동일하게 설정
'''
blurImg = cv2.GaussianBlur(cvGrayImg2, (msize, msize), sigma, 0)
#라플라시안 마스크와 동일
dstImg = cv2.Laplacian(blurImg, -1)

#라플라시안 마스크와 동일
mpt.subplot(121), mpt.imshow(cvGrayImg2, 'gray'), mpt.title('Original Image')
mpt.xticks([]), mpt.yticks([])
mpt.subplot(122), mpt.imshow(dstImg, 'gray'), mpt.title('Laplacian Image')
mpt.xticks([]), mpt.yticks([])
mpt.show()

#실행된 모든 창을 종료한다.
cv2.destroyAllWindows()


# 4.test
mask = np.array(([0, 1, 0], [1, -4, 1], [0, 1, 0]), dtype=np.float32)
dstImg = cv2.filter2D(cvGrayImg2, -1, mask)

mpt.subplot(121), mpt.imshow(cvGrayImg2, 'gray'), mpt.title('Original Image')
mpt.xticks([]), mpt.yticks([])
mpt.subplot(122), mpt.imshow(dstImg, 'gray'), mpt.title('Laplacian Image')
mpt.xticks([]), mpt.yticks([])
mpt.show()

cv2.destroyAllWindows()