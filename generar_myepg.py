from datetime import datetime, timedelta

canales = [
    ("MI_MUSICA_ROMANTICA", "Mi Musica Romantica", "100% Amor"),
    ("MI_MUSICA_REGGAETON", "Mi Musica Reggaeton", "Puro Flow"),
    ("MI_MUSICA_SALSA", "Mi Musica Salsa", "Musica Salsa las 24 horas"),
    ("FOLKLORICO", "Folklorico", "Musica folklorica chamamé variada las 24 horas"),
    ("TIERRA_MIA_TV", "Tierra Mia TV", "24 horas Chamamé rioplatense"),
    ("BILLBOARD", "Billboard", "Billboard"),
    ("EMISORAS", "Emisoras", "Disfruta caundo quieras tus emisoras favoritas las 24 HS - Música variada"),
    ("LFP_PLAY", "Lfp PLay", "Eventos disponibles de la Liga de Fútbol Profesional Argentina - PRIMERA B NACIOINAL entre otros"),
    ("UN_POCO_DE_RUIDO", "Un Poco de Ruido", "Cumbia 24 hs de la mano de Un Poco de Ruido"),
    ("GH_DORADA", "Gh Dorada", "Viví las 24 horas de tu reality favorito con las camáras disponibles las 24/7")
]


fecha_inicio = datetime.utcnow().replace(
    hour=0,
    minute=0,
    second=0,
    microsecond=0
)


xml = """<?xml version="1.0" encoding="UTF-8"?>
<tv generator-info-name="EPG Automatico">
"""


# Crear canales

for canal_id, nombre, programa in canales:
    xml += f"""
<channel id="{canal_id}">
    <display-name>{nombre}</display-name>
</channel>
"""


# Crear programación 30 días

for dia in range(30):

    inicio = fecha_inicio + timedelta(days=dia)
    fin = inicio + timedelta(days=1)

    start = inicio.strftime("%Y%m%d%H%M%S")
    stop = fin.strftime("%Y%m%d%H%M%S")

    for canal_id, nombre, programa in canales:

        xml += f"""
<programme channel="{canal_id}" start="{start} +0000" stop="{stop} +0000">
    <title>{programa}</title>
    <desc>Programacion musical 24 horas</desc>
</programme>
"""


xml += """
</tv>
"""


# Guardar archivo

with open("epgmy.xml", "w", encoding="utf-8") as archivo:
    archivo.write(xml)


print("EPG actualizado correctamente")
