
import numpy as np
from math import *
import cv2
from tkinter import *
from PIL import ImageTk,Image 

def create_image():
	img = np.zeros((512, 512, 3), dtype=np.uint8)
	img.fill(255)
	return img


def create_shadow(rate,coords):
	step = 0
	for x in range(coords):
		for y in range(coords):
			point=(x,y)
			color = (x+0, x+0, x+0)
			image = cv2.line(img, point, point, (0, 0, 0), 3)

	return image


def create_circle(x, y):
	image = cv2.circle(img, (x,y), 50, (0, 0, 0))
	
	return image


def create_head_lines(x, y, radius):
	#image = cv2.line(img, (x,(y-radius)), (x,(y+radius)), (0, 0, 0), 1)
	#image = cv2.line(img, (x-radius,y), (x+radius,y), (0, 0, 0), 1)
	return image


def linear_regretion(value, min_value, max_value, new_min_value, new_max_value):
	value_range = max_value - min_value
	new_value_range = new_max_value - new_min_value
	new_value = (((value-min_value) * new_value_range) / value_range) + new_min_value
	return new_value


def create_polygon_coords(ratio):
	coords = []
	for x in range(50):
		y = sin(x)*ratio
		coords.append((x,y))
	return coords



def callback(e):
	global line, arcv, arch, rec, j1, j2, varstring_x, varstring_y, varstring_ratiox, varstring_ratioy

	canvas.delete(line)
	canvas.delete(arcv)
	canvas.delete(arch)
	canvas.delete(rec)
	canvas.delete(j1)
	canvas.delete(j2)

	x = e.x
	y = e.y

	varstring_x.set("Pos x: {}".format(x))
	varstring_y.set("Pos x: {}".format(y))

	if x<=256:
		ratiox = int(linear_regretion(x, 256, 512, 257, 306))
		arcv = canvas.create_arc(256, 206, ratiox, 306, start=90, extent=180, style=ARC)
		#rec = canvas.create_rectangle(256, 206, ratio, 306)
		varstring_ratiox.set("Pos x: {}".format(ratiox))
	elif x>256:
		ratiox = int(linear_regretion(x, 1, 256, 206, 256))
		arcv = canvas.create_arc(256, 206, ratiox, 306, start=270, extent=180, style=ARC)
		#rec = canvas.create_rectangle(256, 206, ratio, 306)
		varstring_ratiox.set("Pos x: {}".format(ratiox))
	if y<=256:
		ratioy = int(linear_regretion(y, 256, 512, 257, 306))
		varstring_ratioy.set("Pos x: {}".format(ratioy))
		arch = canvas.create_arc(206, 256, 306, ratioy, start=0, extent=180, style=ARC)
		if ratiox in range(220, 290):
			j1 = canvas.create_line(216, 306, ratiox, ratioy+75)
			j2 = canvas.create_line(296, 306, ratiox, ratioy+75)
		elif ratiox <= 220:
			j1 = canvas.create_line(216, 306, 220, ratioy+75)
			j2 = canvas.create_line(296, 306, 220, ratioy+75)
		elif ratiox >= 290:
			j1 = canvas.create_line(216, 306, 290, ratioy+75)
			j2 = canvas.create_line(296, 306, 290, ratioy+75)

	elif y>256:
		ratioy = int(linear_regretion(y, 1, 256, 206, 256))
		varstring_ratioy.set("Pos x: {}".format(ratioy))
		arch = canvas.create_arc(206, 256, 306, ratioy, start=180, extent=180, style=ARC)
		if ratiox in range(220, 290):
			j1 = canvas.create_line(216, 306, ratiox, 331)
			j2 = canvas.create_line(296, 306, ratiox, 331)
		elif ratiox >= 291:
			j1 = canvas.create_line(216, 306, 290, 331)
			j2 = canvas.create_line(296, 306, 290, 331)
		elif ratiox <= 220:
			j1 = canvas.create_line(216, 306, 220, 331)
			j2 = canvas.create_line(296, 306, 220, 331)

	line = canvas.create_line(x, y, 256, 256)
	print("ratio x: {}, ratio y: {}".format(ratiox, ratioy))

root = Tk()
root.resizable(width=False, height=False)
canvas = Canvas(root, width = 512, height = 512)  
canvas.pack()

img = create_image()
image = create_circle(256, 256)
image = create_head_lines(256, 256, 50)
cv2.imwrite('head.jpg', image)

img = ImageTk.PhotoImage(Image.open("head.jpg"))  
canvas.create_image(0, 0, anchor=NW, image=img) 
line = canvas.create_line(0, 0, 0 ,0)
rec = canvas.create_rectangle(0, 0, 0, 0)
arcv = canvas.create_arc(0, 0, 0, 0)
arch = canvas.create_arc(0, 0, 0, 0)
j1 = canvas.create_line(0, 0, 0 ,0)
j2 = canvas.create_line(0, 0, 0 ,0)
l1 = canvas.create_line(206, 256, 216, 306)
l2 = canvas.create_line(306, 256, 296, 306)

varstring_x = StringVar()
varstring_y = StringVar()

varstring_ratiox = StringVar()
varstring_ratioy = StringVar()

label_x = Label(root, textvariable=varstring_x)
label_x.pack()

label_y = Label(root, textvariable=varstring_y)
label_y.pack()

label_ratiox = Label(root, textvariable=varstring_ratiox)
label_ratiox.pack()

label_ratioy = Label(root, textvariable=varstring_ratioy)
label_ratioy.pack()


root.bind('<Motion>', callback)
root.mainloop()