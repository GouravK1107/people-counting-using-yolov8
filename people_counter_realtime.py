from ultralytics import YOLO
import cv2 as cv

model = YOLO("yolov8n.pt")

real_time = cv.VideoCapture(0)
if not real_time:
    print("Couldn't making the open the webcame !")
    exit()

print("Enter the 'q' to end up the session.")

while True:
    status, frame = real_time.read()
    if not status:
        break

    results = model(frame, stream=True)
    person = 0

    for i in results:
        a = i.boxes

        if a is not None:
            for j in a:
                cls_id = int(j.cls[0])
                confident = float(j.conf[0])
            
                if cls_id == 0 and confident >= 0.5:
                    person += 1

    
    cv.putText(frame, f"Count of People: {person}", (20, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 200), 2)
    cv.imshow("People Counting Terminal !", frame)

    if cv.waitKey(1) & 0xFF == 'q':
        break

real_time.release()
cv.destroyAllWindows()