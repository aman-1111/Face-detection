# Face Detection Project

## 📌 Introduction
Hey there! 👋 This is a simple yet powerful **Face Detection** project built using **Python** and **OpenCV**. It captures video from your webcam and detects faces in real-time. If you've ever been curious about how face detection works, this is a great starting point!

## 🚀 What This Project Does
- Detects faces in real-time using your webcam.
- Uses OpenCV's Haar cascade model for quick and efficient detection.
- Highlights detected faces with a rectangle.
- Works on most laptops and external webcams without extra setup.

## 📂 What's Inside?
```
Face-detection/
│── haarcascade_frontalface_default.xml  # Pre-trained face detection model
│── webcam.py                            # The main script that runs face detection
│── README.md                            # This file you're reading! 😃
```

## 🛠️ Setting Things Up
Before you run the project, make sure you have Python installed along with these dependencies:

### Install Required Packages:
```sh
pip install opencv-python numpy
```

## 🎥 How to Run It
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/Face-detection.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Face-detection
   ```
3. Start the face detection program:
   ```sh
   python webcam.py
   ```

## 📜 What Does `webcam.py` Do?
This script is the heart of the project! Here's a quick breakdown:

- Loads the Haar cascade model to recognize faces:
  ```python
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  ```
- Captures video from your webcam:
  ```python
  cap = cv2.VideoCapture(0)
  ```
- Scans each frame for faces and marks them:
  ```python
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
  for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
  ```
- Displays the video feed with detected faces highlighted.
- Press **'q'** to close the window when you're done.

## 🔥 What You'll See
Once you run `webcam.py`, a window will pop up showing your webcam feed. If the script detects a face, it'll draw a blue rectangle around it. Pretty cool, right? 😎

## 💡 A Few Quick Tips
- Make sure your **webcam is enabled** before running the script.
- If the detection isn't accurate, try tweaking **scaleFactor** and **minNeighbors** in `detectMultiScale()`.
- Good lighting helps in better face detection!

## 📌 Want to Contribute?
This project is open-source, so feel free to fork it, make improvements, and send a pull request. I'd love to see your ideas! 💡

## 📜 License
You're free to use and modify this project under the MIT License.

---
_Made with ❤️ by Aman Chaurasia

