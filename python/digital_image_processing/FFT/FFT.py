'''
컴퓨터정보통신공학전공 175704 박지연
FFT Filtering 소스코드
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

#이미지 불러오기
#이미지를 불러오는 과정에서 상대경로 지정에 문제가 있었음 -> 절대경로로 지정
img = cv2.imread("D:/jiyeon/jiyeon/building.jpeg")

#이미지의 R,G,B 성분을 분리, opencv에서는 BGR의 순서로 구성되어 있음
b,g,r = cv2.split(img)
#RGB의 순서로 이미지 재구성
img = cv2.merge([r, g, b])
#이미지를 gray scale로 변결
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
FFT = Fast Fourier Transform
-> 기존의 O(N^2)의 연산량을 가지는 DFT와는 달리 O(N*logN)의 적은 연산량을 가짐
-> 중심은 저주파, 주변은 고주파 영역을 나타내며 특정 주파수를 제거함을 통해 이미지 가공 가능
-> 중심의 저주파 제거: 이미지의 경계(edge)가 남음
-> 주변의 고주파 제거: 모아레 패턴 등을 제거 가능
'''

#이미지에 FFT 적용
f = np.fft.fft2(img)
#수월한 분석을 위해 주파수가 0인 부분 즉, 저주파 부분을 중앙으로 이동시킴
fshift = np.fft.fftshift(f)
#주파수 스펙트럼 계산
magnitude_spectrum = 20 * np.log(np.abs(fshift))

#이미지 행렬의 열의 개수, 행의 개수
rows, cols = img.shape
#int로 형변환하지 않으면 중심 좌표 계산에서 에러 발생
crow, ccol = int(rows / 2), int(cols / 2)

#중앙에서 10X10 사이즈의 값을 1로 설정함을 통해 중앙의 저주파를 제거
#-> 저주파 제거 = edge 검출
d = 10
fshift[crow - d : crow + d, ccol - d : ccol + d] = 1

#푸리에 역변환(주파수 -> 이미지)
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

img_new = np.uint8(img_back)
#threshold = 임계값을 적용
#cv2.threshold()-> 모든 픽셀에 대해 동일한 임계값을 적용
#cv2.THRESH_BINARY_INV = 흑백 이미지 -> 이진 이미지로 변환하기 위해 파라미터 설정
ret, thresh = cv2.threshold(img_new, 30, 225, cv2.THRESH_BINARY_INV)

#원본 이미지
plt.subplot(221), plt.imshow(img, cmap = 'gray')
plt.title("Original Image"), plt.xticks([]), plt.yticks([])

#원본 이미지의 주파수 스펙트럼
plt.subplot(222), plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title("Spectrum"), plt.xticks([]), plt.yticks([])

#원본 이미지의 푸리에 변환 결과(저주파 제거)
plt.subplot(223), plt.imshow(img_back, cmap = 'gray')
plt.title("Fourier Transform"), plt.xticks([]), plt.yticks([])

#threshold를 적용하여 이진 이미지로 변환한 결과
plt.subplot(224), plt.imshow(thresh, cmap = 'gray')
plt.title("Threshold with FT"), plt.xticks([]), plt.yticks([])

plt.show()