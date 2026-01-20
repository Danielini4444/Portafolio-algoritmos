import tkinter as tk
from tkinter import messagebox, ttk

class NutriMindGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NutriMind Pro ✨")
        self.root.geometry("450x650")
        self.root.configure(bg="#f5f5f5")
        
        # Base de Conocimiento
        self.alimentos = {
            "Perder Grasa": "Enfoque: Proteína magra (pollo, pescado) y mucha fibra (vegetales).",
            "Mantenerse": "Enfoque: Balance general entre granos integrales, grasas sanas y proteína.",
            "Ganar Músculo": "Enfoque: Superávit calórico con extra de carbohidratos complejos y proteína."
        }

        self.crear_interfaz()

    def crear_interfaz(self):
        # Título
        tk.Label(self.root, text="NutriMind Pro", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#2e7d32").pack(pady=10)
        tk.Label(self.root, text="Tu sistema experto en nutrición", font=("Helvetica", 10), bg="#f5f5f5").pack()

        # Formulario
        frame = tk.Frame(self.root, bg="#f5f5f5")
        frame.pack(pady=20, padx=20)

        fields = [("Peso (kg):", "peso"), ("Altura (cm):", "altura"), ("Edad:", "edad")]
        self.entries = {}

        for i, (label, var) in enumerate(fields):
            tk.Label(frame, text=label, bg="#f5f5f5").grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(frame)
            entry.grid(row=i, column=1, padx=10)
            self.entries[var] = entry

        # Género
        tk.Label(frame, text="Género:", bg="#f5f5f5").grid(row=3, column=0, sticky="w", pady=5)
        self.genero = ttk.Combobox(frame, values=["Hombre", "Mujer"], state="readonly")
        self.genero.grid(row=3, column=1, padx=10)
        self.genero.current(0)

        # Actividad
        tk.Label(frame, text="Actividad:", bg="#f5f5f5").grid(row=4, column=0, sticky="w", pady=5)
        self.actividad = ttk.Combobox(frame, values=["Sedentario", "Ligero", "Activo"], state="readonly")
        self.actividad.grid(row=4, column=1, padx=10)
        self.actividad.current(0)

        # Objetivo
        tk.Label(frame, text="Meta:", bg="#f5f5f5").grid(row=5, column=0, sticky="w", pady=5)
        self.meta = ttk.Combobox(frame, values=["Perder Grasa", "Mantenerse", "Ganar Músculo"], state="readonly")
        self.meta.grid(row=5, column=1, padx=10)
        self.meta.current(1)

        # Botón
        btn = tk.Button(self.root, text="Calcular mi Plan ✨", command=self.calcular, bg="#2e7d32", fg="white", font=("bold"), relief="flat", padx=20)
        btn.pack(pady=20)

        # Resultado
        self.res_text = tk.Text(self.root, height=10, width=50, font=("Helvetica", 9), state="disabled", bg="#e8f5e9")
        self.res_text.pack(padx=20, pady=10)

    def calcular(self):
        try:
            p = float(self.entries['peso'].get())
            a = float(self.entries['altura'].get())
            e = int(self.entries['edad'].get())
            
            # Motor de Inferencia (Echo)
            if self.genero.get() == "Hombre":
                tmb = (10 * p) + (6.25 * a) - (5 * e) + 5
            else:
                tmb = (10 * p) + (6.25 * a) - (5 * e) - 161
            
            factores = {"Sedentario": 1.2, "Ligero": 1.375, "Activo": 1.55}
            calorias = tmb * factores[self.actividad.get()]
            
            ajustes = {"Perder Grasa": -500, "Mantenerse": 0, "Ganar Músculo": 400}
            total = calorias + ajustes[self.meta.get()]
            
            # Mostrar resultado (Valen)
            self.res_text.config(state="normal")
            self.res_text.delete(1.0, tk.END)
            res = (f"¡Listo, Dani! Aquí tienes tu plan:\n\n"
                   f"🎯 Meta: {self.meta.get()}\n"
                   f"🔥 Calorías diarias: {round(total)} kcal\n"
                   f"💡 {self.alimentos[self.meta.get()]}\n\n"
                   f"¡Dale con todo, recuerda que cada paso cuenta! 🍎")
            self.res_text.insert(tk.END, res)
            self.res_text.config(state="disabled")

        except ValueError:
            messagebox.showerror("Error", "Ay Dani, checa tus datos. ¡Usa solo números!")

if __name__ == "__main__":
    root = tk.Tk()
    app = NutriMindGUI(root)
    root.mainloop()