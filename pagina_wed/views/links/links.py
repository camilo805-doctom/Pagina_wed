import reflex as rx
from pagina_wed.componentes.boton_link import boton_link
from pagina_wed.componentes.title import title
from pagina_wed.Styles.styles import tamaños as tamaños

def links() -> rx.component:
    return rx.vstack(
        title("Comunidad"),
        boton_link(
            "Twitch", 
            "Directos de lunes a Sabado", 
            "icons/twitch.svg",
            "https://www.twitch.tv/luxsama2603",

        ),
        boton_link(
            "Instagram", 
            "Sigame sin pena",
            "icons/instagram.svg",
            "https://www.instagram.com/camilomunozb_/"
        ),
        boton_link(
            "Tik-Tok", 
            "Cuando me acuerdo subo pendejadas",
            "icons/tiktok.svg",
            "https://www.tiktok.com/@camilom_3"
        ),
        boton_link(
            "Donaciones", 
            "Si quieres apoyarme a mantener una familia de 4 hijos y un perro", 
            "icons/paypal.svg",
            "https://streamlabs.com/luxsama2603/tip"
        ),
        boton_link(
            "Grupo de WhatsApp", 
            "Parchate en el grupo mas chimba",
            "icons/whatsapp.svg",
            "https://chat.whatsapp.com/JcT5iKCJaGdHBjwOW3fLkh"
        ),
        title("Recursos"),
        boton_link(
            "Patrocionios y mas", 
            "Whatsapp de contrato",
            "icons/whatsapp.svg",
            "https://wa.me/qr/46IJQWNJAJHWB1"
        ),
        boton_link(
            "Steam",
            "Por si quieres regalarme un juego",
            "icons/steam.svg",
            "https://steamcommunity.com/tradeoffer/new/?partner=1485499976&token=VW7n5c_H"
        ),
        boton_link(
            "Amazon",
            "Si quieres apoyar la produccion del canal",
            "icons/amazon.svg",
            "https://www.amazon.com/hz/wishlist/dl/invite/gYEEF1I?ref_=wl_share"
        ),
        width="100%",
        spacing=tamaños.MEDIUM.value
    )

        