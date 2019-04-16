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
win32api.keybd_event(0x58, 0, )  # x
win32api.keybd_event(0x46, 0, )  # f
win32api.keybd_event(0x43, 0, )  # c
win32api.keybd_event(0x45, 0, )  # e
win32api.keybd_event(0x34, 0, )  # 4
win32api.keybd_event(0xBD, 0, )  # -
win32api.keybd_event(0x53, 0, )  # s
win32api.keybd_event(0x45, 0, )  # e
win32api.keybd_event(0x53, 0, )  # s
time.sleep(0.1)
win32api.keybd_event(0x53, 0, )  # s
win32api.keybd_event(0x49, 0, )  # i
win32api.keybd_event(0x4F, 0, )  # o
win32api.keybd_event(0x4E, 0, )  # n
win32api.keybd_event(0x0D, 0, )  # ENTER

# maximize the server window with the working GUI
win32gui.ShowWindow(vcxsrv_window, win32con.SW_MAXIMIZE)
