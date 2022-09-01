import math
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

greeting = Label(text="Cálculo de tensão em duas linhas flexiveis conectadas a 1 peso")
greeting.grid(row=0, column=0, columnspan=3)


# Comando do botão
def cal_sum():
    a1 = int(a.get())
    a2 = int(b.get())
    ps = int(p.get())

    t = ps / (math.cos(math.radians(a2)) / math.cos(math.radians(a1)) * math.sin(math.radians(a1)) + math.sin(
        math.radians(a2)))
    tl = t * ((math.cos(math.radians(a2))) / (math.cos(math.radians(a1))))

    result_t.config(text=t)
    result_tl.config(text=tl)


# Entradas de dados
ent_a = Label(text="Valor de A1")
ent_a.grid(row=1, column=0)
a = Entry()
a.grid(row=2, column=0)

ent_b = Label(text="Valor de A2")
ent_b.grid(row=3, column=0)
b = Entry()
b.grid(row=4, column=0)

ent_p = Label(text="Valor de P")
ent_p.grid(row=5, column=0)
p = Entry()
p.grid(row=6, column=0)

# Botão para realizar o calculo
calc = Button(text="calcular", command=cal_sum)
calc.grid(row=7, column=0, columnspan=3, padx=10, pady=10, )

# Resultados

id_t = Label(text="Valor de T").grid(row=1, column=1)
result_t = Label()
result_t.grid(row=2, column=1)

id_tl = Label(text="Valor de TL").grid(row=3, column=1)
result_tl = Label()
result_tl.grid(row=4, column=1)

# Imagem de exemplo
img_frame = LabelFrame(pady=30)
img_frame.grid(row=8, column=0, columnspan=2)
img_label_ex = Label(img_frame, text="exemplo de aplicação")
img_label_ex.grid(row=9, column=0, columnspan=2)
img_ex = ImageTk.PhotoImage(Image.open("ex1.JPG"))
img_label = Label(img_frame, image=img_ex)
img_label.grid(row=10, column=0, columnspan=2)


root.mainloop()

