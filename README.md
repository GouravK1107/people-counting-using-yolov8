# 👥 People Counting from Image using YOLOv8

A Computer Vision project that detects and counts the number of people in an image using **YOLOv8 (Ultralytics)** and **OpenCV**.

This project uses a pretrained deep learning model to identify persons in an image and display the total count with bounding boxes.

---

## 🚀 Features

- Detects multiple people in a single image
- Draws bounding boxes around each detected person
- Displays confidence scores
- Shows total people count on the image
- Uses modern YOLOv8 deep learning model
- Easy to extend to real-time webcam detection

---

## 🛠️ Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics (YOLOv8)
- PyTorch (installed automatically with Ultralytics)

---

## 📂 Project Structure

```
people-counter-yolov8/
│
├── people_counter_image.py
├── test.jpg
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 How It Works

1. Load a pretrained YOLOv8 model (`yolov8n.pt`)
2. Run inference on the input image
3. Filter detections where class ID = 0 (Person in COCO dataset)
4. Count total detected persons
6. Display result

---

## 🖼️ Testing Images

This repository may include sample test images such as:

- `test.jpg`
- `image1.jpg`
  
You are free to:

- Use any image containing people
- Replace the image filename inside the script
- Provide a full image path if needed

To change image:

```python
image_path = "your_image_name.jpg"
```

Or use full path:

```python
image_path = r"C:\path\to\your\image.jpg"
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/people-counter-yolov8.git
cd people-counter-yolov8
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 🎯 Example Output

- Total people count displayed on top-left corner

---

## 📌 Notes

- Confidence threshold is set to 0.5 (can be modified in code).
- Accuracy depends on image clarity and lighting.
- Small or heavily occluded people may not be detected.
- You can upgrade to `yolov8s.pt` or larger models for higher accuracy.

---

## 🔥 Future Improvements

- Real-time webcam people counting
- Object tracking (count unique entries)
- Region-based counting (entry/exit gate)
- Crowd density estimation
- GUI-based interface

---

## 👨‍💻 Author

Gourav K  
BCA Student | Backend & AI Enthusiast  
Focused on Computer Vision and AI System Development.
2026

---

⭐ If you found this project useful, consider starring the repository!
