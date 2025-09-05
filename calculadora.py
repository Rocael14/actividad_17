import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x500")

etiqueta_primer_numero = tk.Label(ventana, text="Ingresa un numero:")
etiqueta_primer_numero.pack(pady=5)

entrada_primer_numero = tk.Entry(ventana)
entrada_primer_numero.pack(pady=5)

etiqueta_segundo_numero = tk.Label(ventana, text="Ingresa un numero:")
etiqueta_segundo_numero.pack(pady=5)

entrada_segundo_numero = tk.Entry(ventana)
entrada_segundo_numero.pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="Resultado:", font=("Arial", 10, "bold"))
etiqueta_resultado.pack(pady=5)
try:
    imagen_boton_basura = tk.PhotoImage(file="trash.png")
    imagen_boton = tk.PhotoImage(file="exit.png")
except tk.TclError:
    print("Error: No se encontró la imagen 'exit.png'.")
    imagen_boton_basura = None
    imagen_boton = None
def Sumar():
    primer_numero = int(entrada_primer_numero.get())
    segundo_numero = int(entrada_segundo_numero.get())
    etiqueta_resultado.config(text=f"Resultado: {primer_numero+segundo_numero}", fg="green",font=("Arial", 24, "bold"))

def Restar():
    primer_numero = int(entrada_primer_numero.get())
    segundo_numero = int(entrada_segundo_numero.get())
    etiqueta_resultado.config(text=f"Resultado: {primer_numero - segundo_numero} ", fg="green",font=("Arial", 24, "bold"))

def Dividir():
    primer_numero = int(entrada_primer_numero.get())
    segundo_numero = int(entrada_segundo_numero.get())
    if segundo_numero == 0:
        etiqueta_resultado.config(text=f"ERROR:No se puede dividir dentro de 0", fg="red", font=("Arial", 10, "bold"))
    else:
        etiqueta_resultado.config(text=f"Resultado: {primer_numero/segundo_numero}", fg="green",font=("Arial", 24, "bold"))

def limpiar():
    entrada_primer_numero.delete(0, tk.END)
    entrada_segundo_numero.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado:", fg="black", font=("Arial", 10, "bold"))


boton_sumar = tk.Button(ventana, text="+", command=Sumar,  width=4, height=1,bg="black" ,fg="white",activebackground="grey", activeforeground="black",font=("Arial", 24, "bold"))
boton_sumar.place(x=50, y=200)
boton_restar = tk.Button(ventana, text="-", command=Restar,  width=4,bg="black" ,fg="white",activebackground="grey", activeforeground="black",font=("Arial", 24, "bold"))
boton_restar.place(x=150, y=200)
boton_dividir = tk.Button(ventana, text="/", command=Dividir,  width=4,bg="black" ,fg="white",activebackground="grey", activeforeground="black",font=("Arial", 24, "bold"))
boton_dividir.place(x=250, y=200)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, image=imagen_boton_basura,borderwidth=0, highlightthickness=0)
boton_limpiar.place(x=400, y=200)

boton_salir = tk.Button(ventana, text="Salar", command=ventana.quit, image=imagen_boton,borderwidth=0, highlightthickness=0)
boton_salir.place(x=400, y=30)

ventana.mainloop()