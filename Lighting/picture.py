import cv2
import numpy as np

img = cv2.imread('musedash_final_Colored_Lines.png', cv2.IMREAD_UNCHANGED)

size=(10,10)
#size=(40,20)
#size=(80,40)
resized = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
cv2.imwrite('resized_image.png',resized)

cap = cv2.VideoCapture('pred_video_compressed2.mp4')
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fc = 0
ret = True

buffer = []
while (fc < frameCount and ret):
    ret, frame = cap.read()
    buffer.append(cv2.resize(frame, size, interpolation = cv2.INTER_AREA))
    fc += 1

cap.release()

size=(10,10)
row = 0
current_LED = 0
for i in range(size[1]):
    for j in range(size[0]):
        print(current_LED)
        if (i % 2) == 0:
            print(frame[i,row+j])
        else:
            print(frame[i,size[0]+row-j-1])
        current_LED += 1
    row += size[0]