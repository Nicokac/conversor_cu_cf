import tkinter as tk
from tkinter import messagebox
import platform

root = tk.Tk()
root.title("Calcular cajas físicas")
root.geometry("400x300")
root.configure(bg="#4B6587")

label_style = {'bg': '#4B6587', 'fg': "white"}
entry_style = {'bg': '#D3D3D3', 'fg': "black"}

min_sku = 0.237
max_sku = 3
cons = 5.678

main_frame = tk.Frame(root, bg='#4B6587', padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

def validar_entradas(cajas_unitarias, sku, empaque):
    """
    Valida que los valores ingresados sean válidos.
    Retorna un mensaje de error si la validación falla, o None si es correcta.
    """
    if not cajas_unitarias or not sku or not empaque:
        return "Por favor, complete todos los campos"
    try:
        cajas_unitarias = int(cajas_unitarias)
        sku = float(sku)
        empaque = int(empaque)
    except ValueError:
        return "Por favor, ingrese solo números válidos"
    if cajas_unitarias <= 0 or sku <= 0 or empaque <= 0:
        return "Por favor, ingrese un número mayor a 0"
    if sku < min_sku or sku > max_sku:
        return f"El SKU debe estar entre {min_sku} y {max_sku} litros"
    return None

def calcular_cf():
    """
    Calcula las cajas físicas en base a los valores ingresados.
    Muestra el resultado o un mensaje de error en la interfaz.
    """
    try:
        cajas_unitarias = entry_cajas_unitarias.get()
        sku = entry_sku.get()
        empaque = entry_empaque.get()

        # Validar entradas
        error = validar_entradas(cajas_unitarias, sku, empaque)
        if error:
            error_label.config(text=error)
            return

        # Calcular cajas físicas
        lts_bebida = int(cajas_unitarias) * cons
        cant_botellas = lts_bebida / float(sku)
        cajas_fisicas = cant_botellas / int(empaque)

        # Mostrar resultado
        entry_cajas_fisicas.config(state="normal")
        entry_cajas_fisicas.delete(0, tk.END)
        entry_cajas_fisicas.insert(0, f"{cajas_fisicas:.2f}")
        entry_cajas_fisicas.config(state="readonly")
        error_label.config(text="")

    except ZeroDivisionError:
        error_label.config(text="El empaque no puede ser 0")
    except ValueError:
        error_label.config(text="Por favor, ingrese valores válidos")

def limpiar_datos():
    """
    Restablece todos los campos de entrada y el mensaje de error a sus valores iniciales.
    """
    entry_cajas_unitarias.delete(0, tk.END)
    entry_sku.delete(0, tk.END)
    entry_empaque.delete(0, tk.END)
    entry_cajas_fisicas.config(state="normal")
    entry_cajas_fisicas.delete(0, tk.END)
    entry_cajas_fisicas.insert(0, "0.00")
    entry_cajas_fisicas.config(state="readonly")
    error_label.config(text="Formulario listo para nuevos datos")

def mostrar_info():
    """Muestra la información del proyecto y las versiones utilizadas."""
    info = (
        "Calculadora de Cajas Físicas\n\n"
        f"Versión de Python: {platform.python_version()}\n"
        f"Versión de Tkinter: {tk.TkVersion}\n"
        f"Versión del proyecto: 1.0\n"
        "Creador: Nicolás Kachuk\n\n"
        "Enlaces:\n"
        "1. GitHub: Nicokac\n"
        "2. LinkedIn: Nicolás Kachuk\n"
    )
    messagebox.showinfo("Información", info)

def salir():
    """Cierra la aplicación."""
    root.quit()

# Barra de menú
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Menú principal
menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Salir", command=salir)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

menu_ayuda = tk.Menu(menu_bar, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=mostrar_info)
menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

# Título principal
titulo = tk.Label(main_frame, text="Conversión CU a CF", bg='#4B6587', fg='white', font=('Arial', 12, 'bold'))
titulo.grid(row=0, column=0, columnspan=2, pady=5)

# Separador
separador = tk.Frame(main_frame, bg='white', height=2)
separador.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)

# Entradas y etiquetas
tk.Label(main_frame, text="Cant. cajas unitarias:", **label_style).grid(row=2, column=0, sticky="w", pady=5)
entry_cajas_unitarias = tk.Entry(main_frame, **entry_style)
entry_cajas_unitarias.grid(row=2, column=1, pady=5)
entry_cajas_unitarias.insert(0, "1")

tk.Label(main_frame, text="Formato botella (lts):", **label_style).grid(row=3, column=0, sticky="w", pady=5)
entry_sku = tk.Entry(main_frame, **entry_style)
entry_sku.grid(row=3, column=1, pady=5)
entry_sku.insert(0, "0.5")

tk.Label(main_frame, text="Empaque (cant. bot.):", **label_style).grid(row=4, column=0, sticky="w", pady=5)
entry_empaque = tk.Entry(main_frame, **entry_style)
entry_empaque.grid(row=4, column=1, pady=5)
entry_empaque.insert(0, "6")

tk.Label(main_frame, text="Cant. cajas físicas:", **label_style).grid(row=5, column=0, sticky="w", pady=5)
entry_cajas_fisicas = tk.Entry(main_frame, **entry_style, state="readonly")
entry_cajas_fisicas.grid(row=5, column=1, pady=5)
entry_cajas_fisicas.insert(0, "0.00")

# Botón de cálculo
boton_calcular = tk.Button(main_frame, text="Calcular", command=calcular_cf, bg='#6D8299', fg='white')
boton_calcular.grid(row=6, column=0, pady=10)

# Botón de limpiar
boton_limpiar = tk.Button(main_frame, text="Limpiar", command=limpiar_datos, bg='#FF6F61', fg='white')
boton_limpiar.grid(row=6, column=1, pady=10)

# Mensaje de error
error_label = tk.Label(main_frame, text="Complete todos los campos y presione Calcular", bg='#4B6587', fg="red", font=('Arial', 10))
error_label.grid(row=7, column=0, columnspan=2, pady=5)

root.mainloop()
