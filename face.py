import face_recognition
import cv2
import numpy as np
from db_function import get, add_item

students = []


video_capture = cv2.VideoCapture(0)

abaid_image = face_recognition.load_image_file("abaid.jpg")
abaid_face_encoding = face_recognition.face_encodings(abaid_image)[0]

dileep_image = face_recognition.load_image_file("dileep.jpg")
dileep_face_encoding = face_recognition.face_encodings(dileep_image)[0]

aadithya_image = face_recognition.load_image_file("aadithya.jpg")
aadithya_face_encoding = face_recognition.face_encodings(aadithya_image)[0]

known_face_encodings = [
    abaid_face_encoding,
    dileep_face_encoding,
    aadithya_face_encoding
]
known_face_names = [
    "Abaid",
    "Dileep",
    "Aadithya"
    
]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    if(name not in students):
        add_item(name)
        students.append(name)
        print(name)
        
    


    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
