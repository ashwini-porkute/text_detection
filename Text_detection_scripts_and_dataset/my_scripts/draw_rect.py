import cv2
import sys

image_path = "/home/ashwini/TextDetection_MobilenetSSD/Final_Human_Dataset/PC_inference/img/00eba99def1218eb.jpg"
I = cv2.imread(image_path)
print(I.shape)


# (int(x-w/2), int(y-h/2)), (int(x+w/2), int(y+w/2))
cv2.rectangle(I,(73,20),(142,167),(255,255,0), 2)
cv2.rectangle(I,(149,8),(224,162),(255,255,0), 2)
cv2.imshow("result",I)
cv2.imwrite("result.jpg",I)
cv2.waitKey(0)
