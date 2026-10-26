from ultralytics import YOLO

model = YOLO("yolo11n.pt")

model.train(
    data=r"C:\Users\Purav lad\OneDrive\Desktop\project\SPILL_Detection\SPILL\data.yaml",
    epochs=100,
    imgsz=640,
    batch=8,
    patience=20
)