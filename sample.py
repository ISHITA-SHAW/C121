import cv2
cap = cv2.VideoCapture(0)
while True:
    try:
        ret,frame = cap.read()
        grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        height,width = grey.shape
        ul = (int(width/2-56),int(height/2-56))
        br = (int(width/2+56),int(height/2+56))
        cv2.rectangle(grey,ul,br,(255,12,52),2)
        cv2.imshow("output",grey)
    except Exception as e:
        pass
    key = cv2.waitKey(25)
    if key==32:
        break
cap.release()
cv2.destroyAllWindows()

        

