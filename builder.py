import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import networkx as nx
import numpy as np


class SimpleTableInput(tk.Frame):

    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)
        self._entry = {}
        self.rows = rows
        self.columns = columns
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self)
                e.grid(row=row, column=column, stick="nsew")
                e.insert(0, '0')
                self._entry[index] = e
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(int(self._entry[index].get()))
            result.append(current_row)
        self.matrix = np.array(result)
        return result


class Example(tk.Frame):
    def __init__(self, parent, n):
        tk.Frame.__init__(self, parent)
        self.table = SimpleTableInput(self, n, n)
        self.submit = tk.Button(self, text="Submit", command=self.on_submit)
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="bottom")
        self.graph=nx.complete_graph(2)

    def on_submit(self):
        matrix = self.table.get()
        matrix = np.array(matrix)
        print(matrix)

def eval_graph():
    global table
    print(eval("nx.diameter(table.graph)"))


def build_graph():
    # global table
    matrix = table.table.get()
    matrix = np.array(matrix)

    f = plt.figure(figsize=(5, 4))
    a = f.add_subplot(111)
    plt.axis('off')

    G = nx.from_numpy_matrix(matrix)
    table.graph=G
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos=pos, ax=a)
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    b3 = tk.Button(root, text="eval_graph", command=eval_graph)
    b3.pack(side='top')


def create_matrix():
    global table

    n = int(e1.get())
    table = Example(root, n)  # .pack(side="left") ERROR
    table.pack(side="left")
    b2 = tk.Button(root, text="Build Graph", command=build_graph)
    b2.pack(side='top')


root = tk.Tk()
b1 = tk.Button(root, text="Number of points", command=create_matrix)
e1 = tk.Entry(root)
e1.insert(0, '0')
b1.pack(side='right')
e1.pack(side='right')
matrix = []
root.mainloop()
