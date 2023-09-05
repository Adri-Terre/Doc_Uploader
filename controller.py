import vista
import os
import shutil       

from tkinter.messagebox import *
from tkinter import filedialog
from tkinter import *
from tkcalendar import Calendar



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
    from module_variable import regex_numero,fecha_seteada
    import os, re, errno
    import module_variable as mod_var
    from tkinter import ttk 

    aep_seleccionado= vista.combo_aep.get()
    sistema_seleccionado = vista.combo_sistema.get()
    folio_seleccionado = vista.combo_folio.get()
    re_match = False


    if file_origen != "": 
        a= file_origen.rindex("/")
        ruta_origen = file_origen[:(a+1)]
        b = file_origen.rindex(".")
        extension_archivo = file_origen[(b):] 

    else:
        showinfo(
            "Campo incompleto",
            "Asigne la ruta origen",)
        
    
    if (vista.w9.winfo_ismapped()) == True:
        vista.w9.destroy()


    if re.match(regex_numero, vista.folio_input.get()):
        re_match = True
    

    if (fecha_seteada != "" and aep_seleccionado != "" and folio_seleccionado != "" and vista.folio_input.get() != ""):# or (fecha_seteada != "" and aep_seleccionado != "" and mod_var.var1.get() == True and vista.folio_input.get() != ""):
        if (re_match  == True):          
            
            if (folio_seleccionado== "CHECK LIST I") or (folio_seleccionado== "CHECK LIST II"): 
                nombre_check = str(fecha_seteada + " " + aep_seleccionado + " " + sistema_seleccionado + " " + folio_seleccionado + " " + vista.folio_input.get() + extension_archivo)

                archivo_renombrado = os.path.join (ruta_origen,nombre_check)#ruta_origen + nombre_nuevo
                
            else:
                nombre_nuevo = str(fecha_seteada + " " + aep_seleccionado + " " + sistema_seleccionado + " " + folio_seleccionado + " " + vista.folio_input.get() + extension_archivo)
        

                archivo_renombrado = os.path.join (ruta_origen,nombre_nuevo)#ruta_origen + nombre_nuevo

            c= fecha_seteada.index(".")
            año_seteado = fecha_seteada[:(c)]

           
            if (folio_seleccionado== "CHECK LIST I") or (folio_seleccionado== "CHECK LIST II"):    
                    try:
                        nueva_carpeta = ruta_destino + "/" + aep_seleccionado + "/" + año_seteado + "/" + sistema_seleccionado + "/" + "Check list"
                        os.mkdir(nueva_carpeta)
                        
                    except OSError as e:
                        if e.errno == errno.EEXIST:
                            print ("La carpeta ya existe")
                    
                    ruta_destino2 = ruta_destino + "/" + aep_seleccionado + "/" + año_seteado + "/" + sistema_seleccionado + "/" + "Check list" + "/" + nombre_check
            else:
                    ruta_destino2 = ruta_destino + "/" + aep_seleccionado + "/" + año_seteado + "/" + sistema_seleccionado + "/" + nombre_nuevo
                    
            
            try:
                os.rename(file_origen, archivo_renombrado)
                
                print ("Se reemplaza el archivo: " + str(file_origen) + "por: "+str(archivo_renombrado))

                
                shutil.move(archivo_renombrado,ruta_destino2)           
                    
                w9 = vista.Label(vista.master, text= ruta_destino2, foreground="green")
                w9.place(x=10, y=295)
                vista.contador_archivos_cargados = vista.contador_archivos_cargados + 1
                text = str (vista.contador_archivos_cargados)
                vista.w2.destroy()
                w2 = vista.Label(vista.master, text= text, foreground="black")
                w2.place(x=820, y=270)

                vista.folio_input.delete(0,END)
                vista.w8.destroy()   
                vista.w7.destroy()                   
                vista.combo_aep.set("")
                vista.combo_sistema.set("")
                vista.combo_folio.set("")
                    
            except:
                showinfo("Advertencia", "Cierre el archivo seleccionado")
        else:
            showinfo("Mensaje Período", "El período ingresado deben ser números")
    else:
        showinfo(
            "Campos incompletos",
            "Complete todos los campos",)
    
    

    

