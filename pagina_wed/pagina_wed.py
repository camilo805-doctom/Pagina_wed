import reflex as rx 
from pagina_wed.componentes.barra_nav import barra_nav
from pagina_wed.componentes.footer import footer
from pagina_wed.views.header.header import header
from pagina_wed.views.links.links import links
import pagina_wed.Styles.styles as styles
from pagina_wed.Styles.styles import tamaños as tamaños

#class State(rx.State):
#    pass


def index() -> rx.Component:
    return rx.box(
        barra_nav(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH, #contenido CSS
                width="100%",
                margin_y=tamaños.BIG.value,
                padding=tamaños.BIG.value
            )
        ),
        footer()
    )



app=rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Luxsama | Juegos, charlas y programación.",
    description="Hola mi nombre es Lux, stremer y estudiante de programacion colombiano.",
    image="gamepad-solid.svg"
)
app.compile()


