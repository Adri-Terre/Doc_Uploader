""" este modulo se emplea para emplear variables globales """

regex_numero = "[0-9]"
image_64_encode = ""
var1 = False
var2 = False
fecha_seteada = ""
file_origen = ""
ruta_destino = ""
contador_archivos_cargados = 0

aeropuertos = (
    "AEP",
    "BAR",
    "BCA",
    "CAT",
    "CBA",
    "CHP",
    "CRR",
    "CRV",
    "DIL",
    "DOZ",
    "DRY",
    "ECA",
    "ERE",
    "ESQ",
    "EZE RWY 11 29",  # 2-1-23
    "EZE RWY 17 35",  # 2-1-23
    "EZE VOR",  # 2-1-23
    "FDO",
    "FSA",
    "GAL",
    "GBE",
    "GNR",
    "GPI",
    "GRA",
    "GUA",
    "IGU",
    "JUA",
    "JUJ",
    "LAR",
    "LYE",
    "MDP",
    "MJZ",
    "MLG",
    "NEU",
    "NIN",
    "OEL",
    "OSA",
    "PAL",
    "PAR",
    "POS",
    "PTA",
    "ROS",
    "RTA",
    "RYD",
    "SAL",
    "SDE",
    "SIS",
    "SJU",
    "SNT",
    "SRA",
    "SVO",
    "TRC",
    "TRE",
    "TRH",
    "TUC",
    "UIS",
    "USH",
    "VIE",
)

sistema = ("ILS","VOR","LI")

folio = ("ILS LH", "ILS PARAMETROS", "DME ILS PARAMETROS", "VOR LH","DME VOR PARAMETROS","VOR PARAMETROS I","VOR PARAMETROS II", "LI LH", "LI PARAMETROS")

extension = (".pdf",".jpg",".jfif",".csv",".xlsx",".doc")