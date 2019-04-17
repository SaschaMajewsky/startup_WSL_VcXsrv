import os
import time
from imagesearch import click_image, imagesearch
import win32gui
import win32con
import win32api

# start the vcxsrv server
vcxsrv_filename = "vcxsrv_config\\config.xlaunch"
os.system("start " + vcxsrv_filename)
time.sleep(1)

# minimize the server window for now
vcxsrv_window = win32gui.GetForegroundWindow()
win32gui.ShowWindow(vcxsrv_window, win32con.SW_MINIMIZE)

# enter the windows subsystem for linux bash
os.system("start cmd /c wsl")
time.sleep(0.8)

# open a xfce4 session to connect to our vcxsrv server
# a bit tinkered as pywinauto library currently doesn't seem stable
pos = imagesearch("image_recognition\\bash.PNG")
time.sleep(0.2)
click_image("image_recognition\\bash.PNG", pos, "left", 0.2, offset=5)
key_send_list = [0x58, 0x46, 0x43, 0x45, 0x34, 0xBD, 0x53, 0x45, 0x53, 0x53, 0x49, 0x4F, 0x4E, 0x0D]
for key in key_send_list:
    win32api.keybd_event(key, 0, )
    time.sleep(0.05)

# maximize the server window with the working GUI
win32gui.ShowWindow(vcxsrv_window, win32con.SW_MAXIMIZE)
