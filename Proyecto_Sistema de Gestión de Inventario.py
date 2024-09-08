# Sistema de Gestión de Inventario

import tkinter as tk
from tkinter import messagebox

# Estructura del inventario: un diccionario con ID del producto como clave y un diccionario con detalles del producto
inventario = {}

# Función para agregar un producto al inventario
def agregar_producto():
    id_producto = entry_id.get()
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()
    
    if id_producto in inventario:
        messagebox.showerror("Error", f"El producto con ID {id_producto} ya existe.")
    else:
        try:
            cantidad = int(cantidad)
            precio = float(precio)
            inventario[id_producto] = {'nombre': nombre, 'cantidad': cantidad, 'precio': precio}
            messagebox.showinfo("Éxito", f"Producto {nombre} agregado con éxito.")
            limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero y el precio un número decimal.")

# Función para eliminar un producto del inventario
def eliminar_producto():
    id_producto = entry_id.get()
    if id_producto in inventario:
        del inventario[id_producto]
        messagebox.showinfo("Éxito", f"Producto con ID {id_producto} eliminado.")
        limpiar_campos()
    else:
        messagebox.showerror("Error", f"El producto con ID {id_producto} no se encuentra en el inventario.")

# Función para buscar un producto por su ID
def buscar_producto():
    id_producto = entry_id.get()
    if id_producto in inventario:
        producto = inventario[id_producto]
        messagebox.showinfo("Producto encontrado", f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']:.2f}")
    else:
        messagebox.showerror("Error", f"El producto con ID {id_producto} no está en el inventario.")

# Función para listar todos los productos en el inventario
def listar_inventario():
    if inventario:
        listado = "\n".join([f"ID: {id_p}, Nombre: {datos['nombre']}, Cantidad: {datos['cantidad']}, Precio: ${datos['precio']:.2f}" for id_p, datos in inventario.items()])
        messagebox.showinfo("Inventario", listado)
    else:
        messagebox.showinfo("Inventario", "El inventario está vacío.")

# Función para actualizar la cantidad de un producto
def actualizar_cantidad():
    id_producto = entry_id.get()
    nueva_cantidad = entry_cantidad.get()
    
    if id_producto in inventario:
        try:
            nueva_cantidad = int(nueva_cantidad)
            inventario[id_producto]['cantidad'] = nueva_cantidad
            messagebox.showinfo("Éxito", f"Cantidad actualizada para el producto {inventario[id_producto]['nombre']}.")
            limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")
    else:
        messagebox.showerror("Error", f"El producto con ID {id_producto} no se encuentra en el inventario.")

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Inventario")

# Crear los widgets de la interfaz
label_id = tk.Label(ventana, text="ID del Producto")
label_id.grid(row=0, column=0)

entry_id = tk.Entry(ventana)
entry_id.grid(row=0, column=1)

label_nombre = tk.Label(ventana, text="Nombre del Producto")
label_nombre.grid(row=1, column=0)

entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=1, column=1)

label_cantidad = tk.Label(ventana, text="Cantidad")
label_cantidad.grid(row=2, column=0)

entry_cantidad = tk.Entry(ventana)
entry_cantidad.grid(row=2, column=1)

label_precio = tk.Label(ventana, text="Precio")
label_precio.grid(row=3, column=0)

entry_precio = tk.Entry(ventana)
entry_precio.grid(row=3, column=1)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar Producto", command=agregar_producto)
btn_agregar.grid(row=4, column=0, pady=10)

btn_eliminar = tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto)
btn_eliminar.grid(row=4, column=1)

btn_buscar = tk.Button(ventana, text="Buscar Producto", command=buscar_producto)
btn_buscar.grid(row=5, column=0)

btn_listar = tk.Button(ventana, text="Listar Inventario", command=listar_inventario)
btn_listar.grid(row=5, column=1)

btn_actualizar = tk.Button(ventana, text="Actualizar Cantidad", command=actualizar_cantidad)
btn_actualizar.grid(row=6, column=0)

btn_limpiar = tk.Button(ventana, text="Limpiar Campos", command=limpiar_campos)
btn_limpiar.grid(row=6, column=1)

# Ejecutar la aplicación
ventana.mainloop()
