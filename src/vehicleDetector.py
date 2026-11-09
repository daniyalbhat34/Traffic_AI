from ultralytics import YOLO

class VehicleDetector:
    def __init__(self, path, threshold):
        self.conf_thre = threshold
        self.model = YOLO(path)
    
    def detect(self, frame):
        results = self.model.track(frame, persist=True, tracker="bytetrack.yaml", imgsz=1280, iou=0.6, conf=0.05, verbose=False)
        detections = []

        for result in results:
            boxes = result.boxes
            for box in boxes:
                classId = int(box.cls.item())
                conf = box.conf.item()

                trackId = None
                if box.id is not None:
                    trackId = int(box.id.item())

                if classId in {2, 3, 5, 7} and conf >= self.conf_thre:
                    print(f"Vehicle detected: Class {classId}, Confidence: {conf:.2f}")
                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    detections.append({"classId": classId, "conf": conf, "bbox": [x1, y1, x2, y2], "trackId": trackId})

        return detections



