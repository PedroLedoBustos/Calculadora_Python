import tkinter as tk  # Importar la biblioteca tkinter para crear interfaces gráficas

class Calculadora:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora")
        self.raiz.geometry("400x500")
        
        self.entrada_actual = ""
        
        # Crear el widget de entrada
        self.display = tk.Entry(raiz, font=("Arial", 24), borderwidth=2, relief="solid")
        self.display.pack(expand=True, fill="both")
        
        # Crear un marco para los botones
        self.marco_botones = tk.Frame(raiz)
        self.marco_botones.pack(expand=True, fill="both")
        
        self.crear_botones()
        
    def crear_botones(self):
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]
        
        fila = 0
        columna = 0
        
        for texto_boton in botones:
            boton = tk.Button(self.marco_botones, text=texto_boton, font=("Arial", 18), borderwidth=1, relief="solid", command=lambda bt=texto_boton: self.clic_boton(bt))
            boton.grid(row=fila, column=columna, sticky=tk.NSEW)
            
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1
                
        for i in range(4):
            self.marco_botones.columnconfigure(i, weight=1)
            self.marco_botones.rowconfigure(i, weight=1)
            
    def clic_boton(self, caracter):
        if caracter == "=":
            self.calcular_resultado()
        elif caracter == "C":
            self.entrada_actual = ""
            self.actualizar_display()
        else:
            self.entrada_actual += str(caracter)
            self.actualizar_display()
            
    def actualizar_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.entrada_actual)
        
    def calcular_resultado(self):
        try:
            resultado = str(eval(self.entrada_actual))
            self.entrada_actual = resultado
            self.actualizar_display()
        except Exception:
            self.entrada_actual = ""
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")