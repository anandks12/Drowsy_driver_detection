import scipy.spatial
import mediapipe as mp
import cv2
import numpy as np
import math
import pygame
from call import call
import threading




mp_pose = mp.solutions.pose
pose_estimator = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

face_mesh = mp.solutions.face_mesh

draw_utils = mp.solutions.drawing_utils
landmark_style = draw_utils.DrawingSpec((0, 255, 0), thickness=1, circle_radius=1)
connection_style = draw_utils.DrawingSpec((0, 0, 255), thickness=1, circle_radius=1)

distanceModule = scipy.spatial.distance

face_model = face_mesh.FaceMesh(static_image_mode=False,
                                max_num_faces=1,
                                min_detection_confidence=0.6,
                                min_tracking_confidence=0.5)



LIPS = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95,
        185, 40, 39, 37, 0, 267, 269, 270, 409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78]
LEFT_EYE_TOP_BOTTOM = [160,159,158,144, 145,153]
LEFT_EYE_LEFT_RIGHT = [133, 33]
RIGHT_EYE_TOP_BOTTOM =[385,386,387, 380,374,373]
RIGHT_EYE_LEFT_RIGHT =[362,263]
UPPER_LOWER_LIPS = [82,13,312,87,14,317]
LEFT_RIGHT_LIPS = [78, 308]
RIGHT_EYE = [ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]
LEFT_EYE = [ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]
jaw=[152]
def play_sound(s):
    pygame.mixer.init()
    if s == "SLEEPING !!!":
        pygame.mixer.music.load('alert-alarm.wav')
    else:
        pygame.mixer.music.load('output.wav')
    pygame.mixer.music.play(1)
    print("sound is playing..")
def on_button(si):
    sleep = 0
    drowsy = 0
    active = 0
    head = 0
    status = ""
    color = (0, 0, 0)
    def compute(ptA, ptB):
        x1 = int(ptA.x * img_w)
        y1 = int(ptA.y*img_h)
        x2 = int(ptB.x*img_w)
        y2 = int(ptB.y * img_h)
        dist=distanceModule.euclidean([x1,y1],[x2,y2])
        return dist
    def blinked(output,s):
        if output is not None:
            for face in output:
                a = face.landmark[s[0]]
                b = face.landmark[s[3]]
              #  c = face.landmark[s[1]]
              #  d = face.landmark[s[4]]
                e = face.landmark[s[2]]
                f = face.landmark[s[5]]
                g = face.landmark[s[6]]
                h = face.landmark[s[7]]
                up = compute(a,b ) + compute(e,f)
                down = compute(g, h)
                ear = up / (2.0 * down)
                cv2.putText(img=frame, text='EAR ratio:' + str(ear), fontFace=0,
                            org=(450, 200), fontScale=0.5,thickness=0,color=(255, 0, 0))

        # Eye aspect ratio
            if (ear > 0.25):
                return 2
            elif (ear == 0.25):
                 return 1
            elif ( ear < 0.25 ):
                return 0
        else :
            cv2.imshow("Result of detector", frame)

        #Mouth aspect ratio
    def mopen(output,s):
        if output is not None:
            for face in output:
                a = face.landmark[s[0]]
                b = face.landmark[s[3]]
                c = face.landmark[s[1]]
                d = face.landmark[s[4]]
                e = face.landmark[s[2]]
                f = face.landmark[s[5]]
                g = face.landmark[s[6]]
                h = face.landmark[s[7]]
                # i=face.landmark[s[8]]


                up = compute(a,b ) + compute(e,f) + compute(c,d)
                down = compute(g, h)
                mar = up / (2.0 * down)
                cv2.putText(img=frame, text='MAR ratio:' + str(mar), fontFace=0,
                            org=(450, 100), fontScale=0.5, color=(255, 0, 0))
            if (mar < .2) :
                return 2
            elif ( compute(c,d) > 13 ) or (mar >0.25):

                return 1
        else :
            cv2.imshow("Result of detector", frame)
            cv2.putText(frame, "Face not detected ", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)




    if si == "Real Time Detection":
        cap = cv2.VideoCapture(0)
    elif si == "Video Detection":
        cap = cv2.VideoCapture('D:/sleep.mp4')
    while True:
        try :
            result, frame = cap.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.GaussianBlur(frame, (5, 5), 0)
            img_h, img_w = frame.shape[:2]
            if result:
                image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                outputs = face_model.process(image_rgb)

                results = pose_estimator.process(image_rgb)

                    # cv2.imshow("Result of detector", frame)
                    # cv2.putText(frame, "Face not detected ", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


                if outputs.multi_face_landmarks is not None and results.pose_landmarks is not None :
                    # for face in outputs.multi_face_landmarks:
                    #     for i in LEFT_EYE:
                    #         pt1=face.landmark[i]
                    #         x=int(pt1.x*img_w)
                    #         y=int(pt1.y*img_h)
                    #         cv2.circle(image_rgb,(x,y),2,(100,100,0),-1)
                    #         cv2.putText(image_rgb,str(i),(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1)
                    # cv2.imshow("Result ", image_rgb)
                    #
                    # F: collect all [x,y] pairs of all facial landamarks
                    leye = blinked(outputs.multi_face_landmarks,LEFT_EYE_TOP_BOTTOM + LEFT_EYE_LEFT_RIGHT)
                    reye = blinked(outputs.multi_face_landmarks,RIGHT_EYE_TOP_BOTTOM + RIGHT_EYE_LEFT_RIGHT)
                    mouth = mopen(outputs.multi_face_landmarks,UPPER_LOWER_LIPS + LEFT_RIGHT_LIPS + jaw)
                    if results.pose_landmarks is not None:
                        head_landmarks = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE.value:mp_pose.PoseLandmark.RIGHT_EAR.value + 1]
                        nose_x, nose_y = head_landmarks[0].x, head_landmarks[0].y
                        neck_x, neck_y = head_landmarks[1].x, head_landmarks[1].y
                        dx = neck_x - nose_x
                        dy = neck_y - nose_y
                        angle = -1 * (180 / 3.14159) * math.atan2(dy, dx) #converting radian to degree
                        angle = round(angle, 2)
                    if outputs.multi_face_landmarks is not None :
                        all_landmarks = np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in
                                              outputs.multi_face_landmarks[0].landmark])
                        if (leye == 0 and reye == 0):
                            sleep += 1
                            drowsy = 0
                            head = 0
                            active = 0
                            if (sleep > 25):
                                status = "SLEEPING !!!"
                                color = (255, 0, 0)
                                if sleep > 25 and sleep <= 27:

                                    music_thread = threading.Thread(target=play_sound(status))
                                    music_thread.start()

                        elif ((leye == 1 and reye == 1) or mouth == 1):
                            sleep = 0
                            active = 0
                            head = 0
                            drowsy += 1
                            if (drowsy > 25):
                                status = "Drowsy !"
                                color = (0, 0, 255)
                                if drowsy > 25 and drowsy<=27:

                                    music_thread = threading.Thread(target=play_sound,args=(status,))
                                    music_thread.start()

                        elif (angle > 43 and angle < 50) or ( (angle>=68 and angle <71) or (not (angle > 61 and angle <= 81)) ) or (angle > 81 and angle < 90):

                            drowsy = 0
                            sleep = 0
                            active += 1
                            head += 1
                            if (head > 30):
                                status = "Are you drowsy???"
                                color = (0, 0, 255)
                        elif (mouth == 2 and leye == 2 and reye == 2) or (angle>70 and angle >75) :
                            drowsy = 0
                            sleep = 0
                            head=0
                            active += 1
                            if  active:
                                status = "Active :)"
                                color = (0, 255, 0)


                        right_eye = all_landmarks[RIGHT_EYE]
                        left_eye = all_landmarks[LEFT_EYE]
                        lips = all_landmarks[LIPS]
                        le = [13, 14]
                        l = all_landmarks[le]
                        cv2.polylines(frame, [left_eye], True, (0, 0, 255), 1, cv2.LINE_AA)
                        cv2.polylines(frame, [l], True, (0, 0, 255), 1, cv2.LINE_AA)
                        cv2.polylines(frame, [right_eye], True, (0, 255, 0), 1, cv2.LINE_AA)
                        cv2.polylines(frame, [lips], True, (255, 0, 0), 1, cv2.LINE_AA)
                        cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 4)
                        cv2.putText(frame, text='Max drowsy frames: ' + str(drowsy), fontFace=0,
                                    org=(10, 30), fontScale=0.5, color=(0, 255, 0))
                        cv2.putText(img=frame, text='Max sleepy frames:' + str(sleep), fontFace=0,
                                    org=(10, 50), fontScale=0.5, color=(0, 255, 0))
                        cv2.putText(frame, f"Head angle: {angle}", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
                        cv2.putText(frame, f"Head frames : {head} ", (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
                    elif angle > 60 and angle <=65 :
                        cv2.putText(frame, "Are You Drowsy ???", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        cv2.putText(frame, f"Head angle: {angle}", (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
                    else:
                        cv2.putText(frame, "Face not detected ", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0, 255), 2)
                    if si == "Real Time Detection" and sleep > 50 :
                        c1 = threading.Thread(target=call)
                        c1.start()
                        break

                    cv2.imshow("Result of detector", frame)

                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                    if cv2.getWindowProperty('Result of detector', cv2.WND_PROP_VISIBLE) < 1:  # exit if window closed
                        break
                else:
                    cv2.putText(frame, "Person not detected ", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    cv2.imshow("Result of detector", frame)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                if cv2.getWindowProperty('Result of detector', cv2.WND_PROP_VISIBLE) < 1:  # exit if window closed
                    break
        except:
            print("Video completed")
            break

    cap.release()
    cv2.destroyAllWindows()


