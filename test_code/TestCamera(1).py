'''
test Camera
'''
import numpy as np
import cv2

cap=cv2.VideoCapture(0)  #0代表树莓派上自带的摄像头，1代表USB摄像头

#一下cap.set(),可以注释掉#
cap.set(3,320)#摄像头采集图像的宽度320
cap.set(4,240)#摄像头采集图像的高度240
cap.set(5,30) #摄像头采集图像的帧率fps为30

#查看采集图像的参数
print(cap.get(3))
print(cap.get(4))
print(cap.get(5))

while(True):
	ret,color_frame=cap.read()
	img1=cv2.flip(color_frame,0)  #翻转图像，0垂直翻转，1水平翻转，-1水平垂直翻转
	cv2.imshow('color_frame',img1)  #展示每一帧
	if cv2.waitKey(1)&0xff==ord('q'): #按Q键退出，可以改成任意键
		break
cap.release()
cv2.destroyAllWindows()
