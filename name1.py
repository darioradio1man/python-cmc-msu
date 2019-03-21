from tkinter import *
from tkinter import messagebox as mb
import random
root = Tk()
root.title("First, ПЕРВЫЙ!")
root.geometry("400x300")
# L = Label(root, text="text")


def fnB(*args):
    print(args, "QQ")
    root.destroy()


def get_random_color():
    r = lambda: random.randint(0, 255)
    new_color = '#%02X%02X%02X' % (r(), r(), r())
    return new_color


def change_color(rand_number):
    root.config(bg=rand_number)


def combine_colors():
    new_color = get_random_color()
    change_color(new_color)


button = Button(root, command=fnB, text="Butt OFF")
button.grid(row=1, column=1)

# button.bind('Button 1', fnB) # 2ой способ забиндить

# это вторая кнопка, отвечает за цвет
button_hello = Button(root, command=combine_colors, text="Color")
button_hello.grid(row=1, column=2)
root.configure(bg=get_random_color())


# кнопка проверяет, являются ли введенные символы числом
def check():
    s = entry.get()
    if s.isdigit() == FALSE:
        mb.showerror("Ошибка", "Должно быть введено число")
    else:
        entry.delete(0, END)
        label['text'] = s


entry = Entry()
entry.grid(row=2, column=1)
Button(text='Передать', command=check).grid(row=1, column=3)
label = Label(height=1)
label.grid(row=2, column=2)


root.mainloop()
