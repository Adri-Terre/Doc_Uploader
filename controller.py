import vista
import os
import shutil       

from tkinter.messagebox import *
from tkinter import filedialog



def ruta():
    folder_selected = filedialog.askdirectory()
    return folder_selected

def file():
    import module_variable as mod_var
    file_selected = filedialog.askopenfilename()
    fichero = open(file_selected,'r')
    mod_var.file_origen = file_selected
    return file_selected

def upload():
    from module_variable import file_origen, ruta_destino,aeropuertos
    from module_variable import fecha_seteada
    import os

   
    aep_seleccionado= vista.combo_aep.get()
    sistema_seleccionado = vista.combo_sistema.get()
    folio_seleccionado = vista.combo_folio.get()
    #extension_seleccionada = vista.combo_extension.get() 
    
    
    a= file_origen.rindex("/")
    
    ruta_origen = file_origen[:(a+1)]
    #nombre_origen = file_origen[(a+1):]
    b = file_origen.rindex(".")
    extension_archivo = file_origen[(b):] 
    #print(extension_archivo)
    ##shutil.copy(file_origen,"C:\Users\aterreni\Documents\GitHub\prueba.pdf")
    
    nombre_nuevo = str(fecha_seteada + " " + aep_seleccionado + " " + folio_seleccionado + " " + vista.folio_input.get() + extension_archivo)
    

    archivo_renombrado = os.path.join (ruta_origen,nombre_nuevo)#ruta_origen + nombre_nuevo

    os.rename(file_origen, archivo_renombrado)
    
    print ("Se reemplaza el archivo: " + str(file_origen) + "por: "+str(archivo_renombrado))

    c= fecha_seteada.index(".")
    año_seteado = fecha_seteada[:(c)] 
    ruta_destino = ruta_destino + "/" + aep_seleccionado + "/" + año_seteado + "/" + sistema_seleccionado + "/" + nombre_nuevo
    
    #nuevo_dest = os.path.join (ruta_destino, nombre_nuevo)#ruta_destino + nombre_nuevo
    
    #w9 = vista.Label(vista.master, text= nombre_nuevo, foreground="green")
    #w9.place(x=10, y=270)

    shutil.move(nombre_nuevo,ruta_destino)
    
    w9 = vista.Label(vista.master, text= ruta_destino, foreground="green")
    w9.place(x=10, y=275)
    vista.contador_archivos_cargados = vista.contador_archivos_cargados + 1
    text = str (vista.contador_archivos_cargados)
    vista.w2.destroy()
    w2 = vista.Label(vista.master, text= text, foreground="black")
    w2.place(x=820, y=250)

    

