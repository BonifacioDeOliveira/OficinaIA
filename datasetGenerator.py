import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = video_capture.read()

    rgb_small_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)

    for top, right, bottom, left in face_locations:
        #print("{} {} {} {}".format(top,right,bottom,left))
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        for top, right, bottom, left in face_locations:
            count += 1
            cv2.imwrite(str(count) + ".png", frame[top+5:bottom-5, left+5:right-5])
        break
    cv2.imshow('Video', frame)

video_capture.release()
