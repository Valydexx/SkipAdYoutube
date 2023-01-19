import pyautogui
import time
import webbrowser

webbrowser.open("https://youtube.com")

def skipad():
    while True:
        skipcoord = pyautogui.locateCenterOnScreen("D:\YouTube AdSkiper\play.png", confidence=0.99, region=(1208, 0, 1585, 1079))
        bannercoord = pyautogui.locateCenterOnScreen("D:\YouTube AdSkiper\skip.png", confidence=0.99, region=(931, 0, 1100, 1079))
        print(skipcoord)
        print(bannercoord)

        if skipcoord or bannercoord is not None:
            break

    if skipcoord is not None:
        pyautogui.click(skipcoord)
    elif bannercoord is not None:
        pyautogui.click(bannercoord)

    time.sleep(1)
    skipad()


skipad()
