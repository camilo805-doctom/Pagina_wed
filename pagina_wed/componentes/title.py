import reflex as rx
import pagina_wed.Styles.styles as styles

def title(text:str)->rx.component:
    return rx.heading(
        text,
        size="lg",
        style=styles.title_style  
    )