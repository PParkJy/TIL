'''
My face image's brightness transformation (reduction)
'''

import cv2
from PIL import Image
from PIL import ImageTk
#if you use "from tkinter import *" then, the upper line "from PIL import Image" doesen't act.
#so, "from ~~ import *" should be used with care.
from tkinter import Tk,Label
from tkinter import font

filename = "your file path"

window = Tk()
window.title("JIYEON PARK")
window.geometry("500x500")

cvGrayImg = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
cvGrayImg = cv2.resize(cvGrayImg,(270,329))

h,w = cvGrayImg.shape
for y in range(h):
    for x in range(w):
        tp = cvGrayImg[y,x] - 30
        if tp < 0:
            tp = 0
        cvGrayImg[y,x] = tp

#tkinter = RGB
#openCV = BRG
cvGrayImg = cv2.cvtColor(cvGrayImg, cv2.COLOR_BGR2RGB)
#numpy -> Image
cvGrayImg = Image.fromarray(cvGrayImg)
#Image -> tkinter's object
cvGrayImg = ImageTk.PhotoImage(cvGrayImg)

label_img = Label(image=cvGrayImg)
label_img.pack()

label_name = Label(text="성명: ---",font=font.Font(family="맑은 고딕",size=15))
label_name.pack()

label_id = Label(text=" 학번: ------",font=font.Font(family="맑은 고딕",size=15))
label_id.pack()

label_hobby = Label(text="       취미: ------",font=font.Font(family="맑은 고딕",size=15))
label_hobby.pack()

label_good = Label(text="특기: ---",font=font.Font(family="맑은 고딕",size=15))
label_good.pack()

window.mainloop()

