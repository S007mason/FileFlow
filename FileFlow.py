
import os
import shutil
import tkinter
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import *
import sys
from PIL import Image, ImageTk
from tkinter import messagebox
def mostrar_acerca_de():
    messagebox.showinfo("Acerca de", "https://github.com/S007mason/FileFlow")

def get_resource_path(relative_path):
    """
    Devuelve la ruta absoluta de un recurso, 
    compatible con PyInstaller (modo congelado) y en modo script.
    """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Creamos la ventana principal, definimos dimensiones, título e ícono usando la ruta absoluta
ventana = tkinter.Tk()
ventana.geometry("500x400")
ventana.title("File Flow")
ventana.iconbitmap(get_resource_path("assets/icono.ico"))

menubar = tk.Menu(ventana)
ayuda_menu = tk.Menu(menubar, tearoff=0)
ayuda_menu.add_command(label="Acerca de", command=mostrar_acerca_de)
menubar.add_cascade(label="Ayuda", menu=ayuda_menu)

ventana.config(menu=menubar)
# ------------------ Función para el modo predeterminado ------------------ #
def fun():
    Carpeta_principal = filedialog.askdirectory()
    archivos = os.listdir(Carpeta_principal)
    rutas_completas = [os.path.join(Carpeta_principal, nombre) for nombre in archivos]
    for x in rutas_completas:
        nombre_archivo, extension = os.path.splitext(x)
        print(extension)
        
        ruta = f'{Carpeta_principal}/{extension}'
        ruta3 = f'{Carpeta_principal}/{extension}/{os.path.basename(x)}'
        
        if not os.path.exists(ruta):
            os.mkdir(ruta)
        # Mueve el archivo a la carpeta creada (si la carpeta ya existe, simplemente mueve)
        shutil.move(x, ruta3)

# ------------------ Función para el modo personalizado ------------------ #
def carp():
    # Se crea una nueva ventana para configurar el modo personalizado
    root = tkinter.Tk()
    root.title("")
    root.geometry('700x500')
    root.iconbitmap(get_resource_path("assets/icono.ico"))
    
    labelLand = tk.Label(root, text="Nombre de la carpeta")
    labelLand.pack()
    
    labelCity = tk.Label(root, text="Extensión")
    labelCity.pack()
    
    landString = tk.StringVar()
    entryLand = tk.Entry(root, width=20, textvariable=landString)
    entryLand.pack()
    
    resultString = tk.StringVar()
    resultLabel = tk.Label(root, textvariable=resultString)
    resultLabel.pack()
    
    # Declaramos la variable global 'datos' donde se irán acumulando las extensiones
    global datos
    datos = []
    
    # Lista de opciones (en este ejemplo se incluye un subconjunto de extensiones)
    options_list  = [
    # Documentos y texto
    ".txt", ".doc", ".docx", ".pdf", ".odt", ".rtf", ".tex", ".wpd", ".csv", ".tsv", ".xls", ".xlsx", ".ppt", ".pptx", 
    ".key", ".numbers", ".pages", ".epub", ".mobi", ".azw3", ".ibooks", ".pub", ".abw", ".sdw", ".uot", ".gnumeric", 
    ".gdoc", ".gslides", ".gsheet", ".gdraw", ".gform", ".json", ".xml", ".yaml", ".yml", ".md", ".mdown", ".markdown", 
    ".rst", ".log", ".tex", ".bib", ".chm", ".hlp", ".man", ".info", ".toc", ".adoc", ".asciidoc", ".apt", ".csv", 
    ".tsv", ".log", ".cfg", ".ini", ".plist", ".dot", ".dotx", ".ott", ".uof", ".uop", ".wp", ".stw", ".sxw", ".gnumeric", 
    ".fodt", ".odf", ".fods", ".et", ".dps", ".csl", ".xla", ".xlam", ".xlr", ".xll", ".wks", ".prn", ".dif", ".sylk",

    # Archivos de imagen
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".psd", ".ai", ".eps", ".raw", ".cr2", ".nef", ".arw", 
    ".dng", ".orf", ".heic", ".ico", ".jfif", ".indd", ".webp", ".exr", ".dds", ".psb", ".pct", ".ppm", ".pgm", 
    ".pbm", ".pnm", ".xpm", ".xbm", ".tga", ".dxf", ".ai", ".skp", ".3dm", ".emf", ".wmf", ".jpe", ".rle", ".cur", 
    ".cut", ".pic", ".sid", ".pcx", ".icns", ".xwd", ".pat", ".sct", ".yuv", ".rle", ".vnd", ".r3d", ".sgi", ".rgb", 
    ".rgba", ".bw", ".ras", ".map", ".miff", ".hdri", ".ptx", ".ptm", ".sif", ".sgi", ".bif", ".art", ".big", ".blp", 
    ".bzp", ".b3d", ".cpt", ".ctf", ".cut", ".dib", ".dcm", ".dic", ".dpx", ".e00", ".exv", ".fits", ".ftc", ".ftu", 
    ".g3", ".hdp", ".img", ".jb2", ".jbf", ".jng", ".jp2", ".jpf", ".j2k", ".jpx", ".mng", ".msk", ".nrrd", ".ora", 
    ".pam", ".pdn", ".pixar", ".qfx", ".sct", ".t2b", ".wdp", ".x3f", ".ycbcr", ".cpt", ".dsf", ".fpx", ".iff", ".luc", 
    ".nrg", ".mic", ".pov", ".rmf", ".rrb", ".wmf", ".x3f", ".xar", ".xhtml", ".ycbcra", ".bpg", ".xmp", ".ccx", ".cnf", 
    ".dc3", ".pgx", ".icm", ".jxr", ".jp3", ".mef", ".pcl", ".pxr", ".rpf", ".uwp", ".webp", ".rle", ".xmp", ".xpm", 
    ".rgb", ".sr2", ".aai", ".dpx", ".hdr", ".jls", ".m2v", ".miff", ".mpl", ".pgx", ".pwp", ".raw", ".wtx",

    # Audio
    ".mp3", ".wav", ".aac", ".ogg", ".flac", ".wma", ".m4a", ".aiff", ".au", ".voc", ".ra", ".mid", ".midi", ".mod", 
    ".xm", ".it", ".s3m", ".opus", ".vqf", ".ape", ".cda", ".ac3", ".dts", ".kar", ".sf2", ".pcm", ".gsm", ".spx", 
    ".wv", ".vqf", ".rso", ".tm8", ".tta", ".vqf", ".rfl", ".rmi", ".ram", ".rex", ".rsn", ".rso", ".sd", ".sfk", 
    ".shn", ".smp", ".snd", ".sndt", ".spf", ".sss", ".sseq", ".sty", ".swa", ".tak", ".tm8", ".tta", ".vgm", ".vox", 
    ".w64", ".wma", ".wow", ".wpk", ".xa", ".xmf", ".xra", ".xt", ".ym", ".2sf", ".acm", ".ast", ".bfd", ".bik", 
    ".ce", ".cm", ".co", ".ds", ".dsf", ".dss", ".dtk", ".ds2", ".f32", ".f64", ".fuz", ".gsf", ".its", ".jmf", ".ko", 
    ".lvp", ".m4b", ".ma1", ".ma2", ".mlp", ".mod", ".mp", ".mpdp", ".mte", ".odx", ".oma", ".pcm", ".psf", ".ptb", 
    ".rol", ".raw", ".rns", ".rv", ".rws", ".sd2", ".sfark", ".sfd", ".sgu", ".sid", ".sidt", ".smpl", ".spk", ".ss",
    
    # Video
    ".mp4", ".avi", ".mkv", ".flv", ".mov", ".wmv", ".mpg", ".mpeg", ".m4v", ".3gp", ".f4v", ".webm", ".ogv", 
    ".vob", ".m2ts", ".mts", ".ts", ".rm", ".rmvb", ".divx", ".srt", ".ssa", ".ass", ".vtt", ".mxf", ".prproj", 
    ".veg", ".aep", ".flv", ".swf", ".vpj", ".camproj", ".imovielibrary", ".amxd", ".mux", ".ivr", ".3g2", ".avi", 
    ".bik", ".fli", ".flc", ".mkv", ".mng", ".moi", ".mpe", ".mpg", ".mpv", ".mxf", ".smv", ".tp", ".trp", ".ts", 
    ".vdat", ".vdo", ".wm", ".wtv", ".xf", ".yuv", ".dv", ".hdmov", ".ifo", ".rpl", ".rss", ".svcd", ".tod", ".xvid", 
    ".aep", ".agif", ".aom", ".arf", ".atf", ".avi", ".avx", ".bcm", ".bdm", ".bsf", ".cmv", ".cyx", ".d2v", ".dav", 
    ".dlt", ".dmb", ".dmo", ".dms", ".dmss", ".dsy", ".evo", ".fcpxml", ".fla", ".fli", ".h263", ".h264", ".hevc", 
    ".ivf", ".jtv", ".kux", ".m3u", ".m3u8", ".mep", ".mlt", ".mov", ".mpd", ".mpo", ".mps", ".mpsub", ".mve", ".mvg", 
    ".mvp", ".nsv", ".nut", ".ogm", ".ogg", ".omf", ".pls", ".px3", ".pyv", ".qtl", ".qtm", ".r3d", ".ram", ".rat", 
    ".rcd", ".rec", ".rmvb", ".roq", ".rpm", ".rv", ".rvi", ".sbg", ".sbv", ".scm", ".sdx", ".smi", ".smil", ".snagproj", 
    ".srt", ".stx", ".svi", ".tfd", ".trm", ".vro", ".webm", ".wmx", ".wtv", ".xesc", ".xtv", ".y4m", ".yuv", ".zeg", 
    ".zfp", ".zmv", ".zw",
    
    # Archivos comprimidos
    ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".dmg", ".tgz", ".tbz2", ".lzma", ".z", ".cab", 
    ".arj", ".lzh", ".ace", ".jar", ".war", ".apk", ".xip", ".xar", ".zoo", ".cpio", ".alz", ".r01", ".r02", ".sit", 
    ".sitx", ".hqx", ".uu", ".uue", ".xxe", ".arc", ".pkg", ".lzx", ".ipa", ".rpm", ".deb", ".tbz", ".lz4", ".ar", 
    ".mar", ".pea", ".tar.gz", ".tar.xz", ".tar.bz2", ".zst", ".dd", ".img", ".ipg", ".lz", ".paf", ".pak", ".ppmd", 
    ".rk", ".rpm", ".s7z", ".sea", ".sen", ".shar", ".sux", ".tgx", ".uqw", ".wax", ".wrk", ".zap", ".xsn", ".z01", 
    ".z02", ".z03", ".z04", ".z05", ".xz", ".gz",
    
    # Bases de datos y backups
    ".sql", ".db", ".sqlite", ".mdb", ".accdb", ".dbf", ".myd", ".myi", ".ibd", ".frm", ".parquet", ".hdf5", ".ndjson", 
    ".arff", ".sav", ".sas7bdat", ".dmp", ".dat", ".idx", ".dbx", ".dbc", ".arc", ".dbase", ".gdb", ".fdb", ".adt", 
    ".pdb", ".qbw", ".adb", ".adf", ".pgn", ".bkf", ".bak", ".mbk", ".ibs", ".pgm", ".ndb", ".sas", ".spv", ".vdi", 
    ".vmdk", ".xlsb", ".xlt", ".xmltv", ".xmpz", ".kdb", ".mpb", ".ndb", ".pki", ".reb", ".sql", ".thumbdb", ".lmp", 
    ".msh", ".pdp", ".sav", ".shs", ".tlb", ".tml", ".wmf", ".xva", ".3gr", ".3gpp", ".acm", ".adn", ".afd", ".asq",
    
    # Web, scripts, código fuente y programación
    ".html", ".htm", ".xhtml", ".css", ".js", ".ts", ".jsx", ".tsx", ".json", ".xml", ".yml", ".yaml", ".vue", ".php", 
    ".asp", ".jsp", ".cfm", ".pl", ".cgi", ".rb", ".py", ".md", ".mdx", ".lock", ".toml", ".ini", ".env", ".scss", 
    ".sass", ".less", ".tpl", ".twig", ".ejs", ".pug", ".haml", ".xsl", ".xsd", ".xslt", ".svgz", ".woff", ".woff2", 
    ".ttf", ".eot", ".otf", ".ico", ".map", ".config", ".htaccess", ".htpasswd", ".hosts", ".sh", ".bat", ".ps1", 
    ".bash", ".fish", ".zsh", ".command", ".c", ".cpp", ".cxx", ".h", ".hpp", ".cs", ".vb", ".java", ".class", ".scala", 
    ".kt", ".swift", ".dart", ".go", ".rs", ".erl", ".ex", ".el", ".cl", ".lisp", ".r", ".jl", ".hs", ".sql", ".psql", 
    ".sqlite", ".sdf", ".r", ".rb", ".jsp", ".jsx", ".pyc", ".php", ".ts", ".tsx", ".jsp", ".l", ".lua", ".pl", ".pm", 
    ".jsp", ".cbl", ".cls", ".cls", ".clw", ".fs", ".gap", ".hxml", ".i3", ".inc", ".k", ".l", ".m", ".mli", ".mod", 
    ".pas", ".php3", ".php4", ".phps", ".plg", ".pwn", ".q", ".r3", ".rc", ".rex", ".rkt", ".rs", ".s", ".sbt", ".sc", 
    ".scd", ".scn", ".scpt", ".shtml", ".sql", ".st", ".sub", ".sup", ".sv", ".swift", ".tab", ".tcc", ".tcl", ".te", 
    ".tex", ".tpl", ".ts", ".tt", ".txt", ".uc", ".uml", ".vdproj", ".vhd", ".vhdl", ".vim", ".vimrc", ".vtl", ".xul", 
    ".y", ".yaml", ".yarn", ".zc", ".zi", ".zip", ".zzz", ".7zip", ".7z", ".arc", ".a", ".ar", ".asar", ".awk", ".axf",
    
    # Archivos de configuración y otros binarios
    ".cfg", ".conf", ".dat", ".bak", ".tmp", ".log", ".key", ".pem", ".crt", ".csr", ".ovpn", ".csr", ".pfx", ".htpasswd", 
    ".htaccess", ".hosts", ".reg", ".rdp", ".psd1", ".psm1", ".service", ".timer", ".target", ".mount", ".socket", 
    ".automount", ".swap", ".ovpn", ".psd", ".xml", ".vmdk", ".vdi", ".raw", ".img", ".iso", ".qemu", ".key", ".json", 
    ".lock", ".toml", ".env", ".yml", ".yaml", ".config", ".ini", ".plist", ".cfg", ".cnf", ".dmg", ".log", ".bak",
    
    # Otros
    ".blend", ".3ds", ".obj", ".fbx", ".stl", ".dae", ".x3d", ".lwo", ".skp", ".step", ".iges", ".sldprt", ".sldasm", 
    ".dwg", ".dxf", ".svgz", ".u3d", ".vtu", ".msh", ".ply", ".ma", ".mb", ".abc", ".usd", ".usdZ", ".glb", ".bvh", 
    ".ase", ".geo", ".abc", ".nwc", ".3mf", ".afdesign", ".afphoto", ".sketch", ".pat", ".grib", ".mtl", ".hdr", 
    ".jps", ".mpo", ".igs", ".iges", ".3dm", ".asc", ".igs", ".a3d", ".wrl", ".vrml", ".pov", ".obj", ".objz", ".objb", 
    ".dael", ".cdw", ".crp", ".fpp", ".fdb", ".vss", ".obj", ".svg", ".dwf", ".dwfx", ".g", ".kicad", ".sch", ".gbr", 
    ".gerber", ".pcb", ".pcbdoc", ".brd", ".trm", ".lay", ".gmf", ".dpv", ".fpb", ".fps", ".sd", ".scd", ".sht", ".sm", 
    ".tec", ".vtm", ".mf", ".vtu", ".tec", ".shp", ".geojson", ".dbf", ".cpg", ".sbn", ".prj", ".wld", ".prj"
]

    
    value_inside = tkinter.StringVar(root)
    value_inside.set("Selecciona una opcción")
    
    question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
    question_menu.config()
    question_menu.pack()
    
    def print_answers():
        p = "Selected Option: {}".format(value_inside.get())
        elemento = value_inside.get()
        datos.append(elemento)
        # Se muestra la opción seleccionada en la ventana de configuración
        global labele
        labele = tk.Label(root, text=p)
        labele.pack()
    
    submit_button = tkinter.Button(root, text='Agregar extensión', command=print_answers)
    submit_button.pack()
    
    def cr():
        global aoa
        aoa = entryLand.get()
        print("Nombre de la carpeta:", aoa)
        print("Extensiones seleccionadas:", datos)
        aoa_datos = (aoa, datos)
        # Se muestra en la ventana principal la carpeta y las extensiones elegidas
        Labelee = tk.Label(ventana, text=aoa_datos)
        Labelee.place(x=75, y=250, width=100, height=50)
        root.destroy()
        return aoa
    
    resultButton = tk.Button(root, text="--->", command=cr)
    resultButton.pack()
    
    root.mainloop()

# ------------------ Función para mover archivos según el modo personalizado ------------------ #
def otra():
    Carpeta_principal_2 = filedialog.askdirectory()
    archivos = os.listdir(Carpeta_principal_2)
    rutas_completas = [os.path.join(Carpeta_principal_2, nombre) for nombre in archivos]
    for x in rutas_completas:
        nombre_archivo, extension = os.path.splitext(x)
        ruta_c = f'{Carpeta_principal_2}/{aoa}'
        if not os.path.exists(ruta_c):
            os.mkdir(ruta_c)
        if extension in datos:
            shutil.move(x, ruta_c)

# ------------------ Función que decide qué modo ejecutar ------------------ #
def funcio():
    if var1.get() == 1:
        fun()
    elif var2.get() == 1:
        otra()

# ------------------ Elementos de la ventana principal ------------------ #
etiqueta = tkinter.Label(ventana, text="Selecciona un modo de ordenación de carpetas?", bg="black", fg="white", font=("Helvetica", 15, "bold"))
etiqueta.pack(fill=tkinter.X)

# Se carga la imagen usando la ruta absoluta
img_botton = tk.PhotoImage(file=get_resource_path("assets/imagen.png"))
Botón = tkinter.Button(compound="center", image=img_botton, command=funcio, height=200, width=110, cursor="hand2")
Botón.place(x=350, y=100, width=130, height=200)

casa = tk.Label(ventana, text="Crea carpetas, asignales extensiones, selecciona un directorio, y los archivos se ordenarán automáticamente", wraplength=125)
botonto = tkinter.Button(ventana, text="Añadir carpeta", command=carp, cursor="hand2")
casa1 = tk.Label(ventana, text="Busca entre los archivos del directorio seleccionado y crea una carpeta para cada extensión", wraplength=125)

# ------------------ Función para actualizar la vista según los checkbuttons ------------------ #
def actualizar_casillas():
    if var1.get() == 1 and var2.get() == 0:
        casilla2.deselect()
        casa.place_forget()
        casa1.place(x=200, y=40, width=150, height=200)
        botonto.place_forget()
    elif var2.get() == 1 and var1.get() == 0:
        casilla1.deselect()
        casa.place(x=200, y=170, width=150, height=200)
        casa1.place_forget()
        botonto.place(x=75, y=250, width=100, height=50)
    elif (var2.get() == 0 and var1.get() == 0) or (var2.get() == 1 and var1.get() == 1):
        casilla1.deselect()
        casilla2.deselect()
        botonto.place_forget()
        casa1.place_forget()
        casa.place_forget()

var1 = tk.IntVar()
var2 = tk.IntVar()

casilla1 = tk.Checkbutton(ventana, text="Predeterminado", variable=var1, command=actualizar_casillas, cursor="hand2")
casilla2 = tk.Checkbutton(ventana, text="Personalizado", variable=var2, command=actualizar_casillas, cursor="hand2")

casilla1.place(x=70, y=100, width=100, height=50)
casilla2.place(x=70, y=210, width=100, height=50)

ventana.mainloop()
