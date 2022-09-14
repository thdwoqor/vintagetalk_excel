import errno
import glob
import os

import cv2
import numpy as np
from view.gui import width_size


def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode="w+b") as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def hex_to_rgb(hex_string):
    r_hex = hex_string[1:3]
    g_hex = hex_string[3:5]
    b_hex = hex_string[5:7]
    # return int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)
    return int(b_hex, 16), int(g_hex, 16), int(r_hex, 16)


def listImage(image_key, image_value, target_dir, save_path, blank_size, line_color):
    full_width, full_height, index = 0, 0, 1
    image_list = []
    size = int(width_size.get())
    blank_img = None

    for index, i in enumerate(image_value):
        img_array = np.fromfile(os.path.join(target_dir, image_key + "_" + str(i) + ".jpg"), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        image_list.append(img)
        height, width, c = img.shape
        if index == 0:
            blank_img = np.full((int(blank_size), width, 3), hex_to_rgb(str(line_color)), dtype=np.uint8)
        elif index == len(image_value) - 1:
            break
        image_list.append(blank_img)
    img_con = cv2.vconcat(image_list)
    height, width, c = img_con.shape

    dst = cv2.resize(img_con, dsize=(size, int((height * size) / width)), interpolation=cv2.INTER_AREA)
    imwrite(os.path.join(save_path, image_key + ".png"), dst)


def merge(file_path: str, save_path: str, blank_size, line_color):
    target_dir = file_path
    files = glob.glob(os.path.join(target_dir, "*.jpg"))
    name_list = {}

    try:
        if not (os.path.isdir(save_path)):
            os.makedirs(os.path.join(save_path))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    for f in files:
        name = f.split("\\")[-1]
        key = name.split("_")[0]
        value = name.split("_")[1].split(".")[0]

        if key in name_list.keys():
            name_list[key].append(int(value))
        else:
            name_list[key] = [int(value)]

        name_list[key].sort()

    for key, value in name_list.items():
        listImage(key, value, target_dir, save_path, blank_size, line_color)
