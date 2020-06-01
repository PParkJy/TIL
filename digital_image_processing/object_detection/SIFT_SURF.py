import cv2 
from matplotlib import pyplot as plt

#이미지 파일 읽기
img = cv2.imread('wallet.jpg')
other_img = cv2.imread('other_wallet.jpg')

#grayscale로 변환
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
other_gray = cv2.cvtColor(other_img, cv2.COLOR_BGR2GRAY)

plt.subplot(221), plt.imshow(img)
plt.title("Original Image"), plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(other_img)
plt.title("Other Image"), plt.xticks([]), plt.yticks([])


'''
SIFT를 사용할 경우
sift = cv2.xfeature2d.SIFT_create()
key_point, des = sift.detectAndCompute(img, None)
'''

#SURF 클래스 사용
surf = cv2.xfeatures2d.SURF_create()
#SURF를 통한 특징점 검출
key_point1 = surf.detect(img_gray, None)
key_point2 = surf.detect(other_gray, None)
#이미지에 검출된 특징점 그리기
detect_img = cv2.drawKeypoints(img_gray, key_point1, img, flags = cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
detect_other = cv2.drawKeypoints(other_gray, key_point2, other_img, flags = cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)

'''
다른 방식으로 SURF 사용
img = cv2.imread('phone.jpg', cv2.IMREAD_GRAYSCALE)
key_point, des = surf.detectAndCompute(img, None)
detect_img = cv2.drawKeypoints(img, key_point, None, (255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
'''

plt.subplot(223), plt.imshow(detect_img)
plt.title("SURF original detect"), plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.imshow(detect_other)
plt.title("SURF other detect"), plt.xticks([]), plt.yticks([])
plt.show()

