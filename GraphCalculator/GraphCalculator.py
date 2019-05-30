import tkinter as tk
from tkinter import font as tkfont
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import numpy as np
import gettext
import os.path
import sys

datapath = os.path.dirname(sys.argv[0])
gettext.install('messages', datapath)


matrix = np.zeros((10, 10))
l = [0] * 10
f = [0] * 10
e = [0] * 10


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18,
                                      weight="bold", slant="italic")

        self.title(_("Graph algorithms visualiser"))
        self.configure(bg='#E1ECED')
        self.geometry("1000x500+300+200")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, ErrorPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def vertices_button(self):
        global l, f, e
        num = int(self.entry_number_v.get())
        l = [0] * 10
        f = [0] * 10
        e = [0] * 10
        for i in range(0, num):
            l[i] = tk.Label(self, text=_("Neighbours of ") + str(i + 1) + _("st vertex:"),
                            font='helvetica 15', fg='#27415D', bd=2)
            f[i] = tk.Frame(self, bg='#92BBBF', width=7, height=1, relief=tk.SUNKEN)
            e[i] = tk.Entry(f[i], fg='#27415D', width=15)
            l[i].place(x=40, y=75 + 28*i)
            f[i].place(x=230, y=75 + 28*i)
            e[i].grid()

    def ok_button(self):
        global matrix
        n = int(self.entry_number_v.get())
        matrix = np.zeros((n, n))
        for i in range(0, n):
            vertices_list = e[i].get().split(',')
            for j in range(0, len(vertices_list)):
                v = int(vertices_list[j])
                matrix[i][v - 1] = 1
        flag = 1
        for i in range(0, n):
            for j in range(i, n):
                if matrix[i][j] != matrix[j][i]:
                    flag = 0
        if flag == 0:
            self.controller.show_frame("ErrorPage")
        elif self.var.get() == 0:
            self.controller.show_frame("ErrorPage")
        elif self.var.get() == 1:
            self.controller.show_frame("PageOne")
        elif self.var.get() == 2:
            self.controller.show_frame("PageTwo")
        elif self.var.get() == 3:
            self.controller.show_frame("PageThree")
        print(matrix)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#E1ECED')

        label_graph = tk.Label(self, text=_("Enter number of vertices:"),
                               font='helvetica 18', fg='#27415D', bd=2)
        label_graph.place(x=40, y=25)

        self.frame_number_v = tk.Frame(self, bg='#92BBBF', bd=1)
        self.frame_ok_v = tk.Frame(self, bg='#92BBBF', bd=2)
        self.entry_number_v = tk.Entry(self.frame_number_v, fg='#27415D',
                                       width=3)
        self.button_vertices = tk.Button(self.frame_ok_v, text=_("OK!"),
                                         fg='#27415D', width=4, height=2,
                                         command=self.vertices_button)
        self.frame_number_v.place(x=255, y=25)
        self.frame_ok_v.place(x=300, y=22)
        self.entry_number_v.grid()
        self.button_vertices.grid()

        self.frame_ok = tk.Frame(self, bg='#92BBBF', bd=20)
        self.button_ok = tk.Button(self.frame_ok, text=_("OK!"), fg='#27415D',
                                   width=75, height=2, command=self.ok_button)
        self.frame_ok.place(x=125, y=400)
        self.button_ok.grid()

        self.label_alg = tk.Label(self, text=_("Choose an algorithm:"),
                                  font='helvetica 18', fg='#27415D', bd=2)
        self.label_alg.place(x=500, y=25)

        self.var = tk.IntVar()
        self.rbutton1 = tk.Radiobutton(self, text=_("Depth-first spanning tree"),
                                       variable=self.var, value=1)
        self.rbutton2 = tk.Radiobutton(self, text=_("Breadth-first spanning tree"),
                                       variable=self.var, value=2)
        self.rbutton3 = tk.Radiobutton(self, text=_("Something =)"),
                                       variable=self.var, value=3)
        self.rbutton1.place(x=500, y=75)
        self.rbutton2.place(x=500, y=103)
        self.rbutton3.place(x=500, y=131)


class PageOne(tk.Frame):

    def use_method(self):
        global matrix
        f = plt.figure(figsize=(5, 4))
        a = f.add_subplot(111)
        plt.axis('off')

        G = nx.from_numpy_matrix(matrix)
        pos = nx.circular_layout(G)
        nx.draw_networkx(G, pos=pos, ax=a, edge_color='b')
        nx.draw_networkx(nx.dfs_tree(G), pos=pos, ax=a, edge_color='r')
        canvas = FigureCanvasTkAgg(f, master=self)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#E1ECED')

        label = tk.Label(self, text=_("Method 1"), font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=_("Again!"),
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button = tk.Button(self, text=_("Use Method!"),
                           command=self.use_method)
        button.pack()


class PageTwo(tk.Frame):

    def use_method(self):
        global matrix
        f = plt.figure(figsize=(5, 4))
        a = f.add_subplot(111)
        plt.axis('off')

        G = nx.from_numpy_matrix(matrix)
        pos = nx.circular_layout(G)
        nx.draw_networkx(G, pos=pos, ax=a, edge_color='b')
        nx.draw_networkx(nx.bfs_tree(G, 0), pos=pos, ax=a, edge_color='r')
        canvas = FigureCanvasTkAgg(f, master=self)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#E1ECED')

        label = tk.Label(self, text=_("Method 2"), font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=_("Again!"),
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button = tk.Button(self, text=_("Use Method!"),
                           command=self.use_method)
        button.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#E1ECED')

        label = tk.Label(self, text=_("Method 3"), font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=_("Again!"),
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class ErrorPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='#E1ECED')

        label = tk.Label(self, text=_("Error! Please return and check if all the "
                                      "parameters are valid."),
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text=_("Return!"),
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
