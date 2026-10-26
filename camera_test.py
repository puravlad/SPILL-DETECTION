import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera could not be opened")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
# use lable-studios for labeling the images and then use split_dataset.py to split the dataset into train, val, and test sets. Then use train.py to train the model. After training, use test.py to test the model on the test set. Finally, use python webcam.py to run the model on live webcam feed.