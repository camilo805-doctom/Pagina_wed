import reflex as rx
import datetime
from pagina_wed.Styles.styles import tamaños as tamaños
from pagina_wed.Styles.colores import text_color as text_color

def footer()->rx.Component:
    return rx.vstack(
        rx.image(
            src="LOGO.gif",
            height=tamaños.VERY_BIG.value,
            weight=tamaños.VERY_BIG.value,
            alt="Logotipo de SEGA. Un gif usado enfocado en gaming."
            ),
        rx.link(
                f"2020-{datetime.date.today().year} luxsama2603 by Juan Camilo Muñoz Bautista.",
                href="https://www.twitch.tv/luxsama2603",
                is_external=True,
                font_size=tamaños.MEDIUM.value
        ),
        rx.text(
            "BOGOTA, COLOMBIA.",
            font_size=tamaños.MEDIUM.value,
            margin_top=tamaños.ZERO.value
        ),
        margin_bottom=tamaños.BIG.value,
        padding_bottom=tamaños.BIG.value,
        padding_x=tamaños.BIG.value,
        spacing=tamaños.DEFAULT.value,
        color=text_color.FOOTER.value

    )