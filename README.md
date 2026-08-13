# 👥 People Counting using YOLOv8

A Computer Vision project that detects and counts the number of people in an image (and in real-time via webcam) using **YOLOv8 (Ultralytics)** and **OpenCV**. Uses a pretrained deep learning model to identify persons in a frame, draw bounding boxes, and display the total count live.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)

---

## 🚀 Features

- 🧍 Detects multiple people in a single image or live video
- 📦 Draws bounding boxes around each detected person
- 🎯 Displays confidence scores for every detection
- 🔢 Shows total people count directly on the frame
- 🧠 Powered by the modern YOLOv8 deep learning model
- 🎥 Two modes: static image counting and real-time webcam counting

---

## 🛠️ Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics (YOLOv8)
- PyTorch (installed automatically with Ultralytics)

---

## 📂 Project Structure

```
people-counting-using-yolov8/
│
├── people_counter_image.py       # Counts people in a static image
├── people_counter_realtime.py    # Counts people live via webcam
│
├── image.png                     # Sample output image
├── test.png                      # Sample test image
├── test2.png
├── test3.png
├── test4.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 How It Works

1. Load a pretrained YOLOv8 model (`yolov8n.pt`)
2. Run inference on the input image or live video frame
3. Filter detections where class ID = 0 (`person` in the COCO dataset)
4. Count the total number of detected persons
5. Draw bounding boxes + confidence scores and display the running count

---

## 🖼️ Testing Images

The repo ships with a few sample test images (`test.png`, `test2.png`, `test3.png`, `test4.png`) so you can try it out immediately. You're free to:

- Use any image containing people
- Swap in your own test image
- Point to a full image path if needed

To change the image, edit the path inside `people_counter_image.py`:

```python
image_path = "your_image_name.jpg"
```

Or use a full path:

```python
image_path = r"C:\path\to\your\image.jpg"
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/GouravK1107/people-counting-using-yolov8.git
cd people-counting-using-yolov8
```

### 2️⃣ Create a Virtual Environment (Recommended)

```
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux / macOS
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run it

**Static image counting:**
```
python people_counter_image.py
```

**Real-time webcam counting:**
```
python people_counter_realtime.py
```

---

## 🎯 Example Output

- Bounding box drawn around every detected person
- Confidence score shown per detection
- Total people count displayed on the top-left corner of the frame

---

## 📌 Notes

- Confidence threshold is set to `0.5` by default (adjustable in code)
- Accuracy depends on image clarity, lighting and camera angle
- Small or heavily occluded people may not be detected
- Swap in `yolov8s.pt` or a larger YOLOv8 variant for higher accuracy at the cost of speed

---

## 🔥 Future Improvements

- 🚪 Region-based counting (entry / exit gate detection)
- 🔁 Object tracking to count unique entries, not repeated detections
- 👥 Crowd density estimation
- 🖥️ GUI-based interface
- 📊 Logging + analytics dashboard for counted data

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Fork → create a branch → commit → push → open a pull request.

---

## ⭐ Support

If this project helped you, consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Gourav R**
Backend Developer | Applied AI Developer — exploring Computer Vision & AI system development

GitHub: https://github.com/GouravK1107
Portfolio: https://gouravk1107.github.io/my-portfolio/

---

Made with ❤️ and a lot of bounding boxes.
