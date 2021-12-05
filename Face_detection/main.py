import cv2
import time
# import led.py and noti.py
import led
import noti

starttime = 0

print('Start Program !')

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Capture video from webcam.
cap = cv2.VideoCapture(0)

while True:

        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	#check if detecting or not
        if type(faces) is tuple:
                #print("not detect")
                led.off()
        elif starttime == 0:
                #print("detect")
                starttime = time.time()
                noti.push_noti()
                print('Notification sent!')
                led.on()
        else: #if the time pass 15 seconds notification will be sent again
                if time.time() - starttime > 15:
                        starttime = 0

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display
        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
                break
# Release the VideoCapture object
cap.release()

