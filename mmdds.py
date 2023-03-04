import mediapipe as mp
import cv2
import numpy as np

face_mesh = mp.solutions.face_mesh
draw_utils = mp.solutions.drawing_utils
landmark_style = draw_utils.DrawingSpec((0, 255, 0), thickness=1, circle_radius=1)
connection_style = draw_utils.DrawingSpec((0, 0, 255), thickness=1, circle_radius=1)

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
UPPER_LOWER_LIPS = [82,312,87,317]
LEFT_RIGHT_LIPS = [78, 308]
RIGHT_EYE = [ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]
LEFT_EYE = [ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]

def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist
def blinked(output,s):
    for face in output:
        for i in s:
            up = compute(b, d)
            down = compute(a, c)
            ear = up / (2.0 * down)

    # Eye aspect ratio
    if (ear > 0.25):
        return 2
    elif (ear > 0.21 and ear <= 0.25):
        return 1
    else:
        return 0
    #Mouth aspect ratio
def mopen(p1,p2,p3,p4,p5,p6,p7,p8):
    num = compute(p2,p8) + compute(p3,p7) + compute(p4,p6)
    den = compute(p1,p5)
    mar = num/(2.0*den)
    if (mar < 0.25) :
        return 2
    elif ( compute(p3,p7) > 25 ) :
        return 0

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
            for face in outputs.multi_face_landmarks:
                for i in LEFT_EYE_TOP_BOTTOM + RIGHT_EYE_TOP_BOTTOM:
                    pt1=face.landmark[i]
                    x=int(pt1.x*img_w)
                    y=int(pt1.y*img_h)
                    cv2.circle(image_rgb,(x,y),2,(100,100,0),-1)
                    cv2.putText(image_rgb,str(i),(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1)
            cv2.imshow("Result ", image_rgb)
            # F: collect all [x,y] pairs of all facial landamarks
            #leye = blinked(outputs.multi_face_landmarks,LEFT_EYE_)
            #reye = blinked(outputs.multi_face_landmarks,RIGHT_EYE)
            all_landmarks = np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in
                                      outputs.multi_face_landmarks[0].landmark])

                # G: right and left eye landmarks
            right_eye = all_landmarks[RIGHT_EYE]
            left_eye = all_landmarks[LEFT_EYE]
            lips = all_landmarks[LIPS]
                # H: draw only landmarks of the eyes over the image
            cv2.polylines(frame, [left_eye], True, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.polylines(frame, [right_eye], True, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.polylines(frame, [lips], True, (255, 0, 0), 1, cv2.LINE_AA)


            cv2.imshow("Result of detector", frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
cap.release()
