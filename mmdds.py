import scipy.spatial
import mediapipe as mp
import cv2
import numpy as np

face_mesh = mp.solutions.face_mesh
draw_utils = mp.solutions.drawing_utils
landmark_style = draw_utils.DrawingSpec((0, 255, 0), thickness=1, circle_radius=1)
connection_style = draw_utils.DrawingSpec((0, 0, 255), thickness=1, circle_radius=1)
distanceModule = scipy.spatial.distance
STATIC_IMAGE = False
MAX_NO_FACES = 1
DETECTION_CONFIDENCE = 0.6
TRACKING_CONFIDENCE = 0.5

sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

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

def compute(ptA, ptB):
    x1 = int(ptA.x * img_w)
    y1 = int(ptA.y*img_h)
    x2 = int(ptB.x*img_w)
    y2 = int(ptB.y * img_h)
    #dist = np.linalg.norm(ptA - ptB)
    #dist = math.dist(ptA,ptB)
    dist=distanceModule.euclidean([x1,y1],[x2,y2])
    return dist
def blinked(output,s):
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

    # Eye aspect ratio
    if (ear > 0.20):
        return 2
    elif (ear > 0.21 and ear <= 0.25):
         return 1
    else:
        return 0
    #Mouth aspect ratio
def mopen(output,s):
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
        cv2.putText(img=frame, text='Max mouth length:' + str(compute(c, d)), fontFace=0,
                    org=(10, 200), fontScale=0.5, color=(255, 0, 0))

        up = compute(a,b ) + compute(e,f) + compute(c,d)
        down = compute(g, h)
        mar = up / (2.0 * down)
        cv2.putText(img=frame, text='MAR ratio:' + str(mar), fontFace=0,
                    org=(10, 300), fontScale=0.5, color=(255, 0, 0))
    if (mar < .25) :
        return 2
    elif ( compute(c,d) > 20 ) :

        return 1

def draw_landmarks(image, outputs, land_mark, color):
    height, width = image.shape[:2]

    for face in land_mark:
        point = outputs.multi_face_landmarks[0].landmark[face]

        point_scale = ((int)(point.x * width), (int)(point.y * height))

        cv2.circle(image, point_scale, 2, color, 1)


face_model = face_mesh.FaceMesh(static_image_mode=STATIC_IMAGE,
                                max_num_faces=MAX_NO_FACES,
                                min_detection_confidence=DETECTION_CONFIDENCE,
                                min_tracking_confidence=TRACKING_CONFIDENCE)
cap = cv2.VideoCapture(0)
while True:
    result, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_h, img_w = frame.shape[:2]
    if result:
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        outputs = face_model.process(image_rgb)
        if outputs.multi_face_landmarks:
            # for face in outputs.multi_face_landmarks:
            #     for i in jaw:
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
            all_landmarks = np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in
                                      outputs.multi_face_landmarks[0].landmark])

            if (leye == 0 and reye == 0):
                sleep += 1
                drowsy = 0
                active = 0
                if (sleep > 50):
                    status = "SLEEPING !!!"
                    color = (255, 0, 0)


            elif ((leye == 1 and reye == 1) or mouth == 1):
                sleep = 0
                active = 0
                drowsy += 1
                if (drowsy > 40):
                    status = "Drowsy !"
                    color = (0, 0, 255)
            elif(mouth==2 and leye==2 and reye==2):
                drowsy = 0
                sleep = 0
                active += 1
                if active:
                    status = "Active :)"
                    color = (0, 255, 0)

            right_eye = all_landmarks[RIGHT_EYE]
            left_eye = all_landmarks[LEFT_EYE]
            lips = all_landmarks[LIPS]
            le=[13,14]
            l=all_landmarks[le]

            cv2.polylines(frame, [left_eye], True, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.polylines(frame, [l], True, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.polylines(frame, [right_eye], True, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.polylines(frame, [lips], True, (255, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 4)
            cv2.putText(frame, text='Max drowsy frames: ' + str(drowsy), fontFace=0,
                       org=(10, 30), fontScale=0.5, color=(0, 255, 0))
            cv2.putText(img=frame, text='Max sleepy frames:'  + str(sleep), fontFace=0,
                       org=(10, 50), fontScale=0.5, color=(0, 255, 0))


            cv2.imshow("Result of detector", frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
cap.release()
