import tkinter as tk
import numpy as np
import pandas as pd
import math
from scipy.spatial.distance import pdist
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def print_codigo_seleccionado(conductor):
    print("Código de conductor seleccionado:", conductor)
    conductor_seleccionado2.set(conductor)
    obtener_valor_rmg()

def obtener_valor_rmg():
    TipoConductor = conductor_seleccionado.get()
    CodConductor = conductor_seleccionado2.get()
    datos = pd.read_excel('Conductores.xlsx', sheet_name=TipoConductor, skiprows=[0,1])
    datos.set_index('Codigo', inplace=True)
    RMG = datos.at[CodConductor, 'RMG']
    print("El valor del GMR es: ", RMG , "mm")

    return RMG

def obtener_valor_diametro():
    TipoConductor = conductor_seleccionado.get()
    CodConductor = conductor_seleccionado2.get()
    datos = pd.read_excel('Conductores.xlsx', sheet_name=TipoConductor, skiprows=[0,1])
    datos.set_index('Codigo', inplace=True)
    diametro = datos.at[CodConductor, 'Diam_Tot']
    print("El valor del diametro es: ", diametro , "mm")

    return diametro

def obtener_valor_Rac():
    TipoConductor = conductor_seleccionado.get()
    CodConductor = conductor_seleccionado2.get()
    datos = pd.read_excel('Conductores.xlsx', sheet_name=TipoConductor, skiprows=[0,1])
    datos.set_index('Codigo', inplace=True)
    Rac = datos.at[CodConductor, 'R_ac_75']
    print("El valor de la resistencia ac es: ", Rac, "ohm/km")

    return Rac


def mostrar_conductor_seleccionado():
    print("Tipo de conductor seleccionado:", conductor_seleccionado.get())
    print("Conductor específico seleccionado:", conductor_seleccionado2.get())
    
def actualizar_valor(*args):
    global valor_linea
    valor_linea = 1 if largo_tipo.get() == "Con pérdidas" else 0
    print("Valor de valor_linea:", valor_linea)  # Imprime el valor para verificar
    
    return valor_linea

def imprimir_modulo_y_angulo(real, imaginario):
    # Calcular el módulo
    modulo = np.sqrt(real**2 + imaginario**2) 
    # Calcular el ángulo en radianes
    angulo_rad = np.arctan2(imaginario, real)
    # Convertir el ángulo a grados
    angulo= np.rad2deg(angulo_rad)
    
    return modulo,angulo

def actualizar_desplegable(*args):
    TipoConductor = conductor_seleccionado.get()
    menu_desplegable2['menu'].delete(0, 'end')

    if TipoConductor == "ACSR":
        CodConductor = ["Bittern", "Bluebird", "Bluejay", "Bobolink", "Brahma", "Brant", "Bunting", "Canary", 
                              "Cardinal", "Chicadee", "Chuckar", "Cochin", "Condor", "Cukoo", "Curlew", "Dipper", 
                              "Dorking", "Dotterel", "Dove", "Drake", "Eagle", "Falcon", "Finch", "Flamingo", 
                              "Flicker", "Gannet", "Grackle", "Grosbeack", "Guinea", "Hawk", "Hen", "Ibis", 
                              "Joree", "Kingbird", "Kiwi", "Lapwing", "Lark", "Legthorn", "Linnet", "Martin", 
                              "Merlin", "Minorca", "Nuthatch", "Oriole", "Ortolan", "Osprey", "Ostrich", 
                              "Parakeet", "Parrot", "Partridge", "Peacock", "Pelican", "Petrel", "Pheasant", 
                              "Piper", "Plover", "Rail", "Rook", "Ruddy", "Scoter", "Skimmer", "Squab", 
                              "Starling", "Stilt", "Tern", "Thrasher", "Waxwing", "Wood Duck"]
    elif TipoConductor == "ACAR":
        CodConductor = ["250-12/7", "300-12/7", "350-12/7", "400-12/7", "450-12/7", "500-12/7", "500-18/19", 
                              "500-24/13", "500-30/7", "550-12/7", "550-18/20", "550-24/14", "550-30/7", "600-12/7", 
                              "600-18/21", "600-24/15", "600-30/7", "650-18/22", "650-24/16", "650-30/7", "700-18/23", 
                              "700-24/17", "700-30/7", "750-18/24", "750-24/18", "750-30/7", "800-18/25", "800-24/19", 
                              "800-30/7", "850-18/26", "850-24/20", "850-30/7", "900-18/27", "900-24/21", "900-30/7", 
                              "950-18/28", "950-24/22", "950-30/7", "1000-18/29", "1000-24/23", "1000-30/7", "1050-18/30", 
                              "1050-24/24", "1050-30/7", "1100-24/25", "1100-18/31", "1100-30/7", "1200-24/26", "1200-30/7", 
                              "1200-18/32"]
    elif TipoConductor== "AAAC":
        CodConductor = ["Akron", "Alton", "Ames", "Astoria", "Azusa", "Anaheim", "Amherst", "Alliance", "Butte", 
                              "Canton", "Cairo", "Darien", "Elgin", "Flint", "Greeley"]
    else:
        CodConductor = []

    for conductor in CodConductor:
        menu_desplegable2['menu'].add_command(label=conductor, command=lambda c=conductor: print_codigo_seleccionado(c))
        

def actualizar_matriz():
    for widget in contenedor_matriz.winfo_children():
        widget.destroy()
    
    num_circuitos = int(circuitos_var.get())
    filas = 3
    columnas = 2 if num_circuitos == 1 else 2
    
    etiquetas1 = ["a1", "b1", "c1"]
    etiquetas2 = ["a2", "b2", "c2"]
    
    if num_circuitos == 1:
        tk.Label(contenedor_matriz, text="x(m)").grid(row=0, column=1, padx=2, pady=2)
        tk.Label(contenedor_matriz, text="y(m)").grid(row=0, column=2, padx=2, pady=2)
        
    for i in range(filas):
        tk.Label(contenedor_matriz, text=etiquetas1[i]).grid(row=i + 1, column=0, padx=2, pady=2, sticky="e")
        for j in range(columnas):
            entry = tk.Entry(contenedor_matriz, width=10)
            entry.grid(row=i + 1, column=j + 1, padx=2, pady=2)
        
        if num_circuitos == 2:
            tk.Label(contenedor_matriz, text="x(m)").grid(row=0, column=1, padx=2, pady=2)
            tk.Label(contenedor_matriz, text="y(m)").grid(row=0, column=2, padx=2, pady=2)
            tk.Label(contenedor_matriz, text="x(m)").grid(row=0, column=5, padx=2, pady=2)
            tk.Label(contenedor_matriz, text="y(m)").grid(row=0, column=6, padx=2, pady=2)
            
            tk.Label(contenedor_matriz, text=etiquetas2[i]).grid(row=i + 1, column=3, padx=2, pady=2, sticky="e")
            for j in range(columnas):
                entry = tk.Entry(contenedor_matriz, width=10)
                entry.grid(row=i + 1, column=j + 5, padx=2, pady=2)
    
   # contenedor_matriz.grid_propagate(False)
    contenedor_matriz.columnconfigure(1, minsize=50)
    contenedor_matriz.columnconfigure(2, minsize=50)
    contenedor_matriz.config(width=200, height=100)
    actualizar_campo_distancia()


def actualizar_campo_distancia():
    num_conductores = int(num.get())
    if num_conductores > 1:
        distancia_label.grid(row=4, column=0, padx=10, pady=2, sticky="w")
        distancia_entry.grid(row=4, column=1, padx=10, pady=2)
    else:
        distancia_label.grid_forget()
        distancia_entry.grid_forget()
    
    return num_conductores

#%%
def generar_grafica():
    global ax1, ay1, bx1, by1, cx1, cy1, ax2, ay2, bx2, by2, cx2, cy2
    
    x_values = []
    y_values = []
    distancia = float(distancia_entry.get()) if distancia_entry.get() else 0
    obtener_valor_diametro()
    
    for widget in contenedor_matriz.winfo_children():
        if isinstance(widget, tk.Entry):
            value = widget.get()
            if value:
                column = widget.grid_info()["column"]
                if column % 2 == 1:
                    x_values.append(float(value))
                else:
                    y_values.append(float(value))
                    
    num_x_values = len(x_values)
   
    if num_x_values <= 3:
        ax1 = x_values[0]
        bx1 = x_values[1]
        cx1 = x_values[2]
        
        ay1 = y_values[0]
        by1 = y_values[1]
        cy1 = y_values[2]
        
        # Crear el array de posiciones
        posconf = np.array([[ax1, ay1],  # a1
                   [bx1, by1],  # b1
                   [cx1, cy1]]) # c1

        # Calcular las distancias
        distancias = pdist(posconf)
        
        dab=distancias[0]
        dac=distancias[1]
        dbc=distancias[2]
        print(dab,dac,dbc)
        GMD=(dab*dac*dbc)**(1/3)
        print("GMD",GMD)
        num_conductores= actualizar_campo_distancia()
        GMR = obtener_valor_rmg()/1000
        diametro = obtener_valor_diametro()    ## dato en mm
        r= (diametro/1000)/2                   ## en metros
        d = float(distancia_entry.get()) if distancia_entry.get() else 0       ## d= distancia entre conductores por fase ##
        print("La distancia ingresada por el usuario es:", d)  # Esta línea imprime la distancia en consola
        
        
        if num_conductores == 1:
           
            print("Número de conductores por fase: 1")

            Rac_tabla=obtener_valor_Rac()
            R=Rac_tabla/1
            print("Rac es: {:.4f} Ohm/km".format(R))
            
            GMRL = GMR
            L = 0.2 * np.log(GMD /GMR)
            
            print("L es: {:.4f} mH/km".format(L))
            diametro = obtener_valor_diametro()
            r= (diametro/1000)/2
            
            C = (0.0556/(np.log(GMD/r)))
            
            print("C es: {:.4f} uF/km".format(C))
            
            etiqueta_R.config(text=f"R = {R:.6f} Ohm/km")
            
            # Después de calcular L
            etiqueta_L.config(text=f"L = {L:.6f} mH/km")

            # Después de calcular C
            etiqueta_C.config(text=f"C = {C:.6f} nF/km")

        elif num_conductores == 2:
            print("Número de conductores por fase: 2")
            
            Rac_tabla=obtener_valor_Rac()
            R=Rac_tabla/2
            print("Rac es: {:.4f} Ohm/km".format(R))
            
            GMR_L= np.sqrt(GMR*d)
            print ("El valor del GMRL es: ", GMR_L)
            
         
            L = 0.2 * np.log(GMD/GMR_L)
            
            print("L es: {:.4f} mH/km".format(L))
            
            ##################
            #CALCULO DE C
            ##################
            
            diametro = obtener_valor_diametro()    ## dato en mm
            r= (diametro/1000)/2
            
            print("Número de conductores por fase: 2")
            GMR_C= np.sqrt(r*d)
            print ("El valor del GMRC es: ", GMR_C)
            
            
            C= (0.0556/(np.log(GMD/GMR_C)))
            
            print("C es: {:.4f} uF/km".format(C))
            
            etiqueta_R.config(text=f"R = {R:.6f} Ohm/km")
            
            # Después de calcular L
            etiqueta_L.config(text=f"L = {L:.6f} mH/km")

            # Después de calcular C
            etiqueta_C.config(text=f"C = {C:.6f} nF/km")

            
        elif num_conductores == 3:
            
            print("Número de conductores por fase: 3")
            
            Rac_tabla=obtener_valor_Rac()
            R=Rac_tabla/3
            print("Rac es: {:.4f} Ohm/km".format(R))
            
            GMR_L= (GMR * d**2)**(1/3)
            print ("El valor del GMRL es: ", GMR_L)
            
         
            L = 0.2 * np.log(GMD/GMR_L)
            
            print("L es: {:.4f} mH/km".format(L))
            
            ##################
            #CALCULO DE C
            ##################
            
            diametro = obtener_valor_diametro()    ## dato en mm
            r= (diametro/1000)/2
            
            print("Número de conductores por fase: 2")
            GMR_C= (r * d**2)**(1/3)
            print ("El valor del GMRC es: ", GMR_C)
            
            
            C= (0.0556/(np.log(GMD/GMR_C)))
            
            print("C es: {:.4f} uF/km".format(C))
            
            
            etiqueta_R.config(text=f"R = {R:.6f} Ohm/km")
            
            # Después de calcular L
            etiqueta_L.config(text=f"L = {L:.6f} mH/km")

            # Después de calcular C
            etiqueta_C.config(text=f"C = {C:.6f} nF/km")



        elif num_conductores == 4:
            print("Número de conductores por fase: 4")
            
            Rac_tabla=obtener_valor_Rac()
            R=Rac_tabla/4
            print("Rac es: {:.4f} Ohm/km".format(R))
            
            GMR_L=1.09*(GMR * d**3)**(1/4)
            print ("El valor del GMRL es: ", GMR_L)
            
         
            L = 0.2 * np.log(GMD/GMR_L)
            
            print("L es: {:.4f} mH/km".format(L))
            
            ##################
            #CALCULO DE C
            ##################
            
            diametro = obtener_valor_diametro()    ## dato en mm
            r= (diametro/1000)/2
            
            print("Número de conductores por fase: 2")
            GMR_C=1.09*(r * d**3)**(1/4)
            print ("El valor del GMRC es: ", GMR_C)
            
            
            C= (0.0556/(np.log(GMD/GMR_C)))
            
            print("C es: {:.4f} uF/km".format(C))
            
            etiqueta_R.config(text=f"R = {R:.6f} Ohm/km")
            
            # Después de calcular L
            etiqueta_L.config(text=f"L = {L:.6f} mH/km")

            # Después de calcular C
            etiqueta_C.config(text=f"C = {C:.6f} nF/km")

    else:
        ax1 = x_values[0]
        ax2 = x_values[1]
        bx1 = x_values[2]
        bx2 = x_values[3]
        cx1 = x_values[4]
        cx2 = x_values[5]
        
        ay1 = y_values[0]
        ay2 = y_values[1]
        by1 = y_values[2]
        by2 = y_values[3]
        cy1 = y_values[4]
        cy2 = y_values[5]
        
        
        posconf= np.array([[ax1,ay1], #a1
                          [bx1,by1], #b1
                          [cx1,cy1], #c1
                          [ax2,ay2], #a2
                          [bx2,by2], #b2
                          [cx2,cy2]]) #c2
        
        # Calcular las distancias
        distancias = pdist(posconf)
        
        da1b1=distancias[0]
        da1c1=distancias[1]
        da1a2=distancias[2]
        da1b2=distancias[3]
        da1c2=distancias[4]
        
        db1c1=distancias[5]
        db1a2=distancias[6]
        db1b2=distancias[7]
        db1c2=distancias[8]
        
        dc1a2=distancias[9]
        dc1b2=distancias[10]
        dc1c2=distancias[11]
        
        da2b2=distancias[12]
        da2c2=distancias[13]
        
        
        db2c2=distancias[14]
        
        #GMD ENTRE 3 FASES DE GRUPOS  
        
        GMD_AB= (da1b1*da1b2*db1a2*da2b2)**(1/4)
        #print(da1b1,da1b2,db1a2,da2b2)
        #print("")
        GMD_BC= (db1c1*db1c2*dc1b2*db2c2)**(1/4)
        #print(db1c1,db1c2,dc1b2,db2c2)
        #print("")
        GMD_AC= (da1c1*da1c2*dc1a2*da2c2)**(1/4)
        #print(da1c1,da1c2,dc1a2,da2c2)
        
        
        print("GMD_AB: ",GMD_AB,"\nGMD_BC: ",GMD_BC,"\nGMD_AC: ",GMD_AC)
        
        #GMD POR FASE CONSIDERANDO TRANSPOSICIÓN
        
        GMD=(GMD_AB*GMD_BC*GMD_AC)**(1/3)
        
        print("GMD: ", GMD)
        GMR = obtener_valor_rmg()/1000
        
       # GMR_L_n=(GMR*0.45)**(1/2)
        
        d = float(distancia_entry.get()) if distancia_entry.get() else 0       ## d= distancia entre conductores por fase ##
        print("La distancia ingresada por el usuario es:", d)  # Esta línea imprime la distancia en consola
        
        
    ###################################
    ###Calculo de parametros 
    #######################################
        num_conductores= actualizar_campo_distancia()
        
        if num_conductores == 1:
            print("Número de conductores por fase: 1")

            Rac_tabla=obtener_valor_Rac()
            R=Rac_tabla/2
            print("Rac es: {:.4f} Ohm/km".format(R))
            
            GMRL = GMR
            L = 0.2 * np.log(GMD / GMRL)
            
            print("L es: {:.4f} mH/km".format(L))
            diametro = obtener_valor_diametro()
            r= (diametro/1000)/2
            
            C = (0.0556/(np.log(GMD/r)))
            
        
            
            print("C es: {:.4f} uF/km".format(C))
            
            etiqueta_R.config(text=f"R = {R:.6f} Ohm/km")
            
            # Después de calcular L
            etiqueta_L.config(text=f"L = {L:.6f} mH/km")

            # Después de calcular C
            etiqueta_C.config(text=f"C = {C:.6f} nF/km")
        elif num_conductores == 2:
            
           
            print("Número de conductores por fase: 2")
            
            Rac_tabla=obtener_valor_Rac()
            R=Rac_tabla/4
            print("Rac es: {:.4f} Ohm/km".format(R))
            
            GMR_L= np.sqrt(GMR*d)
            print ("El valor del GMRL es: ", GMR_L)
            
            GMRL_A=(GMR_L*da1a2)**(1/2)
            print ("El valor del GMRL A es: ", GMRL_A)
            
            GMRL_B=(GMR_L*db1b2)**(1/2)
            print ("El valor del GMRL A es: ", GMRL_B)
            
            GMRL_C=(GMR_L*dc1c2)**(1/2)
            print ("El valor del GMRL A es: ", GMRL_C)
            
            GMR_L_TOTAL= (GMRL_A*GMRL_B*GMRL_C)**(1/3)
            
            
            print ("El valor del GMRL es: ", GMR_L_TOTAL)
            
            L = 0.2 * np.log(GMD/GMR_L_TOTAL)
            
            print("L es: {:.4f} mH/km".format(L))
            
            ##################
            #CALCULO DE C
            ##################
            
            diametro = obtener_valor_diametro()    ## dato en mm
            r= (diametro/1000)/2
            
            print("Número de conductores por fase: 2")
            GMR_C= np.sqrt(r*d)
            print ("El valor del GMRC es: ", GMR_C)
            
            GMRC_A=(GMR_C*da1a2)**(1/2)
            print ("GMR C A: ", GMRC_A)
            
            GMRC_B=(GMR_C*db1b2)**(1/2)
            print ("GMR C B: ", GMRC_B)
            
            GMRC_C=(GMR_C*dc1c2)**(1/2)
            print ("GMR C C: ", GMRC_C)
            
            GMR_C_TOTAL= (GMRC_A*GMRC_B*GMRC_C)**(1/3)
            
            
            print ("GMR C TOTAL: ", GMR_C_TOTAL)
            
            C= (0.0556/(np.log(GMD/GMR_C_TOTAL)))
            
            print("C es: {:.4f} uF/km".format(C))
            
            #en esta parte quiero imprimir en la pantalla de tinker debajo de la matriz el valor de L 
           
            etiqueta_R.config(text=f"R = {R:.6f} Ohm/km") 
           
           # Después de calcular L
            etiqueta_L.config(text=f"L = {L:.6f} mH/km")

            # Después de calcular C
            etiqueta_C.config(text=f"C = {C:.6f} nF/km")
            
            
        elif num_conductores == 3:
            
            print("Número de conductores por fase: 3")
            
            Rac_tabla=obtener_valor_Rac()
            R=Rac_tabla/6
            print("Rac es: {:.4f} Ohm/km".format(R))
          
      
            GMR_L= (GMR * d**2)**(1/3)
            print ("El valor del GMRL es: ", GMR_L)
            
            GMRL_A=(GMR_L*da1a2)**(1/2)
            print ("El valor del GMRL A es: ", GMRL_A)
            
            GMRL_B=(GMR_L*db1b2)**(1/2)
            print ("El valor del GMRL A es: ", GMRL_B)
            
            GMRL_C=(GMR_L*dc1c2)**(1/2)
            print ("El valor del GMRL A es: ", GMRL_C)
            
            GMR_L_TOTAL= (GMRL_A*GMRL_B*GMRL_C)**(1/3)
            
            
            print ("El valor del GMRL es: ", GMR_L_TOTAL)
            
            L = 0.2 * np.log(GMD/GMR_L_TOTAL)
            
            print("L es: {:.4f} mH/km".format(L))
   
            ##################
            #CALCULO DE C
            ##################
            
            diametro = obtener_valor_diametro()    ## dato en mm
            r= (diametro/1000)/2                   ## en metros
            
            print("Número de conductores por fase: 2")
            GMR_C= (r * d**2)**(1/3)
            print ("El valor del GMRC es: ", GMR_C)
            
            GMRC_A=(GMR_C*da1a2)**(1/2)
            print ("GMR C A: ", GMRC_A)
            
            GMRC_B=(GMR_C*db1b2)**(1/2)
            print ("GMR C B: ", GMRC_B)
            
            GMRC_C=(GMR_C*dc1c2)**(1/2)
            print ("GMR C C: ", GMRC_C)
            
            GMR_C_TOTAL= (GMRC_A*GMRC_B*GMRC_C)**(1/3)
            
            
            print ("GMR C TOTAL: ", GMR_C_TOTAL)
            
            C= (0.0556/(np.log(GMD/GMR_C_TOTAL)))
            
            print("C es: {:.4f} uF/km".format(C))
            
            
            etiqueta_R.config(text=f"R = {R:.6f} Ohm/km")
            
            # Después de calcular L
            etiqueta_L.config(text=f"L = {L:.6f} mH/km")

            # Después de calcular C
            etiqueta_C.config(text=f"C = {C:.6f} nF/km")

            #en esta parte quiero imprimir en la ventana de tinker los valores de L y C, en la posicón row 3 y columna 3 
            
        
            
        elif num_conductores == 4:
            
            
            print("Número de conductores por fase: 4")
            
            Rac_tabla=obtener_valor_Rac()
            R=Rac_tabla/8
            print("Rac es: {:.4f} Ohm/km".format(R))
            
            GMR_L= 1.09*(GMR * d**3)**(1/4)
            print ("El valor del GMRL es: ", GMR_L)
            
            GMRL_A=(GMR_L*da1a2)**(1/2)
            print ("El valor del GMRL A es: ", GMRL_A)
            
            GMRL_B=(GMR_L*db1b2)**(1/2)
            print ("El valor del GMRL A es: ", GMRL_B)
            
            GMRL_C=(GMR_L*dc1c2)**(1/2)
            print ("El valor del GMRL A es: ", GMRL_C)
            
            GMR_L_TOTAL= (GMRL_A*GMRL_B*GMRL_C)**(1/3)
            
            
            print ("El valor del GMRL es: ", GMR_L_TOTAL)
            
            L = 0.2 * np.log(GMD/GMR_L_TOTAL)
            
            print("L es: {:.4f} mH/km".format(L))
            
            ##################
            #CALCULO DE C
            ##################
            
            diametro = obtener_valor_diametro()    ## dato en mm
            r= (diametro/1000)/2
            
            print("Número de conductores por fase: 4")
            GMR_C= 1.09*(r * d**3)**(1/4)
            print ("El valor del GMRC es: ", GMR_C)
            
            GMRC_A=(GMR_C*da1a2)**(1/2)
            print ("GMR C A: ", GMRC_A)
            
            GMRC_B=(GMR_C*db1b2)**(1/2)
            print ("GMR C B: ", GMRC_B)
            
            GMRC_C=(GMR_C*dc1c2)**(1/2)
            print ("GMR C C: ", GMRC_C)
            
            GMR_C_TOTAL= (GMRC_A*GMRC_B*GMRC_C)**(1/3)
            
            
            print ("GMR C TOTAL: ", GMR_C_TOTAL)
            
            C= (0.0556/(np.log(GMD/GMR_C_TOTAL)))
            
            print("C es: {:.4f} uF/km".format(C))
        
        
            
            etiqueta_R.config(text=f"R = {R:.6f} Ohm/km")
            
            # Después de calcular L
            etiqueta_L.config(text=f"L = {L:.6f} mH/km")

            # Después de calcular C
            etiqueta_C.config(text=f"C = {C:.6f} nF/km")
            

    fig.clear()
    ax = fig.add_subplot(111)
    ax.scatter(x_values, y_values, s=100, c="blue")
    ax.set_title("Disposición de los circuitos", fontsize=16, color="black", fontweight="bold", loc="center")
    ax.set_xlabel("x (m)",fontsize=12, color="black", fontweight="bold", labelpad=5)
    ax.set_ylabel("y (m)",fontsize=12, color="black", fontweight="bold", labelpad=5)
    canvas.draw()
    
    return R,L,C







def confirmar_longitud():
    # Obtener el valor de longitud desde el campo de entrada
    longitud_valor = float(tipo_longitud.get())
        
    # Determinar la categoría de la longitud
    if longitud_valor < 80:
        resultado_label.config(text='Modelo de Línea corta')
        desplegable_largo.grid_forget()
    elif 80 <= longitud_valor <= 250:
        resultado_label.config(text='Modelo de Línea media')
        desplegable_largo.grid_forget()
    else:
        resultado_label.config(text='Modelo de Línea larga')
        # Mostrar el OptionMenu para la selección de pérdidas
        desplegable_largo.grid(row=10, column=1, padx=10, pady=1)  # Mostrar el OptionMenu solo si la línea es larga


def obtener_datosSR():
    
    r,l,c = generar_grafica()
    
    longitud_valor = float(tipo_longitud.get())
    
    a = actualizar_valor() # 0 es con perdidas o 1 sin perdidas

   # tipo_dato = datosSR.get()
    frecuencia_valor = float(frecuencia_var.get())
   # potencia_valor = float(potencia.get())
    #potencia_q_valor = float(potencia_q.get())
    voltaje_operacion_valor = float(voltaje_operacion.get())
    
    
    w = 2*np.pi*frecuencia_valor
    R = r*longitud_valor
    xL = complex(0,w*l*10**-3*longitud_valor)
    xC = complex(0,-1/(w*c*10**-6))
    
    alfa = R
    Beta = w*(l*(10**(-3))*c*(10**(-6)))**(1/2)
    
    Z = R+xL
    Y = complex(0,w*c*10**-6*longitud_valor)
    
    gm = ((Z*Y)/(longitud_valor)**2)**(1/2)
    
    Zc = (Z/Y)**(1/2)
    
    print('######################################')
    print('gm: ', gm)
    print('Z: ', Z)
    print('Y: ', Y)
    print('Zc: ', Zc)
    print('######################################')
    
    
    if longitud_valor < 80 and voltaje_operacion_valor <= 69:
       A = 1
       B = Z
       C = 0
       D = A
       
    elif 80 <= longitud_valor <= 250:
        A = 1+(Z*Y/2)
        B = Z
        C = Y*(1+(Z*Y)/4)
        D = A
        
    elif longitud_valor > 250:
          
       if a==1: #con perdidas
            A = math.cosh(gm*longitud_valor)
            B = Zc*math.sinh(gm*longitud_valor)  ### f
            C = (1/Zc)*math.sinh(gm*longitud_valor)
            D = A
            
                        
       elif a==0: #sin perdidas
            A = math.cos(Beta*longitud_valor)
            B = Zc * math.sin(Beta*longitud_valor)
            C = 1 / Zc
            D = A
            
    return A,B,C,D

def calculo_operacion():

    A,B,C,D =  obtener_datosSR()
    
    print('######################################')
    print('A: ', A)
    print('B: ', B)
    print('C: ', C)
    print('D: ', D)
    print('######################################')
    
    datoSR= datosSR.get()   ##datos en envio =1  carga=2
   # Vr= float(voltaje_operacion.get())
    V= float(voltaje_operacion.get()) / (3)**(1/2) 
    
    P = float(potencia_p.get())  # Convierte el valor a float
    Q = float(potencia_q.get())  # Convierte el valor a float
    
    # Calcular el módulo y el ángulo
    S = np.sqrt(P**2 + Q**2)
    angulo_rad = np.arctan2(Q, P)  # arctan2 para obtener el ángulo correcto en radianes
    angulo_S = np.rad2deg(angulo_rad)  # Convertir a grados
    
    I = complex(P,-1*Q) / (3*V)
    
    print('######################################')
    print('V: ', V)
    print('I: ', I)
    print('S: ', S)
    print('P: ', P)
    print('Q: ', Q)
    print('######################################')
    
    if datoSR == "1":    #datos de generación 
        
        print("Usuario ingrego datos en Generación")  
       
        Vs = V
        Is = I
        
        Ps = P
        Qs = Q
        
        Vr = (D*Vs - 1* B*Is)
        Ir = (-1*C*Vs + A*Is)
        
        mod_Vr, angle_Vr = imprimir_modulo_y_angulo(Vr.real, Vr.imag)
        mod_Ir, angle_Ir = imprimir_modulo_y_angulo(Ir.real, Ir.imag)
        
        mod_Vs, angle_Vs=imprimir_modulo_y_angulo(Vs.real, Vs.imag)
        mod_Is, angle_Is=imprimir_modulo_y_angulo(Is.real, Is.imag)
        
        Sr = 3*Vr*np.conj(Ir)
        
        Pr = Sr.real
        Qr = Sr.imag
        
        eficiencia= Pr/P * 100
        
        RV = ((abs(Vs/A))-abs(Vr))/abs(Vr)  *100        
        
    else:                  #datos de carga
        Vr = V
        Ir = I
        Pr = P
        Qr = Q
        #print("Corriente de envio", abs(I),-1*angulo_S)
        #print("Corriente de recibo", Vr)
        #print("Usuario ingrego datos en la carga")        
        #Vs= A*Vr + B*Ir
        
        Vs = A*Vr + B*Ir
        Is = C*Vr + D*Ir
        
        mod_Vr, angle_Vr = imprimir_modulo_y_angulo(Vr.real, Vr.imag)
        mod_Ir, angle_Ir = imprimir_modulo_y_angulo(Ir.real, Ir.imag)
        
        mod_Vs, angle_Vs=imprimir_modulo_y_angulo(Vs.real, Vs.imag)
        mod_Is, angle_Is=imprimir_modulo_y_angulo(Is.real, Is.imag)
        
        Ss = 3*Vs*np.conj(Is)
        Ps = Ss.real
        Qs = Ss.imag
        
        eficiencia= P/Ps * 100
        
        RV = ((abs(Vs/A))-Vr)/ Vr  *100

###############################################################################    
    etiqueta_Vs.config(text=f"Vs = {mod_Vs:.2f} kV")
    etiqueta_Vsangle.config(text=f"Vs angle = {angle_Vs:.2f} °")
    
    etiqueta_Vr.config(text=f"Vr = {mod_Vr:.2f} kV")
    etiqueta_Vrangle.config(text=f"Vr angle = {angle_Vr:.2f} °")
        
    etiqueta_Is.config(text=f"Is = {mod_Is:.2f} KA")
    etiqueta_Isangle.config(text=f"Is angle = {angle_Is:.2f} °")
            
    
    etiqueta_Ir.config(text=f"Ir = {mod_Ir:.2f} KA")
    etiqueta_Irangle.config(text=f"Ir angle = {angle_Ir:.2f} °")
    
    etiqueta_Ps.config(text=f"Ps = {Ps:.2f} MW")
    etiqueta_Pr.config(text=f"Pr = {Pr:.2f} MW")
    
    etiqueta_Qs.config(text=f"Qs = {Qs:.2f} MVAR")
    etiqueta_Qr.config(text=f"Qr = {Qr:.2f} MVAR")
    
    etiqueta_eficiencia.config(text=f"η = {eficiencia:.2f} [%]")
    etiqueta_RV.config(text=f"RV = {RV:.2f} [%]")
    
    print('######################################')
    print('Vs: ', Vs)
    print('Vr: ', Vr)
    print('Is: ', Is)
    print('Ir: ', Ir)
    print('Ps: ', Ps)
    print('Pr: ', Pr)
    print('Qs: ', Qs)
    print('Qr: ', Qr)
    print('######################################')
    
#%%
ventana = tk.Tk()
ventana.title("Modelación y Operación de Líneas de Transmisión en Estado Estacionario")
ventana.geometry("1020x820+250+50")
ventana.resizable(width=False, height=False)

# Etiquetas
etiqueta = tk.Label(ventana, text="Tipo de conductor: ")
etiqueta.grid(row=0, column=0, padx=10, pady=2, sticky="w")

etiqueta2 = tk.Label(ventana, text="Código: ")
etiqueta2.grid(row=1, column=0, padx=10, pady=2, sticky="w")

etiqueta3 = tk.Label(ventana, text="Número de circuitos: ")
etiqueta3.grid(row=2, column=0, padx=10, pady=2, sticky="w")

etiqueta4 = tk.Label(ventana, text="Número de conductores por fase: ")
etiqueta4.grid(row=3, column=0, padx=10, pady=2, sticky="w")

distancia_label = tk.Label(ventana, text="Distancia entre conductores (m): ")
distancia_label.grid(row=4, column=0, padx=10, pady=2, sticky="w")

###############################################################################
# Crear un Frame llamado frame_resultados como contenedor para las etiquetas
frame_resultados = tk.Frame(ventana)
frame_resultados.grid(row=5, column=3, padx=0, pady=0, sticky="nws")

# Crear la etiqueta "Resultados" y añadirla al Frame
etiqueta_resultados = tk.Label(frame_resultados, text="Resultados", font=("Arial", 10, "bold"))
etiqueta_resultados.pack(anchor="n", pady=(10, 5),padx=200)

# Crear la etiqueta "R = " y añadirla al Frame
etiqueta_R = tk.Label(frame_resultados, text="R = ")
etiqueta_R.pack(anchor="center")

# Crear la etiqueta "L = " y añadirla al Frame
etiqueta_L = tk.Label(frame_resultados, text="L = ")
etiqueta_L.pack(anchor="center")

# Crear la etiqueta "C = " y añadirla al Frame
etiqueta_C = tk.Label(frame_resultados, text="C = ")
etiqueta_C.pack(anchor="center")

###############################################################################


# Crear el frame para los resultados
frame_resultados_2 = tk.Frame(ventana)
frame_resultados_2.grid(row=15, column=3, padx=10, pady=10)  # Cambiar a fila 11 para evitar conflicto

# Columna 1: Valores de envío (Vs, Is, Ps, Qs)
etiqueta_Vs = tk.Label(frame_resultados_2, text="Vs= ")
etiqueta_Vs.grid(row=12, column=3, padx=5, pady=2)

etiqueta_Vsangle = tk.Label(frame_resultados_2, text="Vr= ")
etiqueta_Vsangle.grid(row=12, column=4, padx=5, pady=2)

etiqueta_Is = tk.Label(frame_resultados_2, text="Is= ")
etiqueta_Is.grid(row=13, column=3, padx=5, pady=2)

etiqueta_Isangle = tk.Label(frame_resultados_2, text="Is= ")
etiqueta_Isangle.grid(row=13, column=4, padx=5, pady=2)


etiqueta_Ps = tk.Label(frame_resultados_2, text="Ps= ")
etiqueta_Ps.grid(row=14, column=3, padx=5, pady=2)

etiqueta_Qs = tk.Label(frame_resultados_2, text="Qs= ")
etiqueta_Qs.grid(row=15, column=3, padx=5, pady=2)


# Columna 2: Valores de recibo (Vr, Ir, Pr, Qr)
etiqueta_Vr = tk.Label(frame_resultados_2, text="Vr= ")
etiqueta_Vr.grid(row=12, column=5, padx=5, pady=2)

etiqueta_Vrangle = tk.Label(frame_resultados_2, text="Vr= ")
etiqueta_Vrangle.grid(row=12, column=6, padx=5, pady=2)


etiqueta_Ir = tk.Label(frame_resultados_2, text="Ir= ")
etiqueta_Ir.grid(row=13, column=5, padx=5, pady=2)

etiqueta_Irangle = tk.Label(frame_resultados_2, text="Ir= ")
etiqueta_Irangle.grid(row=13, column=6, padx=5, pady=2)


etiqueta_Pr = tk.Label(frame_resultados_2, text="Pr= ")
etiqueta_Pr.grid(row=14, column=5, padx=5, pady=2)

etiqueta_Qr = tk.Label(frame_resultados_2, text="Qr= ")
etiqueta_Qr.grid(row=15, column=5, padx=5, pady=2)


etiqueta_eficiencia = tk.Label(frame_resultados_2, text="η= ")
etiqueta_eficiencia.grid(row=16, column=4, padx=5, pady=2)

etiqueta_RV = tk.Label(frame_resultados_2, text="RV= ")
etiqueta_RV.grid(row=16, column=5, padx=5, pady=2)

etiquetaENVIO = tk.Label(frame_resultados_2, text="Datos de envio")
etiquetaENVIO.grid(row=7, column=3, padx=10, pady=2, sticky="w")
etiquetaA = tk.Label(frame_resultados_2, text="______________")
etiquetaA.grid(row=7, column=4, padx=10, pady=2, sticky="w")

etiquetaRECIBO = tk.Label(frame_resultados_2, text="Datos de recibo")
etiquetaRECIBO.grid(row=7, column=5, padx=10, pady=2, sticky="w")
etiquetaA = tk.Label(frame_resultados_2, text="______________")
etiquetaA.grid(row=7, column=6, padx=10, pady=2, sticky="w")

################333

etiqueta5 = tk.Label(ventana, text="Frecuencia: [Hz]")
etiqueta5.grid(row=8, column=0, padx=10, pady=2, sticky="w")


etiqueta7 = tk.Label(ventana, text="Potencia: [MVA]")
etiqueta7.grid(row=14, column=0, padx=10, pady=2, sticky="w")

etiqueta9 = tk.Label(ventana, text="Voltaje de operación: [KV]")
etiqueta9.grid(row=15, column=0, padx=10, pady=2, sticky="w")

etiqueta14 = tk.Label(ventana, text="Longitud de la linea: [Km]")
etiqueta14.grid(row=9, column=0, padx=10, pady=2, sticky="w")


etiquetaDATOS = tk.Label(ventana, text="Lugar de datos:")
etiquetaDATOS.grid(row=7, column=0, padx=10, pady=2, sticky="w")
#%%
# Variable para almacenar el tipo de conductor seleccionado
conductor_seleccionado = tk.StringVar()
conductor_seleccionado.set("Seleccione un conductor")
conductor_seleccionado.trace('w', actualizar_desplegable)

# Crear el menú desplegable con los tipos de conductor
conductores = ["ACSR", "ACAR", "AAAC"]
desplegable1 = tk.OptionMenu(ventana, conductor_seleccionado, *conductores)
desplegable1.grid(row=0, column=1, padx=10, pady=2, sticky="w")

# Variable para el segundo menú desplegable
conductor_seleccionado2 = tk.StringVar()
conductor_seleccionado2.set("Seleccione un conductor específico")

# Crear el segundo menú desplegable vacío
menu_desplegable2 = tk.OptionMenu(ventana, conductor_seleccionado2, "")
menu_desplegable2.grid(row=1, column=1, columnspan=2, padx=10, pady=2, sticky="w")

# Variables para los radio buttons
circuitos_var = tk.StringVar()
circuitos_var.set("1")
circuitos_var.trace('w', lambda *args: actualizar_matriz())

# Crear los radio buttons para seleccionar el número de circuitos
radio_un_circuito = tk.Radiobutton(ventana, text="Un circuito", variable=circuitos_var, value="1")
radio_un_circuito.grid(row=2, column=1, padx=10, pady=2, sticky="w")

radio_dos_circuitos = tk.Radiobutton(ventana, text="Dos circuitos", variable=circuitos_var, value="2")
radio_dos_circuitos.grid(row=2, column=2, padx=10, pady=2, sticky="w")

# Crear campo de entrada para la distancia entre conductores
distancia_entry = tk.Entry(ventana)
distancia_entry.grid(row=4, column=1, padx=10, pady=2)


# Lista de opciones para el OptionMenu
numConductores = ["1", "2", "3", "4"]
# Crear OptionMenu
num = tk.StringVar()
num.set("1")  # Configurar un valor válido inicial
num.trace('w', lambda *args: actualizar_campo_distancia())
desplegable3 = tk.OptionMenu(ventana, num, *numConductores)
desplegable3.grid(row=3, column=1, padx=5, pady=2, sticky="w")


# Contenedor para la matriz
contenedor_matriz = tk.Frame(ventana)
contenedor_matriz.grid(row=5, column=0, columnspan=3, padx=1, pady=1)

# Botón para generar la gráfica
boton_grafica = tk.Button(ventana, text="Calcular Parametros", command=generar_grafica, font=("Helvetica", 8), width=20, height=1)
boton_grafica.grid(row=6, column=1, padx=10, pady=3)

# Contenedor para la gráfica
fig = Figure(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().grid(row=0, column=3, padx=5, pady=2, rowspan=4, sticky="nsew")


# boton de seleccion si es de envio o recibo los datos
datosSR = tk.StringVar()
datosSR.set("1")

datos_envio = tk.Radiobutton(ventana, text="Datos de envío", variable=datosSR, value="1")
datos_envio.grid(row=7, column=1, padx=10, pady=2, sticky="w")

datos_recibo = tk.Radiobutton(ventana, text="Datos de recibo", variable=datosSR, value="2")
datos_recibo.grid(row=7, column=2, padx=10, pady=2, sticky="w")


nfrecuencia = ["50", "60"]

frecuencia_var = tk.StringVar()
frecuencia_var.set(nfrecuencia[1])

desplegable_frecuencia = tk.OptionMenu(ventana, frecuencia_var, *nfrecuencia)
desplegable_frecuencia.grid(row=8, column=1, padx=10, pady=1)


# Crear un Frame como contenedor
frame_potencia = tk.Frame(ventana)
frame_potencia.grid(row=14, column=1, padx=10, pady=1)
# Crear la primera entrada dentro del Frame
potencia_p = tk.Entry(frame_potencia, width=10)  # Ajusta el ancho aquí
potencia_p.pack(side="left")
# Crear una etiqueta con ", j" dentro del Frame
coma_j = tk.Label(frame_potencia, text=" , j")
coma_j.pack(side="left")
# Crear la segunda entrada dentro del Frame
potencia_q = tk.Entry(frame_potencia, width=10)  # Ajusta el ancho aquí
potencia_q.pack(side="left")
espacio = tk.Label(frame_potencia, text=" ")
espacio.pack(side="left")



#########################################
voltaje_operacion = tk.Entry(ventana)
voltaje_operacion.grid(row=15, column=1, padx=10, pady=1)

# Crear un Frame como contenedor
frame_voltaje = tk.Frame(ventana)
frame_voltaje.grid(row=15, column=3, padx=10, pady=1)
# Crear la primera entrada dentro del Frame


##########################################3
# Crear un Frame como contenedor para tipo_longitud, boton_confirmar y el OptionMenu
frame_longitud = tk.Frame(ventana)
frame_longitud.grid(row=9, column=1, columnspan=2, padx=10, pady=1, sticky="w")

# Crear el Entry tipo_longitud y añadirlo al Frame
tipo_longitud = tk.Entry(frame_longitud)
tipo_longitud.pack(side="left", padx=(26, 10))

# Crear el botón Confirmar y añadirlo al Frame
boton_confirmar = tk.Button(frame_longitud, text="Confirmar", command=confirmar_longitud)
boton_confirmar.pack(side="left", padx=(0, 10))

# Crear una etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.grid(row=9, column=3, padx=1, pady=2)

##########################################3

# Crear un OptionMenu para la selección de pérdidas
tipo_long_largo = ["Con pérdidas", "Sin pérdidas"]
largo_tipo = tk.StringVar()
largo_tipo.set(tipo_long_largo[1])  # Establecer valor inicial
largo_tipo.trace("w", actualizar_valor)  # Llamar a actualizar_valor cuando cambie

desplegable_largo = tk.OptionMenu(ventana, largo_tipo, *tipo_long_largo)
desplegable_largo.grid(row=9, column=1, padx=1, pady=1)
desplegable_largo.grid_forget()  # Ocultar el OptionMenu inicialmente


boton_confirmar = tk.Button(ventana, text="Calcular operación", command=calculo_operacion)
boton_confirmar.grid(row=16, column=1, padx=10, pady=10)


# Inicializar la matriz
actualizar_matriz()

ventana.mainloop()