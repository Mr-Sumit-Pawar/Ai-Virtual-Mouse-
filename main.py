import cv2
import math
import numpy as np
import handtracking
import autopy

# Define the pins that the servo motors are connected to
SERVO1_PIN = 9
SERVO2_PIN = 10

# Define the maximum and minimum angles for the servo motors
SERVO_MAX_ANGLE = 180
SERVO_MIN_ANGLE = 0

# Create an instance of the Servo library
servo1 = autopy.servo.Servo(SERVO1_PIN)
servo2 = autopy.servo.Servo(SERVO2_PIN)

# Create an instance of the hand tracking library
handTracker = handtracking.HandTracker()

# Capture a video stream from the camera
cap = cv2.VideoCapture(0)

while True:
  # Read the next frame from the video stream
  ret, frame = cap.read()

  # Detect the hand in the video frame
  hand = handTracker.detectHand(frame)

  # If a hand is detected, move the robotic arm to the position of the hand
  if hand is not None:
    servoAngle1 = math.atan2(hand.y - 90, hand.x - 90) * 180 / math.pi
    servoAngle2 = math.atan2(hand.z - 90, hand.x - 90) * 180 / math.pi

    servo1.write(servoAngle1)
    servo2.write(servoAngle2)

  # Display the video frame
  cv2.imshow('Video', frame)

  # Press the 'q' key to quit
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Release the camera
cap.release()

# Close all windows
cv2.destroyAllWindows()