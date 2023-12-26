import reflex as rx
from pagina_wed.componentes.link_icon import link_icon
from pagina_wed.componentes.info_text import info_text
from pagina_wed.Styles.styles import tamaños as tamaños
from pagina_wed.Styles.colores import color as color
from pagina_wed.Styles.colores import text_color as text_color

def header() -> rx.component:
    return rx.vstack(
        rx.hstack(
         rx.avatar(
             name="Lux Sama", 
             size="xl",
             src="AVATAR.jpg",
             color=text_color.BODY.value,
             bg=color.CONTENIDO.value,
             padding="2px",
             border="4px",
             border_color=color.PRIMARIO.value
        ),
         rx.vstack(
                    rx.heading(
                        "Luxsama",
                        size="lg"
                    ),
                    rx.text(
                        "@luxsama2603",
                        margin_top=tamaños.ZERO.value,
                        color=text_color.BODY.value
                    ),
                    rx.hstack(
                        link_icon(
                            "icons/instagram.svg",
                            "https://www.instagram.com/camilomunozb_/",
                            "Instagram"
                            ),
                        link_icon(
                            "icons/github.svg",
                            "https://github.com/camilo805-doctom",
                            "Github"
                            ),
                            spacing=tamaños.DEFAULT.value
                    ),
                    align_items="start",       
            ),
            spacing=tamaños.DEFAULT.value
        ),
        rx.flex(
            info_text("+4","meses stremeando y programando"),
            rx.spacer(),
            info_text("Afiliado:", "Twitch"),
            rx.spacer(),
            info_text("Adidas:", "algun dia patrocinador"),
            width="100%"
        ),
        rx.text(
                """
                Me llamo Lux, tengo 20 años y soy próximo estudiante de ingeniería.
                Me gustan los juegos, el anime, programar y loquear. Espero que pases un buen rato y que te diviertas conmigo. 
                posdata: saluden, porque qué bonito es saludar y ser saludado xd.
                """,
                font_size=tamaños.DEFAULT.value,
                color=text_color.BODY.value
            ),
        spacing=tamaños.BIG.value,
        align_items="start"
         
    )
