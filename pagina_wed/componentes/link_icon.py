import reflex as rx
from pagina_wed.Styles.styles import tamaños as tamaños

def link_icon(image: str, url:str, alt: str)->rx.component:
    return rx.link(
        rx.image(
            src=image,
            width=tamaños.DEFAULT.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )