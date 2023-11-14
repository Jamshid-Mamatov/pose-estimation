from ultralytics import YOLO


model = YOLO('yolov8s-pose.pt')

# Train the model
results = model.train(data='coco8-pose.yaml', epochs=1, imgsz=640)