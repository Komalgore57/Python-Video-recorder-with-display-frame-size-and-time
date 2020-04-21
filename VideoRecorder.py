import cv2
import datetime
cap=cv2.VideoCapture(0)
cap.set(3,1000)
cap.set(4,1000)
k=0


while(k!=27):
    ret,fram=cap.read()
    font=cv2.FONT_HERSHEY_COMPLEX
    date=str(datetime.datetime.now())
    fram=cv2.putText(fram,'Width='+str(cap.get(3))+',',(0,20),font,0.5,(255,255,255),1,cv2.LINE_AA)
    fram=cv2.putText(fram,'Height='+str(cap.get(4)),(120,20),font,0.5,(255,255,255),1,cv2.LINE_AA)
    fram=cv2.putText(fram,'Date='+date,(0,40),font,0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow("komal",fram)
    k=cv2.waitKey(1)
cv2.destroyAllWindows()
cap.release()
