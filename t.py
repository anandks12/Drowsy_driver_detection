import cv2
import mediapipe as mp
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
landmark_style =mp_drawing.DrawingSpec((0, 255, 0), thickness=1, circle_radius=1)
connection_style = mp_drawing.DrawingSpec((0, 0, 255), thickness=1, circle_radius=1)

# Define a function to detect yawn
def detect_yawn(image):
    with mp_face_mesh.FaceMesh(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:

        # Convert the image to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and get facial landmarks
        results = face_mesh.process(image)

        # Check if facial landmarks are detected
        if not results.multi_face_landmarks:
            return False

        # Get the x,y,z coordinates of the mouth landmarks
        mouth_landmarks = [results.multi_face_landmarks[0].landmark[i] for i in range(61, 68)]

        # Get the y-coordinates of the mouth landmarks
        mouth_y_coords = [landmark.y for landmark in mouth_landmarks]

        # Calculate the difference between the top and bottom of the mouth
        mouth_height_diff = max(mouth_y_coords) - min(mouth_y_coords)

        # If the difference is greater than a certain threshold, it's a yawn
        if mouth_height_diff > 0.05:
            return True

        return False

# Open the video capture device
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Flip the image horizontally for a more natural webcam view
    image = cv2.flip(image, 1)

    # Detect a yawn in the image
    is_yawning = detect_yawn(image)

    # Print whether the person is yawning or not
    if is_yawning:
        print("Person is yawning")
    else:
        print("Person is not yawning")

    # Draw the facial landmarks on the image for visualization
    with mp_face_mesh.FaceMesh(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1))

    # Display the image
    cv2.imshow("Yawn Detection", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
