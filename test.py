from ultralytics import YOLO

model = YOLO(
    r"C:\Users\Purav lad\OneDrive\Desktop\project\SPILL_Detection\runs\detect\train2\weights\best.pt"
)

results = model.predict(
    source=r"C:\Users\Purav lad\OneDrive\Desktop\project\SPILL_Detection\SPILL\images\test",
    conf=0.5,
    save=True
)

print("Testing completed!")