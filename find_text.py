import pyautogui
import cv2
import numpy as np
import time
import pytesseract

# Function to find text on the screen using OpenCV
def find_text_on_screen(region=None):
    screenshot = pyautogui.screenshot(region=region)
    screenshot_np = np.array(screenshot)
    screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(screenshot_bgr, cv2.COLOR_BGR2GRAY)

    # Apply image processing techniques (you may need to customize these based on your use case)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(binary, kernel, iterations=1)
    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

    # Find contours in the processed image
    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Check if the contour has a reasonable size (you may need to customize this based on your use case)
        if w > 50 and h > 10:
            # Crop the region of interest (ROI) from the original screenshot
            roi = screenshot_np[y:y+h, x:x+w]

            # Perform text recognition (you may need to customize this based on your use case)
            text = pytesseract.image_to_string(roi)

            if text:
                print(f"Text found: {text}")
                if text == 'cbsAdmSvr11':
                    print("true")

# Main program
try:
    while True:
        # Specify the region on the screen where you want to find text
        # If None, it will capture the entire screen
        screen_region = None

        # Find text on the specified region
        find_text_on_screen(region=screen_region)

        # Wait for a moment before capturing the next screenshot
        time.sleep(1)
except KeyboardInterrupt:
    print("\nScript terminated by user.")
