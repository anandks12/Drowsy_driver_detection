# Importing OpenCV Library for basic image processing functions
import cv2
# Numpy for array related functions
import numpy as np
# Dlib for deep learning based Modules and face landmark detection
import dlib
# face_utils for basic operations of conversion
from imutils import face_utils





# Initializing the camera and taking the instance
cap = cv2.VideoCapture(0)

# Initializing the face detector and landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# status marking for current state
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)


def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist


def blinked(a, b, c, d, e, f):
    up = compute(b, f) + compute(c, e)
    down = compute(a, d)
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
    elif ( compute(p3,p7) > 20 ) :
        return 0


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    face_frame = frame.copy()

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        # The numbers are actually the landmarks which will show eye
        left_blink = blinked(landmarks[36], landmarks[37],
                             landmarks[38], landmarks[39], landmarks[40], landmarks[41])
        right_blink = blinked(landmarks[42], landmarks[43],
                              landmarks[44], landmarks[45], landmarks[46], landmarks[47])
        mouth = mopen(landmarks[48], landmarks[50], landmarks[51],
                             landmarks[52], landmarks[54], landmarks[56],landmarks[57], landmarks[58])

        if (left_blink == 0 and right_blink == 0):
            sleep += 1
            drowsy = 0
            active = 0
            if (sleep > 6):
                status = "SLEEPING !!!"
                color = (255, 0, 0)

        elif (left_blink == 1 and right_blink == 1 or mouth == 0):
            sleep = 0
            active = 0
            drowsy += 1
            if (drowsy > 6):
                status = "Drowsy !"
                color = (0, 0, 255)
        else:
            drowsy = 0
            sleep = 0
            active += 1
            if ( active > 6 ) :
                status = "Active :)"
                color = (0, 255, 0)



        cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 4)

        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 0), 1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Result of detector", face_frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()