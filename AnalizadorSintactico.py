"""
PROGRAMA PRINCIPAL DEL ANALIZADOR SINTACTICO 

@Autor: Miche R. 
"""
#LIBRERIAS 
from tkinter import *
import tokens as AL

# Método para limpiar los campos de texto
def limpiar():
    print("Se accionó la limpieza de datos")
    c2.delete('1.0', END)
    c1.delete('1.0', END)

def analisisSintactico(tokens, c2):
    stack = []  # Pila para rastrear las etiquetas abiertas
    
    # Diccionario para mapear etiquetas de cierre a sus equivalentes de apertura
    
    etiquetas = {
        '</HTML>': '<HTML>',
        '</HEAD>': '<HEAD>',
        '</TITLE>': '<TITLE>',
        '</BODY>': '<BODY>',
        '</DIV>': '<DIV>',
        '</P>': '<P>',
        '</A>': '<A>',
        '</IMG>': '<IMG>',
        '</SCRIPT>': '<SCRIPT>',
        '</STYLE>': '<STYLE>',
        '</META>': '<META>',
        '</LINK>': '<LINK>',
        '</TABLE>': '<TABLE>',
        '</TR>': '<TR>',
        '</TD>': '<TD>',
        '</B>': '<B>',
        '</OL>': '<OL>',
        '</TH>': '<TH>',
        '</HREF>': '<HREF>',
        '</UL>': '<UL>',
        '</LI>': '<LI>',
        '</SPAN>': '<SPAN>',
        '</INPUT>': '<INPUT>',
        '</FORM>': '<FORM>',
        '</BUTTON>': '<BUTTON>',
        '</SELECT>': '<SELECT>',
        '</OPTION>': '<OPTION>',
        '</LABEL>': '<LABEL>',
        '</TEXTAREA>': '<TEXTAREA>',
        '</HR>': '<HR>',
        '</CANVAS>': '<CANVAS>',
        '</SVG>': '<SVG>',
        '</IFRAME>': '<IFRAME>',
        '</AUDIO>': '<AUDIO>',
        '</VIDEO>': '<VIDEO>',
        '</H>': '<H>',
    }

    errores = []  # Lista para almacenar mensajes de error
    lexemas_utilizados = []  # Lista para almacenar los lexemas utilizados

    # Verificar que la primera etiqueta sea <!DOCTYPE>
    if not tokens or tokens[0].value != '<!DOCTYPE>':
        errores.append("Error: Falta la declaración <!DOCTYPE> al principio del documento.")
    
    for token in tokens[1:]:  # Comenzar desde el segundo token
        lexemas_utilizados.append(token.value)  # Agregar el lexema actual a la lista de lexemas utilizados
        if token.type.startswith('ETIQUETA_'):
            if token.value.startswith('</'):  # Etiqueta de cierre
                if not stack:
                    errores.append(f"Error: Etiqueta {token.value} no tiene etiqueta de apertura correspondiente.")
                elif stack[-1] != etiquetas.get(token.value):
                    errores.append(f"Error: Etiqueta {token.value} no coincide con la última etiqueta abierta.")
                else:
                    stack.pop()  # Quita la etiqueta abierta correspondiente de la pila
            else:  # Etiqueta de apertura
                if token.value == '<!DOCTYPE>':  # Tratar la declaración <!DOCTYPE> de manera especial
                    continue  # Saltar la declaración <!DOCTYPE>
                stack.append(token.value)

    # Verificar que todas las etiquetas se hayan cerrado correctamente
    if stack:
        errores.append("Error: Falta cerrar algunas etiquetas.")

    if errores:
        for error in errores:
            c2.insert(END, error + '\n')
    else:
        c2.insert(END, "ANÁLISIS SINTÁCTICO EXITOSO.\n")
        c2.insert(END, "ÁRBOL SINTÁCTICO GENERADO\n")
        for lexema in lexemas_utilizados:
            c2.insert(END, lexema + '\n')

# Método para iniciar el análisis e insertar el resultado 
def analizador():
    entrada = c1.get("1.0", "end-1c")
    array = AL.analisisLexico(entrada)
    c2.delete('1.0', END) 
    analisisSintactico(array, c2)

#TKINTER 
ventana = Tk()
ventana.title("ANALIZADOR LÉXICO & SINTÁCTICO DE HTML | Miche R.")
ventana.geometry("800x700")
ventana.config(bg='white') # Color de la ventana 
ventana.resizable(False, False)

color = '#FFFFC2'  # color de las ventanas 
colorletra = '#2E4053' # Color de las letras 

# Frame
f = Frame()
f.pack()
f.config(width="780", height="680", bg=color)
f.place(x=10, y=10)

#titulo d ela ventana 
l1 = Label(f, width="24", height="1", bg=color, fg=colorletra, font=("Arial Black", 28), text="Analizador Léxico & Sintáctico")
l1.place(x=80, y=1)

#entrada del codigo
l2 = Label(f, width="8", height="1", text="ENTRADA", fg=colorletra, font=("Arial Black", 12), bg=color)
l2.grid(sticky="w")
l2.place(x=20, y=70)

c1 = Text(f, width="35", height="25", font=(colorletra, 12))
c1.place(x=20, y=100)
scroll = Scrollbar(f, command=c1.yview)
scroll.grid(sticky="nsew")
scroll.place(in_=c1, relx=1, relheight=1, bordermode="outside")
c1.config(yscrollcommand=scroll.set)

#salida del codigo 
l3 = Label(f, width="10", height="1", text="SALIDA", fg=colorletra, font=("Arial Black", 12), bg=color)
l3.grid(sticky="e")
l3.place(x=400, y=70)

c2 = Text(f, width="35", height="25", font=("Arial", 12))
c2.place(x=420, y=100)
scroll2 = Scrollbar(f, command=c2.yview)
scroll2.grid(sticky="nsew")
scroll2.place(in_=c2, relx=1, relheight=1, bordermode="outside")
c2.config(yscrollcommand=scroll2.set)
c2.config(state="normal")

#configuracion de los botones 
botonAnalizar = Button(f, text="Validar", font=("Arial Black", 12), fg=colorletra, command=analizador)
botonAnalizar.place(x=15, y=630, width=100, height=30)

botonLimpiar = Button(f, text="Limpiar", font=("Arial Black", 12), fg=colorletra, command=limpiar)
botonLimpiar.place(x=140, y=630, width=100, height=30)

#metodo de ejecucion 
ventana.mainloop()
