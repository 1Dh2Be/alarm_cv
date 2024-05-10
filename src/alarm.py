import cv2
import threading
import imutils
import pygame

# Initialize Pygame once at the beginning.
pygame.init()
pygame.mixer.init()

# Load the sound file once at the beginning.
alarm_sound = pygame.mixer.Sound("alarm_sound/mixkit-alarm-tone-996.wav")

# Initialize a VideoCapture object to capture video from the external camera (index 1).
cap = cv2.VideoCapture(1)

# Set the width & height of the video capture to 640x480 pixels.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Capture the initial frame from the video stream to set up the reference frame.
_, start_frame = cap.read()

# Resize the initial frame to width of 500 pixels, convert to grayscale, and apply Gaussian blur.
start_frame = imutils.resize(start_frame, width=500)
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (5, 5), 0)

# Initialize alarm status, mode, and counter variables as boolean and integer respectively
alarm = False
alarm_mode = False
alarm_counter = 0

def send_alarm():
    """
    Plays the alarm sound multiple times in a loop until the alarm mode is deactivated.
    """
    global alarm
    # Play the sound multiple times in a loop
    for _ in range(2):
        if not alarm_mode:
            break
        alarm_sound.play()
        # Wait for a short time to avoid overloading
        pygame.time.wait(int(alarm_sound.get_length() * 1000))
    alarm = False

# Continuously reading frames from video capture.
while True:
    # Read a frame from the video capture.
    _, frame = cap.read()
    # Resize the fram to a width of 500 Pixels. Allows uniformity across all frames. 
    frame = imutils.resize(frame, width=500)

    # Check if alarm_mode is active.
    if alarm_mode:
        # Converts frame to grayscale and apply Gaussian blur for preprocessing. 
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)

        # Calculate the absolute difference between the current frame and the previous one.
        difference = cv2.absdiff(frame_bw, start_frame)
        # Apply a binary threshold where every pixel with a difference greater to 25 are white,
        # Everything under or equal is black. 
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        # Update the reference frame. 
        start_frame = frame_bw

        # Sum the threshold to check for significant movement. 
        if threshold.sum() > 750000:
            # Increase the counter by one, if the threshold sum +750000
            alarm_counter += 1
        else:
            # Decrease the alarm counter if the difference is not significant. 
            if alarm_counter > 0:
                alarm_counter -= 1
        # Display the threshold image in a GUI. 
        cv2.imshow("WebCam", threshold)
    
    # If alarm mode is not active
    else:
        # Display the frame image in a GUI.
        cv2.imshow("WebCam", frame)
    
    # Triggers the alarm if the counter exceeds a threshold (10)
    if alarm_counter > 10:
        if not alarm:
            alarm = True
            # Start a new thread to handle the alarm sound. 
            threading.Thread(target=send_alarm).start()

    # Check for key presses every 5ms. 
    key_pressed = cv2.waitKey(5) & 0xFF

    # Toggle alarm mode if key pressed is 't'
    if key_pressed == ord('t'):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    
    # Exits the loop and turn alarm mode off if key pressed is 'q'
    if key_pressed == ord('q'):
        alarm_mode = False
        break

# Release the video capture to free up resources.
cap.release()
# Close all OpenCV windows to clean up the GUI. 
cv2.destroyAllWindows()

# Quit pygame after closing the webcam
pygame.mixer.quit()
pygame.quit()