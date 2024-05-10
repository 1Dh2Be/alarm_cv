# alarm_cv - Movement detection 🔔
**alarm_cv** is a Python based Webcam Alarm System application designed to detect motion through a webcam (or any other camera). When significant movement is detected, the system triggers an alarm. This project utilizes OpenCV for image processing and Pygame for handling audio feedback.

## Features 🛠️

- **Real-time Motion Detection**: Detects motion in the video feed in real time.
- **Alarm Notification**: Triggers an audio alarm when significant motion is detected.
- **Adjustable Sensitivity**: Users can modify the sensitivity of motion detection directly in the script.
- **Simple GUI**: Displays the webcam feed with an option to view the threshold image that triggers the alarm.

## Getting Started 🔰

### Prerequisites
- [Python 3.9+](https://www.python.org/downloads): The programming language used for the project.
- [pip](https://pip.pypa.io/en/stable/installation/): Used to download and manage dependencies.

### Installation

1. Clone the repository:

   ```
   git clone git@github.com:1Dh2Be/SummaTube.git
   ```

2. Navigate to the project directory:

   ```
   cd alarm_cv
   ```
3. Create a virtual environment & activate it:
   ```
   python -m venv myenv
   ```
   ```
   source myenv/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```
5. Run the script
   ```
   python src/alarm.py
   ```
   
## Usage 📖

### Configuring the Camera
Before running the application, ensure the correct camera is configured. The script uses `cap = cv2.VideoCapture(1)` by default, which is typically for external USB cameras. If you need to use your built-in webcam or another external USB camera, you may need to adjust the index:
- `0`: Default built-in webcam
- `1`, `2`, etc.: External USB cameras or other video input devices

Ensure that external cameras are properly connected via USB to your computer before starting the application. Network cameras or cameras requiring special connections (e.g., Wi-Fi, Ethernet) are not supported by default and may require additional configuration.

Adjust this setting in the `src/alarm.py` file according to your setup.

### Controls
- 't' Key: Toggle the alarm mode on/off.
- 'q' Key: Quit the application.
### Explanation
Once the script is running and the camera window is visible, you can press the 't' key to toggle the alarm mode. This action activates the alarm mode, causing the camera window to display in black and white. In this mode, areas without movement will appear black, while detected movements will be highlighted with white pixels. This visual feedback helps users clearly see when and where motion is detected.

If a certain amount of movement is detected (the sensitivity can be adjusted by modifying the threshold value in the script), an alarm will sound twice to signal the detection of a movement. To deactivate the alarm mode, press the 't' key again. To close the application and all its windows, press the 'q' key.

## Note 📝

This project is not intended for use in real-life scenarios where reliable movement detection is critical. It was developed solely to assess and demonstrate my newly acquired computer vision skills. Please consider this context when using or modifying the application.

---

For any further questions or inquiries, please contact me on [LinkedIn](https://www.linkedin.com/in/mimoun-atmani/).
