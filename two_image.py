import pyautogui
import cv2
import numpy as np
import time


# Function to find the location of an image on the screen
def find_image_on_screen(template, threshold=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        return max_loc
    else:
        return None


# Function to click on a specified location
def click_on_location(x, y):
    pyautogui.click(x, y)


# List of template images
template_paths = ['C:\\Users\\Both\\Downloads\\move.png', 'C:\\Users\\Both\\Downloads\\move1.png']

# Load template images with OpenCV
templates = [cv2.imread(path) for path in template_paths]

# Main program
try:
    while True:
        for template in templates:
            # Find the location of the template image on the screen
            location = find_image_on_screen(template)

            if location:
                print(f"Image found at {location} for template {template_paths[templates.index(template)]}")

                # Click on the center of the found location
                click_x, click_y = location[0] + template.shape[1] // 2, location[1] + template.shape[0] // 2
                click_on_location(click_x, click_y)

                # Wait for a moment to avoid rapid clicks
                time.sleep(5)
except KeyboardInterrupt:
    print("\nScript terminated by user.")
