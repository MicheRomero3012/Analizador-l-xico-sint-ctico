"""
TABLA DE TOKENS DE LOS ANALIZADORES 

@Autor: Miche R. 
"""
#LIBRERIAS
import ply.lex as lex

# Lista de tokens de HTML
tokens = [
    'SUMA',
    'ASIGNACION',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'IGUAL',
    'MAYOR_IGUAL_QUE',
    'MENOR_IGUAL_QUE',
    'DIFERENTE',
    'MAYOR_QUE',
    'MENOR_QUE',
    'COMILLA_DOBLE',
    'COMILLA_SIMPLE',
    'PARENTESIS_A',
    'PARENTESIS_B',
    'ADMIRACION',
    'INTERROGACION',
    'PUNTO',
    'COMA',
    'GUION_BAJO',
    'CARACTERES',
    'DIGITO',
    'COMENTARIO',
    'ETIQUETA_HTML',
    'ETIQUETA_DOCTYPE',
    'ETIQUETA_HEAD',
    'ETIQUETA_TITLE',
    'ETIQUETA_BODY',
    'ETIQUETA_DIV',
    'ETIQUETA_A',
    'ETIQUETA_IMG',
    'ETIQUETA_SCRIPT',
    'ETIQUETA_STYLE',
    'ETIQUETA_META',
    'ETIQUETA_LINK',
    'ETIQUETA_TABLE',
    'ETIQUETA_TR',
    'ETIQUETA_TD',
    'ETIQUETA_B',
    'ETIQUETA_P',
    'ETIQUETA_OL',
    'ETIQUETA_TH',
    'ETIQUETA_HREF',
    'ETIQUETA_UL',
    'ETIQUETA_LI',
    'ETIQUETA_SPAN',
    'ETIQUETA_INPUT',
    'ETIQUETA_FORM',
    'ETIQUETA_BUTTON',
    'ETIQUETA_SELECT',
    'ETIQUETA_OPTION',
    'ETIQUETA_LABEL',
    'ETIQUETA_TEXTAREA',
    'ETIQUETA_HR',
    'ETIQUETA_CANVAS',
    'ETIQUETA_SVG',
    'ETIQUETA_IFRAME',
    'ETIQUETA_AUDIO',
    'ETIQUETA_VIDEO',
    'ETIQUETA_H',
]
#OPERADORES 
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
#COMPARADORES
t_IGUAL = r'=='
t_MAYOR_IGUAL_QUE = r'>='
t_MENOR_IGUAL_QUE = r'<='
t_DIFERENTE = r'!='
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
#SIMBOLOS
t_COMILLA_DOBLE = r'"'
t_COMILLA_SIMPLE = r'\''
t_PARENTESIS_A = r'\('
t_PARENTESIS_B = r'\)'
t_ADMIRACION = r'\!'
t_INTERROGACION = r'\?'
t_PUNTO = r'\.'
t_COMA = r'\,'
t_GUION_BAJO = r'\_'

# Regla para cadenas de caracteres
def t_CARACTERES(t):
    r'[a-zA-Z]+'
    return t

# Regla para dígitos
def t_DIGITO(t):
    r'\d+'
    return t

# Regla para comentarios 
def t_COMENTARIO(t):
    r'<!--.*?-->'
    return t

# Regla para ignorar espacios en blanco y saltos de línea
t_ignore = ' \t\n'

# Palabras reservadas de HTML
palabras_reservadas = {
    'HTML': 'HTML',
    'HEAD': 'HEAD',
    'TITLE': 'TITLE',
    'BODY': 'BODY',
    'DIV': 'DIV',
    'P': 'P',
    'A': 'A',
    'IMG': 'IMG',
    'DOCTYPE': 'DOCTYPE',
    'SCRIPT': 'SCRIPT',
    'STYLE': 'STYLE',
    'META': 'META',
    'LINK': 'LINK',
    'TABLE': 'TABLE',
    'TR': 'TR',
    'TD': 'TD',
    'B': 'B',
    'OL': 'OL',
    'TH': 'TH',
    'HREF': 'HREF',
    'UL': 'UL',
    'LI': 'LI',
    'SPAN': 'SPAN',
    'INPUT': 'INPUT',
    'FORM': 'FORM',
    'BUTTON': 'BUTTON',
    'SELECT': 'SELECT',
    'OPTION': 'OPTION',
    'LABEL': 'LABEL',
    'TEXTAREA': 'TEXTAREA',
    'HR': 'HR',
    'CANVAS': 'CANVAS',
    'SVG': 'SVG',
    'IFRAME': 'IFRAME',
    'AUDIO': 'AUDIO',
    'VIDEO': 'VIDEO',
    'H': 'H',
}


# Agregar palabras reservadas a la lista de tokens
tokens += list(palabras_reservadas.values())

# Expresiones Regulares para etiquetas de HTML 
def t_ETIQUETA_HTML(t):
    r'<(/?)(HTML)>'
    return t

def t_ETIQUETA_DOCTYPE(t):
    r'<!DOCTYPE>'
    return t

def t_ETIQUETA_HEAD(t):
    r'<(/?)(HEAD)>'
    return t

def t_ETIQUETA_TITLE(t):
    r'<(/?)(TITLE)>'
    return t

def t_ETIQUETA_BODY(t):
    r'<(/?)(BODY)>'
    return t

def t_ETIQUETA_DIV(t):
    r'<(/?)(DIV)>'
    return t

def t_ETIQUETA_A(t):
    r'<(/?)([Aa](\s+HREF\s*=\s*"[A-Za-z]+")?)>'
    return t

def t_ETIQUETA_IMG(t):
    r'<img\s+(src\s*=\s*"[^"]*"\s+alt\s*=\s*"[^"]*"\s*)?/?>'
    return t

def t_ETIQUETA_SCRIPT(t):
    r'<(/?)(SCRIPT)>'
    return t

def t_ETIQUETA_STYLE(t):
    r'<(/?)(STYLE)>'
    return t

def t_ETIQUETA_META(t):
    r'<META\s+name\s*=\s*"[^"]*"\s+content\s*=\s*"[^"]*"\s*/?>'
    return t

def t_ETIQUETA_LINK(t):
    r'<(/?)(LINK)>'
    return t

def t_ETIQUETA_TABLE(t):
    r'<(/?)(TABLE)>'
    return t

def t_ETIQUETA_TR(t):
    r'<(/?)(TR)>'
    return t

def t_ETIQUETA_TD(t):
    r'<(/?)(TD)>'
    return t

def t_ETIQUETA_B(t):
    r'<(/?)(B)>'
    return t

def t_ETIQUETA_P(t):
    r'<(/?)(P)>'
    return t

def t_ETIQUETA_OL(t):
    r'<(/?)(OL)>'
    return t

def t_ETIQUETA_TH(t):
    r'<(/?)(TH)>'
    return t

def t_ETIQUETA_HREF(t):
    r'<(HREF)>'
    return t

def t_ETIQUETA_UL(t):
    r'<(/?)(UL)>'
    return t

def t_ETIQUETA_LI(t):
    r'<(/?)(LI)>'
    return t

def t_ETIQUETA_SPAN(t):
    r'<(/?)(SPAN)>'
    return t

def t_ETIQUETA_INPUT(t):
    r'<(INPUT)>'
    return t

def t_ETIQUETA_FORM(t):
    r'<(/?)(FORM)>'
    return t

def t_ETIQUETA_BUTTON(t):
    r'<(/?)(BUTTON)>'
    return t

def t_ETIQUETA_SELECT(t):
    r'<(/?)(SELECT)>'
    return t

def t_ETIQUETA_OPTION(t):
    r'<(/?)(OPTION)>'
    return t

def t_ETIQUETA_LABEL(t):
    r'<(/?)(LABEL)>'
    return t

def t_ETIQUETA_TEXTAREA(t):
    r'<(/?)(TEXTAREA)>'
    return t

def t_ETIQUETA_HR(t):
    r'<(/?)(HR)>'
    return t

def t_ETIQUETA_CANVAS(t):
    r'<(/?)(CANVAS)>'
    return t

def t_ETIQUETA_SVG(t):
    r'<(/?)(SVG)>'
    return t

def t_ETIQUETA_IFRAME(t):
    r'<(/?)(IFRAME)>'
    return t

def t_ETIQUETA_AUDIO(t):
    r'<(/?)(AUDIO)>'
    return t

def t_ETIQUETA_VIDEO(t):
    r'<(/?)(VIDEO)>'
    return t

def t_ETIQUETA_H(t):
    r'<(/?)(H[0-9]+)>'
    return t

# Regla para manejar errores léxicos
def t_error(t):
    print(f"Carácter no válido: {t.value[0]}")
    t.lexer.skip(1)
#####################################################################################################################################
# Método para análisis de tokens
def analisisLexico(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    array = []
    while True:
        tok = analizador.token()
        if not tok:
            break
        array.append(tok)
    return array


