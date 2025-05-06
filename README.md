# 🖱️ Virtual Mouse Using Hand Tracking

Control your computer's mouse using **hand gestures** captured by your webcam! This project uses **MediaPipe**, **OpenCV**, and **Autopy** to track your hand in real time and convert movements into mouse actions like moving the cursor and clicking.

<p align="center">
  <img src="https://www.google.com/imgres?q=hand%20tracking&imgurl=https%3A%2F%2Fwww.manomotion.com%2Fwp-content%2Fuploads%2F2021%2F07%2FHand-tracking-image.png&imgrefurl=https%3A%2F%2Fwww.manomotion.com%2Fmobile-ar%2F&docid=NreKIFhozKgpVM&tbnid=mznZQfuW1vduGM&vet=12ahUKEwjk9YbBvI6NAxXijK8BHV8FDiYQM3oECGYQAA..i&w=1080&h=1080&hcb=2&ved=2ahUKEwjk9YbBvI6NAxXijK8BHV8FDiYQM3oECGYQAA" alt="Hand Gesture Diagram" width="600"/>
</p>

## 🚀 Features

- 🖐️ Track hand and finger landmarks in real-time
- 🎯 Move the mouse with your index finger
- 👆 Click with a simple gesture (thumb up)
- 🔧 Optional: Control servo motors to simulate robotic arm movement
- 🪄 Smooth and intuitive interaction with interpolation

---

## 📁 Project Structure

virtual-mouse/
├── handtracking.py # Handles hand detection, landmark extraction, and mouse control
├── main.py # Optional: Uses hand data to control servo motors
├── README.md # Documentation



---

## 🧠 Technologies Used

- Python 3.x
- [MediaPipe](https://google.github.io/mediapipe/)
- OpenCV
- NumPy
- Autopy

---


Install Dependencies

Use pip to install the required Python packages:

bash
Copy
Edit
pip install opencv-python mediapipe numpy autopy
