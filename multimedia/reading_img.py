import cv2

im = cv2.imread('multimedia/tokyo_small.png')
print(im.shape)
cv2.imshow("Iamge window", im)
cv2.waitKey(0)