from tkinter import *
from tkinter.messagebox import *
import PIL
from PIL import Image, ImageTk
import module_variable as mod_var
import controller
from tkinter import ttk  
from getpass import getuser

contador_archivos_cargados = 0
contador_registros_cargados = 0

def autor():

    """esta funcion crea una pantalla donde se muestra el autor del proyecto"""

    win = Toplevel()
    win.title("Autor")
    win.geometry("300x100")
    label_autor = Label(win, text="ING. TERRENI ADRIAN HORACIO\n\nv1.0 - AÑO: 2023")
    label_autor.place(x=60, y=20)


def ruta_origen():

    """esta funcion, a traves del controller, inserta la documentacion a analizar"""
    ruta = controller.ruta()
    print (ruta)


def ruta_destino():
    global w6
    """esta funcion, a traves del controller, inserta la documentacion a analizar"""
    ruta = controller.ruta()
    print (ruta)
    mod_var.ruta_destino = ruta
    if (w6.winfo_ismapped()) == True:
        w6.destroy()
    w6 = Label(master, text= ruta, foreground="purple")
    w6.place(x=115, y=80)

def file_origen():
    global w8
    
    """esta funcion, a traves del controller, inserta la documentacion a analizar"""
    file = controller.file()
    print (file)
    
    w8 = Label(master, text= file, foreground="blue")
    w8.place(x=130, y=50)


def upload():
    controller.upload()

def calendario():
    
    from tkcalendar import Calendar, DateEntry
    
    import datetime
    import module_variable as mod_var
    
    def print_sel():
        global w7
        print(cal.selection_get())
        w7 = Label(master, text=cal.selection_get() )
        w7.place(x=30, y=135)
        win_calendario.destroy()
        fecha_seteada = str(cal.selection_get())
        nueva_fecha_seteada = fecha_seteada.replace("-",".")
        mod_var.fecha_seteada = nueva_fecha_seteada

        
    win_calendario = Toplevel()
    today = datetime.date.today()
    dia=today.day
    mes=today.month
    anio=today.year

    mindate = datetime.date(year=2018, month=1, day=21)
    maxdate = today + datetime.timedelta(weeks=520)
    print(mindate, maxdate)
    
 
    cal = Calendar(win_calendario, font="Arial 14",selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="hand1", year=anio, month=mes, day=dia)
    cal.pack(fill="both", expand=True)
    ttk.Button(win_calendario, text="ok", command=print_sel).pack()

# ----------------------------SECCIÓN GRÁFICA DE LA APP------------------------

master = Tk()

fecha = LabelFrame(master, text="Fecha del folio", bd=2)
fecha.place(x=10, y=110, width=165, height=60)

""" Aquí se crea la pantalla principal """

master.geometry("870x410")
master.title("DOC Uploader")
menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)

# ---------Acerca de-----------------------
acerca_de = Menu(menu)
menu.add_cascade(label="Acerca de", menu=acerca_de)
acerca_de.add_command(label="Autor", command=autor)


# --------------BOTON-----------------------------------------------------------------
Button(
    master,
    text="Repositorio Destino",
    width=22,
    command=ruta_destino,
    anchor=CENTER,
).place(x=580, y=15)


load = Image.open("icon_calen.png")
miniatura_calen = (120, 30)
load.thumbnail(miniatura_calen)
load.save("img_miniatura_calen.png")
load = Image.open("img_miniatura_calen.png")
image_calen = ImageTk.PhotoImage(load)

Button(master, image=image_calen,width=52, command=calendario, anchor=CENTER).place(
    x=200, y=120
)

Button(master, text="Upload", width=10, command=upload, anchor=CENTER).place(
    x=770, y=200
)

Button(master, text="Repositorio Origen", width=22, command=file_origen, anchor=CENTER).place(
    x=10, y=15
)

# -------------------------------------------------------------------------------
aep_frame = LabelFrame(master, text="Aeropuerto", bd=2)
aep_frame.place(x=10, y=180, width=180, height=60)

list_aep = mod_var.aeropuertos
combo_aep = ttk.Combobox(
    state="readonly", values=list_aep
)
combo_aep.place(x=30, y=200)

# -------------------------------------------------------------------------------

sistema_frame = LabelFrame(master, text="Sistema", bd=2)
sistema_frame.place(x=200, y=180, width=180, height=60)

list_sist = mod_var.sistema
combo_sistema = ttk.Combobox(
    state="readonly", values=list_sist
)
combo_sistema.place(x=220, y=200)

# -------------------------------------------------------------------------------

folio_frame = LabelFrame(master, text="Folio", bd=2)
folio_frame.place(x=390, y=180, width=180, height=60)

list_folio = mod_var.folio
combo_folio = ttk.Combobox(
    state="readonly", values=list_folio
)
combo_folio.place(x=410, y=200)

# -------------------------------------------------------------------------------

nro_frame = LabelFrame(master, text="Nro. folio", bd=2)
nro_frame.place(x=580, y=180, width=80, height=60)

# -------------------------------------------------------------------------------
folio_input = Entry(master)
folio_input.configure(width=8)
folio_input.place(x=593, y=200)
folio_input.focus_set()

w1 = Label(master, text="Archivos Cargados: ", foreground="black")
w1.place(x=693, y=310)

w2 = Label(master, text="-", foreground="red")
w2.place(x=820, y=310)

w3 = Label(master, text="Ultimo archivo cargado: ", foreground="black")
w3.place(x=10, y=310)

w9 = Label(master, text= "-", foreground="red")
w9.place(x=180, y=310)

w10 = Label(master, text="Archivo seleccionado: ", foreground="black")
w10.place(x=3, y=50)

w11 = Label(master, text="Repositorio destino: ", foreground="black")
w11.place(x=3, y=80)

w12 = Label(master, text="Ultimo registro cargado: ", foreground="black")
w12.place(x=10, y=360)

w13 = Label(master, text= "-", foreground="red")
w13.place(x=180, y=360)

w14 = Label(master, text="Registros cargados: ", foreground="black")
w14.place(x=693, y=360)

w15 = Label(master, text="-", foreground="red")
w15.place(x=820, y=360)

w16 = Label(master, text="Fallas", foreground="black")
w16.place(x=695, y=205)

load = Image.open("logo.png")
miniatura = (160, 120)
load.thumbnail(miniatura)
load.save("img_miniatura.png")
load = Image.open("img_miniatura.png")
mod_var.render = ImageTk.PhotoImage(load)
w5 = Label(master, image=mod_var.render)
w5.place(x=300, y=20)

usuario = getuser()
usuario = usuario.lower()
print(usuario)

mod_var.ruta_destino= "C"+ ":" + "/" + "Users/" + usuario + "/" + "OneDrive - EANA S.E/Historiales y Libros Parámetros" 
mod_var.ruta_destino_excel= "C"+ ":" + "/" + "Users/" + usuario + "/" + "OneDrive - EANA S.E\Reportes e Informes Técnicos\DNAV Checklist 1"
w6 = Label(master, text= mod_var.ruta_destino, foreground="purple")
w6.place(x=115, y=80)

mod_var.checkbox = BooleanVar()
mod_var.checkbox_falla = BooleanVar()

anexo_frame = LabelFrame(master, text="Anexo VIII", bd=2)
anexo_frame.place(x=10, y=250, width=180, height=60)

list_anexo = mod_var.region
combo_anexo = ttk.Combobox(
    state="readonly", values=list_anexo,width=18
)
combo_anexo.place(x=40, y=270)

Checkbutton(
    master,
    onvalue=1,
    offvalue=0,
    variable=mod_var.checkbox,
    ).place(x=12, y=270)

Checkbutton(
    master,
    onvalue=1,
    offvalue=0,
    variable=mod_var.checkbox_falla,
    ).place(x=670, y=200)

master.mainloop()
