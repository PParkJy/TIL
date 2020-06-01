import cv2
from matplotlib import pyplot as plt
import time

filename = "./moving_wallet2.mp4"
video = cv2.VideoCapture(filename)
temp = []

while(video.isOpened()):
    #ret = True or False
    #frame = 영상의 한 프레임
    ret, frame = video.read()
    
    if ret:
        #grayscale로 변환
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        temp.append(frame_gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

video_list = []
#일정 간격으로 프레임 저장
for i in range(0, len(temp), 30):
    video_list.append(temp[i])

#SURF 클래스 사용    
surf = cv2.xfeatures2d.SURF_create()

#현재 프레임과 이전 프레임의 특징점을 반복해서 비교
for i in range(len(video_list) - 1):
    kp1, des1 = surf.detectAndCompute(video_list[i], None)
    kp2, des2 = surf.detectAndCompute(video_list[i+1], None)    
    #Brute-Force 매칭
    bf = cv2.BFMatcher()
    #사용자가 지정한 k개의 가장 좋은 매칭 결과 
    matches = bf.knnMatch(des1, des2, k=2)
    mt = []

    #특징점을 계산하는 점수가 높은 순서대로 정렬
    for m,n in matches:
        if m.distance < 0.3 * n.distance:
            mt.append([m])

    #2개의 이미지 간의 동일 특징점을 선으로 연결하여 표시
    img3 = cv2.drawMatchesKnn(video_list[i], kp1, video_list[i+1], kp2, mt[:15], None, flags=2)    
    plt.imshow(img3)
    plt.show()
    plt.close('all')
