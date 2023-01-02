import pyautogui

# Take a screenshot of the region of the screen that contains the mouse cursor
screenshot = pyautogui.screenshot(region=(800, 400, 250, 250))

# Save the screenshot to a file
screenshot.save('screenshot.png')
