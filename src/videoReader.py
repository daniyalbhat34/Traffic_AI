import cv2
from vehicleDetector import VehicleDetector
from vehicleCounter import VehicleCounter

def openVideo(videoPath="videos/traffic.mp4"):
    cap = cv2.VideoCapture(videoPath)

    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video: {videoPath}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Video FPS: {fps}")

    return cap


def readFrame(cap):
    ret, frame = cap.read()
    return ret, frame


def displayFrame(frame, delay=16):
    cv2.imshow("Traffic AI - Video Feed", frame)
    return cv2.waitKey(delay) == ord("q")


def main():
    cap = openVideo()

    try:
        detector = VehicleDetector("yolo11m.pt", 0.1)
        counter = VehicleCounter()
        while True:
            ret, frame = readFrame(cap)

            if not ret:
                print("End of video.")
                break
            detections = detector.detect(frame)
            for x in detections:
                x1, y1, x2, y2 = x["bbox"]
                trackId = x["trackId"]
                counter.update(trackId)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame,
                    f"ID: {trackId}", 
                    (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.6, 
                    (0, 255, 0),
                    2
                )

            cv2.putText(
                frame,
                f"Vehicles Counted: {counter.counter}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                2
            )

            if displayFrame(frame):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

