import cv2
import mediapipe as mp

cap= cv2.VideoCapture(0)

drawing= mp.solutions.drawing_utils
hands= mp.solutions.hands


hands_object= hands.Hands(max_num_hands=3)

def count_figures(d):
    count=0
    threshScore= (d.landmark[0].y*100 -d.landmark[9].y*100)/2

    if(d.landmark[5].y*100-d.landmark[8].y*100)>threshScore:
        count+=1

    if(d.landmark[9].y*100-d.landmark[12].y*100)>threshScore:
        count+=1

    if(d.landmark[13].y*100-d.landmark[16].y*100)>threshScore:
        count+=1

    if(d.landmark[17].y*100-d.landmark[20].y*100)>threshScore:
        count+=1

    if(d.landmark[5].x*100 -d.landmark[4].x*100)>5:
        count+=1

    return count



while True:
    dummy,image= cap.read()
    image=cv2.flip(image,1)

    result=hands_object.process(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

    if result.multi_hand_landmarks:
        hand_keyPoints= result.multi_hand_landmarks[0]

        c=count_figures(hand_keyPoints)
        print(c)
        cv2.putText(image,"Figures: "+str(c),(200,200),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
        drawing.draw_landmarks(image,hand_keyPoints,hands.HAND_CONNECTIONS)
  
    cv2.imshow("Gestures",image)

    key= cv2.waitKey(1)
    if key==32:
        break
cv2.destroyAllWindows()