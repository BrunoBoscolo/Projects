from tkinter import *
from PIL import Image
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import numpy as np
import cv2
import glob
import mouse
import time
import random
import keyboard


def create_obs_map():
    for x in range(0, (width * 10) + 1, 10):
        vertical_sep = Frame(canva, bg="black", height=height * 10, width=1)
        vertical_sep.place(x=x, y=0)

    for y in range(0, (height * 10) + 1, 10):
        horizontal_sep = Frame(canva, bg="black", height=1, width=width * 10)
        horizontal_sep.place(x=0, y=y)


def add_obs_pf(pf_arr):
    for i in range(width):
        for j in range(height):
            if (pf_arr[i][j] == 1):
                canva.create_text(i * 10 + 5, j * 10 + 5, text=1)
            else:
                canva.create_text(i * 10 + 5, j * 10 + 5, text=0)


def create_player():
    global player
    global player_vision_north
    global player_vision_south
    global player_vision_east
    global player_vision_west

    canva.delete(player)
    canva.delete(player_vision_north)
    canva.delete(player_vision_south)
    canva.delete(player_vision_east)
    canva.delete(player_vision_west)

    px, py = int(player_x_coord.get()), int(player_y_coord.get())

    player = canva.create_rectangle(px, py, px + 10, py + 10, fill="blue")
    player_vision_north = canva.create_rectangle(px - 70, py - 50, px + 80, py - 50, fill="red")
    player_vision_south = canva.create_rectangle(px - 70, py + 60, px + 80, py + 60, fill="red")
    player_vision_east = canva.create_rectangle(px - 70, py - 50, px - 70, py + 60, fill="red")
    player_vision_west = canva.create_rectangle(px + 80, py - 50, px + 80, py + 60, fill="red")


def create_enemy():
    global enemy
    canva.delete(enemy)
    ex, ey = int(enemy_x_coord.get()), int(enemy_y_coord.get())
    enemy = canva.create_rectangle(ex, ey, ex + 10, ey + 10, fill="green")


def get_array_from_file(file):
    obs_arr_st = np.genfromtxt(file, dtype=float, encoding=None, delimiter=None)
    obs_arr_int = obs_arr_st.astype(int)
    return obs_arr_int


def get_array_from_file_colors(file):
    obs_arr_st = np.genfromtxt(file, dtype=int, encoding=None, delimiter=",")
    obs_arr_int = obs_arr_st.astype(int)
    return obs_arr_int


def get_array_from_file_coords(file):
    obs_arr_st = np.genfromtxt(file, dtype=float, encoding=None, delimiter=None)
    obs_arr_int = obs_arr_st.astype(int)
    return obs_arr_int


def get_pathfinder_array(array_obj):
    array_obj = array_obj / 10
    array_obj = array_obj.astype(np.int32)
    pf_width, pf_height = np.shape(array_obj)
    pf_zeros = np.ones((width, height))

    for i in range(pf_width):
        tx, ty, tx1, ty1 = array_obj[i]
        tx, ty, tx1, ty1 = int(tx), int(ty), int(tx1), int(ty1)
        pf_zeros[tx][ty] = 0

    pf_zeros = pf_zeros.astype(int)
    pf_zeros = np.rot90(pf_zeros)
    pf_zeros = np.flip(pf_zeros, 0)

    return pf_zeros


def add_obs(obs_arr_st):
    i, j = 0, 0
    i_max, j_max = np.shape(obs_arr_st)

    for i in range(0, i_max, 1):
        x_o, y_o, x1_o, y1_o = obs_arr_st[i]
        canva.create_rectangle(x_o, y_o, x_o + 10, y_o + 10, fill="brown")


def add_obs_pf(pf_arr):
    for i in range(width):
        for j in range(height):
            if (pf_arr[i][j] == 1):
                canva.create_text(i * 10 + 5, j * 10 + 5, text=1)
            else:
                canva.create_text(i * 10 + 5, j * 10 + 5, text=0)


def get_pf_path(pointx, pointy):

    px, py, tx, ty = canva.coords(player)
    px = int(int(px) / 10)
    py = int(int(py) / 10)
    ex = int(int(pointx) / 10)
    ey = int(int(pointy) / 10)

    grid = Grid(matrix=pf_array)

    start = grid.node(px, py)
    end = grid.node(ex, ey)

    finder = AStarFinder()

    path, runs = finder.find_path(start, end, grid)

    path_w, path_h = np.shape(path)

    for i in range(1, path_w-1):
        ox, oy = path[i]
        #canva.create_rectangle(ox * 10, oy * 10, ox * 10 + 10, oy * 10 + 10, fill="yellow")

    return path


def template_matching(direc):
    global template

    img_rgb = cv2.imread(get_last_image("D:/Tibia/packages/Tibia/screenshots/*.png"))
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    if direc == "down":
        template = cv2.imread('templates/swamp_troll_down.png', 0)
    elif direc == "left":
        template = cv2.imread('templates/swamp_troll_left.png', 0)
    elif direc == "right":
        template = cv2.imread('templates/swamp_troll_right.png', 0)
    elif direc == "up":
        template = cv2.imread('templates/swamp_troll_up.png', 0)

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.6

    loc = np.where(res >= threshold)
    locx, locy = np.shape(loc)
    print(locx, locy)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    cv2.imshow('Detected', img_rgb)
    if locx != 0:
        if locy != 0:
            return loc
    else:
        return


def export_enemy_coords(ex, ey):
    global enemy
    sx, sy, sz = np.shape(scan_coords)
    px, py, t1, t2 = canva.coords(player)

    for i in range(sx):
        for j in range(sy):
            if ex in range(scan_coords[i][j][0], scan_coords[i][j][2]):
                if ey in range(scan_coords[i][j][1], scan_coords[i][j][3]):
                    contx, conty = (i * 10) + 20, (j * 10) + 10
                    x, y, x1, y1 = int(px - 70 + contx), \
                                   int(py - 50 + conty), \
                                   int(px - 70 + contx + 10), \
                                   int(py - 50 + conty + 10)

                    enemy = canva.create_rectangle(x, y, x1, y1, fill="green")
                    return


def convert_global_coords(ex, ey):
    sx, sy, sz = np.shape(scan_coords)
    px, py, t1, t2 = canva.coords(player)

    for i in range(sx):
        for j in range(sy):
            if ex in range(scan_coords[i][j][0], scan_coords[i][j][2]):
                if ey in range(scan_coords[i][j][1], scan_coords[i][j][3]):
                    contx, conty = (i * 10) + 20, (j * 10) + 10
                    x, y, x1, y1 = int(px - 70 + contx), \
                                   int(py - 50 + conty), \
                                   int(px - 70 + contx + 10), \
                                   int(py - 50 + conty + 10)
                    return x, y, x1, y1


def hunt_quarry(loc):
    print(loc)
    if loc == None:
        print("failed")
        print("------------------------------------------")
    else:
        keyboard.send("f")
        time.sleep(round(random.uniform(0,2), 2))
        px, py, t1, t2 = canva.coords(player)
        ey, ex = loc[0][0], loc[1][0]
        export_enemy_coords(ex, ey)
        q_array = np.zeros((8,2), )
        q_array[0] = px - 10, py - 10
        q_array[1] = px, py - 10
        q_array[2] = px + 10, py - 10
        q_array[3] = px - 10, py
        q_array[4] = px + 10, py
        q_array[5] = px + 10, py + 10
        q_array[6] = px, py + 10
        q_array[7] = px - 10, py + 10
        q_array = q_array.astype(np.int32)

        for j in range(8):
            cx, cy, tx1, ty1 = convert_global_coords(ex, ey)
            if cx == q_array[j][0] and cy == q_array[j][1]:
                #canva.create_rectangle(cx, cy, cx + 10, cy + 10, fill="yellow")
                canva.update()
                mouse.move(ex+20, ey+50, absolute=True, duration=round(random.uniform(0,2), 2))
                time.sleep(round(random.uniform(0,2), 2))
                mouse.click("left")
                time.sleep(round(random.uniform(0,2), 2))


def verify_all_direc():
    hunt_quarry(template_matching("up"))
    time.sleep(round(random.uniform(0,2), 2))
    hunt_quarry(template_matching("down"))
    time.sleep(round(random.uniform(0,2), 2))
    hunt_quarry(template_matching("left"))
    time.sleep(round(random.uniform(0,2), 2))
    hunt_quarry(template_matching("right"))


def get_last_image(img_dir):
    img_list_arr = glob.glob(img_dir)
    img_list_arr_w = len(img_list_arr)
    last_image = img_list_arr[img_list_arr_w - 1]
    return str(last_image)


def move_points(cont_p):
    global cont

    x, y, x1, y1 = move_point_arr[cont_p]
    path = get_pf_path(x, y)
    move_player(path)

    cont += 1


def move_player(path):
    sizepx, sizepy = np.shape(path)
    px, py, t1, t2 = canva.coords(player)
    px = int(px / 10)
    py = int(py / 10)
    for i in range(1, sizepx):
        print(px, py)
        print(path[i][0], path[i][1])
        verify_all_direc()
        if px > path[i][0]:

            keyboard.send("a")
            move_left()
            px -= 1
        elif px < path[i][0]:

            keyboard.send("d")
            move_right
            px += 1
        elif py > path[i][1]:

            keyboard.send("w")
            move_up()
            py -= 1
        elif py < path[i][1]:

            keyboard.send("s")
            move_down()
            py += 1
        canva.update()

def move_left():
    canva.move(player, -10, 0)
    time.sleep(2)



def move_right():
    canva.move(player, 10, 0)
    time.sleep(2)



def move_up():
    canva.move(player, 0, -10)
    time.sleep(2)



def move_down():
    canva.move(player, 0, 10)
    time.sleep(2)


pim = Image.open("map.png")

# get the width and height of ratio 3:1
width = int(pim.width / 3)
height = int(pim.height / 3)

# get the width and height of ratio 1:10
width_t = int(width * 10)
height_t = int(height * 10)

# create the tkinter root and rename it as "tracer"
root = Tk()
root.title("Tracer")

# define the resolution of main monitor and secondary monitor
w0, h0 = 1920, 1080
w1, h1 = 1280, 1024

# Put the window in the second monitor
root.geometry(f"{w1}x{h1}+{w0}+0")

# Create the canva node
canva = Canvas(root, width=width * 10, height=height * 10)
canva.place(x=210, y=0)

create_obs_map()
array = get_array_from_file("wall.txt")
add_obs(array)
pf_array = get_pathfinder_array(array)

cont = 1

scan_coords = get_array_from_file_coords("scaner_test.txt")
scan_coords = scan_coords.reshape(15, 11, 4)
move_point_arr = get_array_from_file("walk_point.txt")

wpx, wpy = np.shape(move_point_arr)
for i in range(wpx):
    twpx, twpy = move_point_arr[i][0], move_point_arr[i][1]
    canva.create_rectangle(twpx, twpy, twpx+10, twpy+10, fill="orange")

player = canva.create_rectangle(380, 210, 390, 220, fill="blue")
enemy = canva.create_rectangle(1000, 1000, 1010, 1010, fill="white")

player_vision_north = canva.create_rectangle(1000, 1000, 1000, 1000, fill="red")
player_vision_south = canva.create_rectangle(1000, 1000, 1000, 1000, fill="red")
player_vision_east = canva.create_rectangle(1000, 1000, 1000, 1000, fill="red")
player_vision_west = canva.create_rectangle(1000, 1000, 1000, 1000, fill="red")

frame_input = Frame(root, bg="blue")
frame_input.place(width=200, height=930, x=0, y=0)

player_x_coord = Entry(root)
player_x_coord.insert(1, 0)
player_x_coord.place(width=50, height=25, x=10, y=10)

player_y_coord = Entry(root)
player_y_coord.insert(1, 0)
player_y_coord.place(width=50, height=25, x=65, y=10)

enemy_x_coord = Entry(root)
enemy_x_coord.insert(1, 0)
enemy_x_coord.place(width=50, height=25, x=10, y=50)

enemy_y_coord = Entry(root)
enemy_y_coord.insert(1, 0)
enemy_y_coord.place(width=50, height=25, x=65, y=50)

button_start = Button(frame_input, text="Start pathfinding", command=lambda: get_pf_path(pf_array))
button_start.place(width=105, height=25, x=10, y=90)

button_player_ok = Button(frame_input, text="Ok", command=create_player)
button_player_ok.place(width=25, height=25, x=120, y=10)

button_enemy_ok = Button(frame_input, text="Ok", command=create_enemy)
button_enemy_ok.place(width=25, height=25, x=120, y=50)

button_update_enemy = Button(frame_input, text="Get enemy position", command=lambda: verify_all_direc())
button_update_enemy.place(width=105, height=25, x=10, y=130)

button_test_pf = Button(frame_input, text="move to next point", command= lambda: move_points(cont))
button_test_pf.place(width=105, height=25, x=10, y=160)


root.bind("<w>", move_up)
root.bind("<s>", move_down)
root.bind("<a>", move_left)
root.bind("<d>", move_right)

root.mainloop()
