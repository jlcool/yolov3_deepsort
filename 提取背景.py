import cv2

# 这里我们取视频的第一帧来进行标注。注意⚠️不要使用截图，因为截图会使的图像大小不一致。
vidcap = cv2.VideoCapture(
    'D:\\Documents\\Projects\\Python\\yolov3_deepsort\\data\\video\\1874.MOV')
success, image = vidcap.read()
n = 1
while n < 30:
    success, image = vidcap.read()
    image = cv2.flip(image, 0)
    n += 1

imag = cv2.imwrite('fff.png', image)
if imag == True:
    print('ok')
