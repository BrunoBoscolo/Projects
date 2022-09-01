from tkinter import *
from PIL import Image
import numpy as np
import cv2
import glob
import mouse
import time
import random
import keyboard


def get_last_image(img_dir):
    img_list_arr = glob.glob(img_dir)
    img_list_arr_w = len(img_list_arr)
    last_image = img_list_arr[img_list_arr_w - 1]
    return str(last_image)


def template_matching(direc):
    global template
    keyboard.send("f")
    time.sleep(5)

    img_rgb = cv2.imread(get_last_image("D:/Tibia/packages/Tibia/screenshots/*.png"))
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    if direc == "fish":
        template = cv2.imread('templates/fish.png', 0)
    elif direc == "fishing_rod":
        template = cv2.imread('templates/fishing_rod.png', 0)
    elif direc == "leather_boots":
        template = cv2.imread('templates/leather_boots.png', 0)
    elif direc == "medicine_pounch":
        template = cv2.imread('templates/medicine_pounch.png', 0)
    elif direc == "mouldy_cheese":
        template = cv2.imread('templates/mouldy_cheese.png', 0)
    elif direc == "spear":
        template = cv2.imread('templates/spear.png', 0)
    elif direc == "torch":
        template = cv2.imread('templates/torch.png', 0)
    elif direc == "troll_green":
        template = cv2.imread('templates/troll_green.png', 0)
    elif direc == "wood":
        template = cv2.imread('templates/wood.png', 0)

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8

    loc = np.where(res >= threshold)
    locx, locy = np.shape(loc)
    print(loc)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    #cv2.imshow('Detected', img_rgb)
    if locx != 0:
        if locy != 0:
            return loc[1][0]+(w/2), loc[0][0]+(h/2)
    else:
        return


def eat_fish():
    loc= template_matching("fish")
    if loc == None:
        return
    locx, locy = loc
    mouse.move(locx, locy+20, absolute=True, duration=round(random.uniform(0, 1), 2))
    time.sleep(round(random.uniform(0, 0.5), 2))
    mouse.click("left")


def trow_item():

    mouse.move(65, 56 + 20, absolute=True, duration=round(random.uniform(0, 1), 2))
    time.sleep(round(random.uniform(0, 0.5), 2))
    mouse.hold("left")
    mouse.move(768, 316 + 52, absolute=True, duration=round(random.uniform(0, 1), 2))
    time.sleep(round(random.uniform(0, 0.5), 2))
    mouse.release("left")


def clean_inventory():
    trow_item()
    trow_item()
    trow_item()
    trow_item()
    trow_item()
    trow_item()
    trow_item()
    trow_item()


def verify_battle_list():
    time.sleep(3)
    keyboard.press("f")
    time.sleep(8)
    img_rgb = cv2.imread(get_last_image("D:/Tibia/packages/Tibia/screenshots/*.png"))
    if np.all(img_rgb[456][1372] == [115, 37, 219]):
        mouse.move(1372, 456 + 20, absolute=True, duration=round(random.uniform(0, 1), 2))
        time.sleep(round(random.uniform(0, 0.5), 2))
        mouse.click("left")
        return True
    else:
        return False


def collect_item():
    time.sleep(2)
    coords = [[712, 317],
              [768, 316],
              [816, 321],
              [817, 369],
              [817, 423],
              [766, 423],
              [714, 424],
              [714, 367]]


    keyboard.press("alt")
    for i in range(8):
        mouse.move(coords[i][0], coords[i][1], absolute=True, duration=round(random.uniform(0, 1), 2))
        time.sleep(round(random.uniform(0, 0.5), 2))
        mouse.click("left")
    keyboard.release("alt")


def rotine(event):
    trigger = 1
    while trigger == 1:
        time.sleep(2)
        verify_battle_list()
        verify_battle_list()
        verify_battle_list()
        verify_battle_list()
        collect_item()
        trigger = 0

root = Tk()

w0, h0 = 1920, 1080
w1, h1 = 1280, 1024

root.geometry(f"{w1}x{h1}+{w0}+0")

root.bind("<r>", rotine)
root.mainloop()
