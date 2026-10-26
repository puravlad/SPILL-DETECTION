from ultralytics import YOLO
import cv2

model = YOLO(
    r"C:\Users\Purav lad\OneDrive\Desktop\project\SPILL_Detection\runs\detect\train2\weights\best.pt"
)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    results = model.predict(
        source=frame,
        conf=0.5,
        verbose=False
    )

    annotated_frame = results[0].plot()

    cv2.imshow("Spill Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()