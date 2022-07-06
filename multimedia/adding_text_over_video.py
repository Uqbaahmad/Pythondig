import cv2

video = cv2.VideoCapture(0)                                   #index number and its open laptop camera        

while True:
    state, img = video.read()
    h,w,_ = img.shape
    print(w, h)
    if state:
        cv2.rectangle(img, (0,0), (260, 40), (0,255, 0), -1)
        cv2.putText(img, "Webcam", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
        cv2.putText(img,"Uqba", (10,h-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
        # 2 means font size , 1 means Scale , color range 0-255, cv2."Filter", 
        cv2.imshow("video output", img)
        if cv2.waitKey(1) == 27:                              #27 means keyboard esc button number 
            break                                             #if we press esc then video end otherwise video running till last
    else:
        break
video.release()
cv2.destroyAllWindows()        