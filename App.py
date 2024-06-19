import tkinter as tk

from Modelo.Calculadora import Calculadora

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()