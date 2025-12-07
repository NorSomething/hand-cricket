import mediapipe as mp
import cv2
import numpy as np  
import uuid #to generate unique unifrom id => random string for image name? (for no overlap)
import os

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands #that hand diagram

#each red mark in the hand is a land mark

cap = cv2.VideoCapture(0) #webcam feed (video device number 0)

with mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence=0.5) as hands: #first detection confidence, trackign detection confidence

    while cap.isOpened():
        ret, frame = cap.read() #ret is return value, not really needed, the frame is needed

        #detection
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting bgr to rgb (cuz mediapipe needs rgb)

        #set flag
        image.flags.writeable = False

        results = hands.process(image) #actual detection happening here

        #set flag back to True
        image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        print(results)

        #rendering results 
        if results.multi_hand_landmarks: #if we actually got some results
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)

        #cv2.imshow('Video Feed', frame) #frame is raw webcam feed, but we need with joints
        cv2.imshow('Video Feed', image)

        if cv2.waitKey(10) & 0XFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()