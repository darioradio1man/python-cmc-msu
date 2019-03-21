from tkinter import *
root = Tk()
root.title("First, ПЕРВЫЙ!")
# root.geometry("400x300")
# L = Label(root, text="text")


def fnB(*args):
    print(args, "QQ")
    root.destroy()


button = Button(root, command=fnB, text="Butt ON")
button.grid()
# button.bind('Button 1', fnB) # 2ой способ забиндить
root.mainloop()

