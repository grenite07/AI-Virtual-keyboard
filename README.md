# AI-Virtual-keyboard
🖐️ AI Virtual Keyboard (Gesture Controlled)
A futuristic virtual keyboard that allows you to type in real-time using hand gestures. This project utilizes Computer Vision and Machine Learning to track fingertips and detect "click" gestures, eliminating the need for a physical keyboard.



🚀 Features
Real-time Hand Tracking: Uses MediaPipe to detect hand landmarks with high precision.

Gesture Recognition: Detects a "Pinch" gesture (Index Finger + Thumb) to trigger key presses.

Visual Feedback: Keys change color when hovered (Purple) and clicked (Green).

Smart Layout: Includes standard QWERTY keys plus functional "SPACE" and "DELETE" buttons.

On-Screen Typing: Displays the typed text dynamically on the screen interface.

🛠️ Tech Stack
Python: Core programming language.

OpenCV (cv2): For image processing and drawing the UI.

Cvzone: For simplified hand tracking modules.

MediaPipe: Google's framework for hand landmark detection.

NumPy: For mathematical operations.

⚙️ How It Works
Detection: The webcam captures video frames, and MediaPipe analyzes them to find the 21 landmarks of the hand.

Mapping: The code tracks the coordinates of the Index Finger Tip (Landmark 8) and Thumb Tip (Landmark 4).

Interaction:

Hovering: If the Index finger coordinate falls within a button's boundary, the button highlights.

Clicking: The Euclidean distance between the Index Finger and Thumb is calculated. If the distance is < 30 pixels, it registers as a "Click".

💻 Installation & Usage
Clone the repository

Bash

git clone https://github.com/YOUR-USERNAME/AI-Virtual-Keyboard.git
Install dependencies

Bash

pip install opencv-python cvzone mediapipe numpy
Run the application

Bash

python main.py
🔮 Future Improvements
Add "Shift" and "Caps Lock" functionality.

Integrate pynput to type directly into other applications (Notepad/Word).

Add AI text prediction to speed up typing.

Created by Krishna Kujur - Feel free to connect with me on LinkedIn!
