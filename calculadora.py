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

etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.pack(pady=5)

def Sumar():
    primer_numero = int(entrada_primer_numero.get())
    segundo_numero = int(entrada_segundo_numero.get())
    etiqueta_resultado.config(text=f"Resultado: {primer_numero + segundo_numero}", fg="green")

def Restar():
    primer_numero = int(entrada_primer_numero.get())
    segundo_numero = int(entrada_segundo_numero.get())
    etiqueta_resultado.config(text=f"Resultado: {primer_numero - segundo_numero} ", fg="green")

def Dividir():
    primer_numero = int(entrada_primer_numero.get())
    segundo_numero = int(entrada_segundo_numero.get())
    if segundo_numero == 0:
        etiqueta_resultado.config(text=f"ERROR:No se puede dividir dentro de 0", fg="red")
    else:
        etiqueta_resultado.config(text=f"Resultado: {primer_numero/segundo_numero}", fg="green")

def limpiar():
    entrada_primer_numero.delete(0, tk.END)
    entrada_segundo_numero.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado:", fg="black")


boton_sumar = tk.Button(ventana, text="+", command=Sumar, highlightbackground="red", highlightcolor="blue")
boton_sumar.place(x=400, y=20)
boton_restar = tk.Button(ventana, text="-", command=Restar)
boton_restar.place(x=400, y=60)
boton_dividir = tk.Button(ventana, text="/", command=Dividir)
boton_dividir.place(x=400, y=100)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salar", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()