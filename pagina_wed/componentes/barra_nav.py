import reflex as rx
import pagina_wed.Styles.styles as Styles
from pagina_wed.Styles.styles import tamaños as tamaños
from pagina_wed.Styles.colores import color as color

def barra_nav() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("lux", color=color.PRIMARIO.value),
            rx.span("sama", color=color.SECUNDARIO.value),
            style=Styles.barra_nav_title_style
        ),
        position="sticky",
        bg=color.CONTENIDO.value,
        padding_x=tamaños.BIG.value,
        padding_y=tamaños.DEFAULT.value,
        z_index="999",
        top="0"
    )


