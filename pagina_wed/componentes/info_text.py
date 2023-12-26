import reflex as rx
from pagina_wed.Styles.styles import tamaños as tamaños
from pagina_wed.Styles.colores import color as color
from pagina_wed.Styles.colores import text_color as text_color

def info_text(title:str,body:str)->rx.component:
    return rx.box(
        rx.span(
            title,
            font_weight="bold",
            color=color.PRIMARIO.value
        ),
        f" {body}",
        font_size=tamaños.MEDIUM.value,
        color=text_color.BODY.value

    )