import cv2

video = cv2.VideoCapture(0)                                   #index number and its open laptop camera        

while True:
    state, img = video.read()
    if state:
        cv2.imshow("video output", img)
        if cv2.waitKey(1) == 27:                              #27 means keyboard esc button number 
            break                                             #if we press esc then video end otherwise video running till last
    else:
        break
video.release()
cv2.destroyAllWindows()        