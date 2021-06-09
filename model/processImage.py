# import libraly necessary librari to run program include:
# 1. pip install opencv-python
# 2. pip install keras

import cv2
import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image

# load model
model = model_from_json(open("../DataTraining/fer.json", "r").read())
# load weights
model.load_weights("../DataTraining/fer.h5")

face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
## detec face

# cap = cv2.VideoCapture(0)   # bật webcam
cap = cv2.VideoCapture("../media/img/21/media/1Untitled.png", cv2.CAP_IMAGES)

while True:
    ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
    if not ret:
        continue
    # Convert our original image from the BGR color space to gray
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    # Use detectMultiScale method to detect face in gray image
    # 1.32 Parameter specifying how much the image size is reduced at each image scale.
    # Parameter specifying how many neighbors each candidate rectangle should have to retain it
    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
        # cropping region of interest i.e. face area from  image
        roi_gray = gray_img[y:y + w, x:x + h]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)

        # find max indexed array, returns the indices of the maximum values along an axis.
        max_index = np.argmax(predictions[0])

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]

        # set emotional state
        cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow("Facial emotion analysis ", resized_img)

    if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows
