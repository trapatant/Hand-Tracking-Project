#Hand Tracking Project
import cv2
import time
import mediapipe as mp

cap=cv2.VideoCapture(0)

mpHand=mp.solutions.hands

hands=mpHand.Hands()

mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0

while True:
    success, img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)
            
            for id,lm in enumerate(handLms.landmark):
                print(id,lm)
                h,w,c=img.shape
                
                cx,cy=int(lm.x*w), int(lm.y*h)
                cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
                

    #fps
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    
    cv2.putText(img,"FPS: "+str(int(fps)),(10,75), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    
    
    cv2.imshow("img",img)
    cv2.waitKey(1)


