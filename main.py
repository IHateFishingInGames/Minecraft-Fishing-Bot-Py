import cv2
import numpy as np
import pyautogui

# Load the reference image of the bobber
reference_image = cv2.imread('bobber.png')

# Loop indefinitely
while True:
    # Take a screenshot of the region of the screen that contains the bobber
    screenshot = pyautogui.screenshot(region=(800, 400, 250, 250))

    # Convert the screenshot to a NumPy array
    image = np.array(screenshot)

    # Use template matching to compare the screenshot to the reference image
    result = cv2.matchTemplate(image, reference_image, cv2.TM_CCOEFF_NORMED)

    # Check if the result is above a certain threshold
    if np.max(result) > 0.25:
        print('Bobber detected')
    else:
        print('Bobber not detected')
        # Press the right mouse button and wait until the bobber is not detected again
        while True:
            pyautogui.click(button='right')
            pyautogui.sleep(1)  # Delay for 1 second

            # Take another screenshot and check for the bobber again
            screenshot = pyautogui.screenshot(region=(800, 400, 250, 250))
            image = np.array(screenshot)
            result = cv2.matchTemplate(image, reference_image, cv2.TM_CCOEFF_NORMED)
            if np.max(result) > 0.25:
                break
