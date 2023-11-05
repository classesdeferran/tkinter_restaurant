# importar la llibreria sensera
from tkinter import *

# iniciar tkinter --> crear objeto
aplicacion = Tk()
# ahora aplicacion puede recibir los métodos de tkinter

# ===================================================================
# CONFIGURACIÓ BÂSICA

# mides --> geometry(mides + posX + posY)
aplicacion.geometry("1020x630+0+0")

# evitar canvi de mides --> resizable( eixX, eixY)
aplicacion.resizable(0, 0)

# definir títol --> title("Titol")
aplicacion.title('Restaurant')

# color de fons de la finestra --> config(bg="color")
# també admet RGB
aplicacion.config(bg="burlywood")

# ===================================================================
# MAQUETACIÓ

# panell superior --> 
#   Frame( 
#       on s'aplica (aplicacion),    
#       bd = gruix de bora, 
#       relievef = [FLAT, RAISED, SUNKEN, GROOVE, RIDGE]
# )
panell_superior = Frame(aplicacion, bd=1, relief=FLAT)
# posició
panell_superior.pack(side=TOP)

# etiqueta títol 
etiqueta_titulo = Label(panell_superior, text='Sistema de facturación', 
                        fg="azure4", font=('Helvetica', 48), 
                        bg="burlywood", width= 27 )
etiqueta_titulo.grid(row = 0, column= 0)

# panell esquerra
panel_izquierdo = Frame( aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panell costos
panel_costos =  Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# panell menjar --> LabelFrame() es un frame con etiqueta incluida
panel_comidas = LabelFrame( panel_izquierdo, text='Comidas', 
                           font=('Helvetica', 16, 'bold'),
                           bd=1, relief=FLAT, fg="azure4" )
panel_comidas.pack(side=LEFT)

# panell beure --> LabelFrame() es un frame con etiqueta incluida
panel_bebidas = LabelFrame( panel_izquierdo, text='Bebidas', 
                           font=('Helvetica', 16, 'bold'),
                           bd=1, relief=FLAT, fg="azure4" )
panel_bebidas.pack(side=LEFT)

# panell postres --> LabelFrame() es un frame con etiqueta incluida
panel_postres = LabelFrame( panel_izquierdo, text='Postres', 
                           font=('Helvetica', 16, 'bold'),
                           bd=1, relief=FLAT, fg="azure4" )
panel_postres.pack(side=LEFT)


# panel derecha
panel_derecha = Frame( aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame( panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack(side=TOP)

# panel recibo
panel_recibo = Frame( panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_recibo.pack(side=TOP)

# panel botones
panel_botones = Frame( panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_botones.pack(side=TOP)


# lista de productos
lista_comidas = ["Pollo", 'Paella', "Salmón", 'Ensalada', 'Croquetas', 'Bistec', 'Macarrones', 'Tortilla']
lista_bebidas = ['Agua sin gas', 'Agua con gas', 'Vino blanco', 'Vino tinto', 'Cava', 'Cola', 'Cerveza', 'Café']
lista_postres = ['Fruta 1', 'Fruta 2', 'Fruta 3','Helado', 'Pastel', 'Flan', 'Crema', 'Mousse']




# loop del menjars
variables_comida = [] # per a guardar la selecció
cuadros_comida = []
texto_Comida = []

contador = 0
for comida in lista_comidas:

    # crear check button
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Helvetica', 16, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W) # sticky --> alinea a l'esquerra
    contador += 1

# loop de les begudess
variables_bebida = [] # per a guardar la selecció
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Helvetica', 16, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W) # sticky --> alinea a l'esquerra
    contador += 1

# loop de les postres
variables_postres = [] # per a guardar la selecció
contador = 0
for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Helvetica', 16, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postres[contador])
    postre.grid(row=contador, column=0, sticky=W) # sticky --> alinea a l'esquerra
    contador += 1


# Ara els panells estan centrats en sentit vertical





# ===================================================================
# evitar que la pantalla se cierre
aplicacion.mainloop()