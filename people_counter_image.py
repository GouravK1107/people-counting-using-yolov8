from ultralytics import YOLO
import cv2 as cv

model = YOLO("yolov8n.pt") # loading the model 

image_path = "/Python_programming/opencv/CountingPeople/test4.png"
image = cv.imread(image_path)

if image is None:
    print("Error: Image is not found !!")
    exit()

results = model(image)
person = 0

for i in results:
    for j in i.boxes:
        cls_id = int(j.cls[0])
        confident = float(j.conf[0])

        if cls_id == 0 and confident >= 0.5:
            person += 1

cv.putText(image, f"Counts of peoples: {person}", (50, 20), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
cv.imshow("People Count terminal !", image)
cv.waitKey(0)
cv.destroyAllWindows()
