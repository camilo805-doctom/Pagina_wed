import reflex as rx
import pagina_wed.Styles.styles as styles
from pagina_wed.Styles.styles import tamaños as tamaños

def boton_link(title: str, body: str, image: str, url: str)->rx.component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.tamaños.BIG.value,
                    height=styles.tamaños.DEFAULT.value,
                    margin=tamaños.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing=tamaños.SMALL.value,
                    padding_y=tamaños.SMALL.value,
                    padding_rigth=tamaños.SMALL.value
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=True,
        width="100%",
        text_decoration="none"
    )
