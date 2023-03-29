#from msilib.schema import ComboBox
from tkinter import *
from tkinter.messagebox import *
import PIL
from PIL import Image, ImageTk
import module_variable as mod_var
import controller
from tkinter import ttk  # para la barra de progreso



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
    
    w6 = Label(master, text= ruta, foreground="blue")
    w6.place(x=10, y=50)
    #carpeta = folder_selected + "/" + carpeta_sitio + "/" + anio_seleccionado

def call_exportar_1():

    """esta funcion, a traves del controller, exporta los datos de la agenda en .pdf, .csv"""

    #controller.control_exportar("doc_airport")

def calendario():
    
    from tkcalendar import Calendar, DateEntry
    import datetime
    
    def print_sel():
        print(cal.selection_get())
        w7 = Label(master, text=cal.selection_get() )
        w7.place(x=30, y=105)
        win_calendario.destroy()

        
    win_calendario = Toplevel()
    today = datetime.date.today()
    dia=today.day
    mes=today.month
    anio=today.year

    mindate = datetime.date(year=2018, month=1, day=21)
    maxdate = today + datetime.timedelta(weeks=520)
    print(mindate, maxdate)
    
    cal = Calendar(win_calendario, font="Arial 14", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="hand1", year=anio, month=mes, day=dia)
    cal.pack(fill="both", expand=True)
    ttk.Button(win_calendario, text="ok", command=print_sel).pack()

# ----------------------------SECCIÓN GRÁFICA DE LA APP------------------------

master = Tk()

fecha = LabelFrame(master, text="Fecha del folio", bd=2)
fecha.place(x=10, y=80, width=165, height=60)

""" Aquí se crea la pantalla principal """

master.geometry("770x300")
master.title("DOC Uploader")
menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
# --------Archivo--------------------------
menu.add_cascade(label="Archivo", menu=filemenu)
filemenu.add_command(label="Exportar existentes", command=call_exportar_1)
filemenu.add_separator()


# ---------Acerca de-----------------------
acerca_de = Menu(menu)
menu.add_cascade(label="Acerca de", menu=acerca_de)
acerca_de.add_command(label="Autor", command=autor)


# --------------BOTON-----------------------------------------------------------------
Button(
    master,
    text="Repositorio",
    width=22,
    command=ruta_origen,
    anchor=CENTER,
).place(x=10, y=15)


Button(master, text="Calendario", width=22, command=calendario, anchor=CENTER).place(
    x=220, y=100
)

Button(master, text="Upload", width=10, command=calendario, anchor=CENTER).place(
    x=670, y=180
)

# -------------------------------------------------------------------------------
aep_frame = LabelFrame(master, text="Aeropuerto", bd=2)
aep_frame.place(x=10, y=160, width=180, height=60)

list_aep = mod_var.aeropuertos
combo_fir = ttk.Combobox(
    state="readonly", values=list_aep
)
combo_fir.place(x=30, y=180)

# -------------------------------------------------------------------------------

sistema_frame = LabelFrame(master, text="Sistema", bd=2)
sistema_frame.place(x=200, y=160, width=180, height=60)

list_sist = mod_var.sistema
combo_fir = ttk.Combobox(
    state="readonly", values=list_sist
)
combo_fir.place(x=220, y=180)

# -------------------------------------------------------------------------------

folio_frame = LabelFrame(master, text="Folio", bd=2)
folio_frame.place(x=390, y=160, width=180, height=60)

list_folio = mod_var.folio
combo_fir = ttk.Combobox(
    state="readonly", values=list_folio
)
combo_fir.place(x=410, y=180)

# -------------------------------------------------------------------------------

nro_frame = LabelFrame(master, text="Nro. folio", bd=2)
nro_frame.place(x=580, y=160, width=80, height=60)

folio_input = Entry(master)
folio_input.configure(width=8)
folio_input.place(x=593, y=180)
folio_input.focus_set()

w1 = Label(master, text="Archivos Cargados: ", foreground="black")
w1.place(x=593, y=20)

w2 = Label(master, text="-", foreground="red")
w2.place(x=720, y=20)

w3 = Label(master, text="Ultimo archivo cargado: ", foreground="black")
w3.place(x=10, y=250)

w4 = Label(master, text= "-", foreground="red")
w4.place(x=180, y=250)

load = Image.open("logo.png")
miniatura = (160, 120)
load.thumbnail(miniatura)
load.save("img_miniatura.png")
load = Image.open("img_miniatura.png")
mod_var.render = ImageTk.PhotoImage(load)
w5 = Label(master, image=mod_var.render)
w5.place(x=300, y=20)

master.mainloop()
