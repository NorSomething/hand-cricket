import mediapipe as mp
import cv2
import numpy as np  
import uuid #to generate unique unifrom id => random string for image name? (for no overlap)
import os
import time
import random
import customtkinter as ctk
from PIL import Image, ImageTk


class GAME_GUI:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.geometry('800x600')
        self.root.title('Hand Cricket')

        # self.camera_label = ctk.CTkLabel(self.root)
        # self.camera_label.pack(padx=20, pady=20)

    

        # self.show_cv_inframe()

        self.video_counter()

        # self.show_cv_inframe()


        self.root.mainloop()

    # def show_cv_inframe(self):
    #     #get frame and convert to image

    #     cv2image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)
    #     img = Image.fromarray(cv2image)

    #     imgtk = ImageTk.PhotoImage(image = img)
    #     self.camera_label.imgtk = imgtk
    #     self.camera_label.configure(image = imgtk)


    def count_fingers(self, hand_landmarks):
        
        fingertips = [4, 8, 12, 16, 20] #4 is thumb
        lower_joints = [3, 6, 10, 14, 18] #3 is thumb
        fingers = []

        #landmark.x .y and .z are the position in x, y and depth from camera

        #note : in image coordinate systems, higher y means lower on the screen (opposite of graphs).

        for tip, joint in zip(fingertips[1:], lower_joints[1:]):
            if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[joint].y:
                fingers.append(1)  # finger up
            else:
                fingers.append(0)  # finger down

        #for thumb
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
            fingers.append(1)
        else:
            fingers.append(0)

        return sum(fingers) #number of fingers up

    def video_counter(self):

        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands #that hand diagram

        #each red mark in the hand is a land mark

        self.cap = cv2.VideoCapture(0) #webcam feed (video device number 0)

        with mp_hands.Hands(min_detection_confidence = 0.8, min_tracking_confidence=0.5) as hands: #first detection confidence, trackign detection confidence

            while self.cap.isOpened():
                ret, frame = self.cap.read() #ret is return value, not really needed, the frame is needed

                #detection
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting bgr to rgb (cuz mediapipe needs rgb)

                #set flag
                image.flags.writeable = False

                results = hands.process(image) #actual detection happening here

                #set flag back to True
                image.flags.writeable = True

                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                finger_count = 0

                #print(results)

                #rendering results 
                if results.multi_hand_landmarks: #if we actually got some results

                    for num, hand in enumerate(results.multi_hand_landmarks):
                        
                        mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
                        finger_count = self.count_fingers(hand)
                        
                #cv2.imshow('Video Feed', frame) #frame is raw webcam feed, but we need with joints
                cv2.imshow('Video Feed', image)



                if cv2.waitKey(10) & 0XFF == ord('q'):
                    done = True
                    break
        
        

        self.cap.release()
        cv2.destroyAllWindows()

        return finger_count

    def game(self):

        score = 0

        for _ in range(3):
            
            #print("waiting 1 second")
            print("press q to register your input")
            #time.sleep(1)
            current = video_counter()
            cpu_move = random.randint(1,6)

            print("your input :", current)
            print("cpu input :", cpu_move)

            if current == cpu_move:
                is_out = True
                print("youre out!!")
                return score, cpu_move
            else:
                score+=current
            
        
        return score, cpu_move



if __name__ == "__main__":
    GAME_GUI()