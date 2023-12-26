import reflex as rx
from enum import Enum
from .colores import color as color
from .colores import text_color as text_color
from .fuentes import fuentes, fontWeight

#constantes
MAX_WIDTH="600px"

#cargar fuentes

STYLESHEETS={
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
}

#tamaños
class tamaños(Enum):
    #para este caso "em" representa "16px"
    ZERO="0px !important"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE="1.5em"
    BIG="2em"
    VERY_BIG="2.5em"


#estilo base
BASE_STYLE={
    "font_family":fuentes.DEFAULT.value,
    "font_weight":fontWeight.LIGTH.value,
    "background_color": color.FONDO.value,
    rx.Heading:{
        "size":"lg",
        "color":text_color.HEADER.value,
        "font_family":fuentes.TITLE.value,
        "font_weight":fontWeight.MEDIUM.value,
    },
    rx.Button:{
        "width":"100%",
        "height":"100%",
        "padding": tamaños.SMALL.value,
        "border_radius":tamaños.DEFAULT.value,
        "color":text_color.HEADER.value,
        "background_color": color.CONTENIDO.value,
        "white_space":"normal",
        "text_aling":"start",
        "_hover":{
            "background_color": color.SECUNDARIO.value
        }
    },
    rx.Link:{
        "text_decoration":"none",
        "_hover":{}
    }
}


#fuentes
barra_nav_title_style=dict(
    font_family=fuentes.LOGO.value,
    font_weight=fontWeight.MEDIUM.value,
    font_size=tamaños.LARGE.value
)

#cabezera del titulo
title_style=dict(
    width="100%",
    size="lg",
    padding_top=tamaños.DEFAULT.value,
)


#redefinir estilos
button_title_style=dict(
    font_family=fuentes.TITLE.value,
    font_weight=fontWeight.MEDIUM.value,
    font_size=tamaños.DEFAULT.value,
    color=text_color.HEADER.value
)

button_body_style=dict(
    font_weight=fontWeight.LIGTH.value,
    font_size=tamaños.MEDIUM.value,
    color=text_color.BODY.value
)

