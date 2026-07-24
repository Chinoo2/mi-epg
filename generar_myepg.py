from datetime import datetime, timedelta

canales = [
    ("MI_MUSICA_ROMANTICA", "100% Amor"),
    ("MI_MUSICA_REGGAETON", "Puro Flow"),
    ("MI_MUSICA_SALSA", "Musica Salsa"),
    ("FOLKLORICO", "Musica folklorica chamamé"),
    ("TIERRA_MIA_TV", "24 horas Chamamé"),
    ("BILLBOARD", "Billboard")
]

inicio = datetime.utcnow().replace(hour=0, minute=0, second=0)

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<tv generator-info-name="EPG Automatico">
'''

for canal, nombre in canales:
    xml += f'''
<channel id="{canal}">
<display-name>{canal}</display-name>
</channel>
'''

for canal, programa in canales:
    for dia in range(30):
        start = inicio + timedelta(days=dia)
        stop = start + timedelta(days=1)

        xml += f'''
<programme channel="{canal}" 
start="{start.strftime("%Y%m%d%H%M%S")} +0000" 
stop="{stop.strftime("%Y%m%d%H%M%S")} +0000">

<title>{programa}</title>
<desc>Programacion 24 horas</desc>

</programme>
'''

xml += "\n</tv>"

with open("epg.xml","w",encoding="utf-8") as f:
    f.write(xml)

print("EPG actualizado")
