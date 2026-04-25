from fpdf import FPDF
import os

class ProspectosPDF(FPDF):
    def header(self):
        # Fondo negro
        self.set_fill_color(10, 10, 15)
        self.rect(0, 0, 210, 297, 'F')
        # Barra superior cian
        self.set_fill_color(0, 229, 204)
        self.rect(0, 0, 210, 3, 'F')
        # Logo / titulo
        self.set_y(8)
        self.set_font('Helvetica', 'B', 18)
        self.set_text_color(0, 229, 204)
        self.cell(0, 8, 'RYVENTIS SOLUTIONS', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_font('Helvetica', '', 9)
        self.set_text_color(136, 136, 168)
        self.cell(0, 5, 'Reporte de Prospeccion | Puebla, Mexico | Abril 2026', align='C', new_x='LMARGIN', new_y='NEXT')
        # Linea separadora
        self.set_draw_color(0, 229, 204)
        self.set_line_width(0.5)
        self.line(15, self.get_y() + 2, 195, self.get_y() + 2)
        self.ln(6)

    def footer(self):
        self.set_y(-12)
        self.set_fill_color(0, 229, 204)
        self.rect(0, 284, 210, 3, 'F')
        self.set_font('Helvetica', 'I', 7)
        self.set_text_color(136, 136, 168)
        self.cell(0, 6, f'Ryventis Solutions  |  ryventis.mx  |  Pagina {self.page_no()}', align='C')

    def prospecto_card(self, numero, nombre, sector, zona, telefono, sitio_web, redes,
                        pain_point, servicios, calificacion, por_que, msg_wa, msg_email):

        # Color por calificacion
        if calificacion == 'Alta':
            cal_color = (0, 229, 204)
        elif calificacion == 'Media-Alta':
            cal_color = (124, 58, 237)
        else:
            cal_color = (136, 136, 168)

        y_start = self.get_y()

        # Encabezado con numero y nombre
        self.set_fill_color(0, 229, 204)
        self.rect(12, y_start, 186, 8, 'F')
        self.set_xy(14, y_start + 1.5)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(10, 10, 15)
        self.cell(186, 5, f'  PROSPECTO {numero}   {nombre.upper()}', new_x='LMARGIN', new_y='NEXT')

        # Cuerpo de la tarjeta
        card_y = self.get_y()
        self.set_fill_color(22, 22, 35)
        self.rect(12, card_y, 186, 4, 'F')

        # Badge de calificacion
        self.set_xy(160, card_y + 0.8)
        self.set_fill_color(*cal_color)
        self.set_font('Helvetica', 'B', 7)
        self.set_text_color(10, 10, 15)
        self.cell(36, 2.5, f'  {calificacion.upper()}  ', align='C', fill=True)
        self.set_xy(14, card_y + 0.8)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(136, 136, 168)
        self.cell(140, 2.5, f'{sector}  |  {zona}')
        self.ln(5)

        # Datos de contacto
        self.set_x(14)
        self.set_fill_color(22, 22, 35)
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(0, 229, 204)
        self.cell(30, 4, 'Telefono:', new_x='RIGHT', new_y='LAST')
        self.set_font('Helvetica', '', 8)
        self.set_text_color(240, 240, 248)
        self.cell(80, 4, telefono, new_x='RIGHT', new_y='LAST')
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(0, 229, 204)
        self.cell(25, 4, 'Sitio web:', new_x='RIGHT', new_y='LAST')
        self.set_font('Helvetica', '', 8)
        self.set_text_color(240, 240, 248)
        self.cell(0, 4, sitio_web, new_x='LMARGIN', new_y='NEXT')

        self.set_x(14)
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(0, 229, 204)
        self.cell(30, 4, 'Redes:', new_x='RIGHT', new_y='LAST')
        self.set_font('Helvetica', '', 8)
        self.set_text_color(240, 240, 248)
        self.cell(0, 4, redes, new_x='LMARGIN', new_y='NEXT')

        self.ln(1)

        # Seccion: Por que es prospecto
        self.set_x(14)
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(124, 58, 237)
        self.cell(0, 5, 'POR QUE ES UN BUEN PROSPECTO:', new_x='LMARGIN', new_y='NEXT')
        self.set_x(14)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(240, 240, 248)
        self.multi_cell(182, 4, por_que, new_x='LMARGIN', new_y='NEXT')

        self.ln(1)

        # Seccion: Servicios
        self.set_x(14)
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(0, 229, 204)
        self.cell(0, 5, 'SERVICIOS RECOMENDADOS:', new_x='LMARGIN', new_y='NEXT')
        self.set_x(14)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(240, 240, 248)
        self.multi_cell(182, 4, servicios, new_x='LMARGIN', new_y='NEXT')

        self.ln(1)

        # Mensaje WhatsApp
        self.set_x(14)
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(0, 229, 204)
        self.cell(0, 5, 'MENSAJE DE WHATSAPP:', new_x='LMARGIN', new_y='NEXT')
        # Caja con fondo diferente para el mensaje
        msg_y = self.get_y()
        self.set_fill_color(10, 10, 15)
        self.set_x(14)
        # Calcular altura necesaria
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(200, 240, 235)
        self.set_x(16)
        self.multi_cell(180, 4, f'"{msg_wa}"', fill=True, new_x='LMARGIN', new_y='NEXT')

        self.ln(1)

        # Correo electronico
        self.set_x(14)
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(124, 58, 237)
        self.cell(0, 5, 'CORREO ELECTRONICO:', new_x='LMARGIN', new_y='NEXT')
        self.set_x(14)
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(136, 136, 168)
        self.cell(15, 4, 'Asunto:', new_x='RIGHT', new_y='LAST')
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(240, 240, 248)
        lines = msg_email.split('\n')
        asunto = lines[0] if lines else ''
        cuerpo = '\n'.join(lines[1:]) if len(lines) > 1 else ''
        self.cell(0, 4, asunto, new_x='LMARGIN', new_y='NEXT')
        self.set_x(14)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(200, 200, 220)
        self.multi_cell(182, 4, cuerpo, new_x='LMARGIN', new_y='NEXT')

        # Linea separadora
        self.ln(3)
        self.set_draw_color(40, 40, 60)
        self.set_line_width(0.3)
        self.line(12, self.get_y(), 198, self.get_y())
        self.ln(5)


def safe(text):
    replacements = {
        '\u00e1': 'a', '\u00e9': 'e', '\u00ed': 'i', '\u00f3': 'o', '\u00fa': 'u',
        '\u00c1': 'A', '\u00c9': 'E', '\u00cd': 'I', '\u00d3': 'O', '\u00da': 'U',
        '\u00fc': 'u', '\u00dc': 'U', '\u00f1': 'n', '\u00d1': 'N',
        '\u00bf': '?', '\u00a1': '!', '\u2014': '--', '\u2013': '-',
        '\u201c': '"', '\u201d': '"', '\u2018': "'", '\u2019': "'",
    }
    for orig, repl in replacements.items():
        text = text.replace(orig, repl)
    return text


prospectos = [
    {
        "numero": 1,
        "nombre": "Centro Dental Ayon",
        "sector": "Clinica Dental",
        "zona": "Santa Cruz Buenavista - Zavaleta",
        "telefono": "222 323 4235",
        "sitio_web": "centrodentalayon.com",
        "redes": "Sin redes detectadas activamente",
        "calificacion": "Alta",
        "por_que": (
            "Ofrece agendado por WhatsApp de forma manual en su propio sitio. "
            "Atiende lunes a sabado de 8am a 6pm -- fuera de ese horario los pacientes "
            "escriben y no reciben respuesta, perdiendo citas ante la competencia. "
            "La zona Zavaleta tiene alta densidad de clinicas dentales, por lo que "
            "la velocidad de respuesta es el factor decisivo para captar pacientes."
        ),
        "servicios": (
            "- Bot de WhatsApp: atencion automatica 24/7, agendado de citas, confirmaciones y "
            "recordatorios automaticos 24h antes de cada cita.\n"
            "- Precio estimado: $8,000 - $12,000 MXN + retencion $1,800/mes"
        ),
        "msg_wa": (
            "Hola! Vi que Centro Dental Ayon tiene muy buena presencia en Zavaleta. "
            "Un patron comun en clinicas es que los pacientes escriben al WhatsApp fuera "
            "de horario y al dia siguiente ya agendaron en otro lado. Nosotros resolvemos "
            "eso con un sistema que atiende y agenda automaticamente a cualquier hora. "
            "Si quieres te lo muestro funcionando -- 15 minutos esta semana son suficientes. Soy Pablo de Ryventis."
        ),
        "msg_email": (
            "Asunto: Como Centro Dental Ayon puede captar mas pacientes sin contestar cada mensaje\n"
            "Hola equipo de Centro Dental Ayon,\n\n"
            "Vi que actualmente agendan citas por WhatsApp -- algo que funciona bien, pero que tiene un "
            "punto debil: los mensajes que llegan fuera de horario se quedan sin respuesta.\n\n"
            "En Ryventis ayudamos a clinicas dentales en Puebla a implementar un sistema que atiende "
            "automaticamente a cualquier hora, agenda la cita, y envia el recordatorio al paciente el "
            "dia anterior -- sin que el equipo tenga que hacer nada extra.\n\n"
            "El resultado: menos citas perdidas, menos tiempo contestando mensajes, mas pacientes captados.\n\n"
            "Les propongo una llamada de 15 minutos para mostrarles como funciona. Sin compromiso.\n\n"
            "Saludos,\nPablo | Ryventis Solutions | ryventis.mx"
        ),
    },
    {
        "numero": 2,
        "nombre": "DentalEsp",
        "sector": "Clinica Dental",
        "zona": "Santa Cruz Buenavista - Zavaleta",
        "telefono": "222 848 9254 (WA) / 222 403 1199",
        "sitio_web": "dentalesp.com.mx",
        "redes": "Sin redes activas detectadas",
        "calificacion": "Alta",
        "por_que": (
            "Sitio web activo con informacion de servicios pero sin sistema de citas integrado. "
            "Todo el agendado depende de WhatsApp manual o llamada. "
            "Compite directamente con otras clinicas en Zavaleta -- zona de altisima competencia dental. "
            "La diferencia en esta zona se gana en velocidad de respuesta al primer contacto."
        ),
        "servicios": (
            "- Bot de WhatsApp: respuesta inmediata, agendado automatico de citas.\n"
            "- Landing page mejorada con formulario inteligente conectado al bot.\n"
            "- Precio estimado: $10,000 - $15,000 MXN + retencion $2,000/mes"
        ),
        "msg_wa": (
            "Hola! Vi DentalEsp en Zavaleta -- zona con mucha competencia dental. "
            "La diferencia en esa zona suele ganarse en velocidad de respuesta: el paciente que "
            "escribe primero y recibe atencion inmediata, elige esa clinica. Nosotros implementamos "
            "un sistema que responde y agenda al instante, a cualquier hora, sin que el equipo tenga "
            "que estar al pendiente. Te cuento como en 15 minutos esta semana. Soy Pablo de Ryventis."
        ),
        "msg_email": (
            "Asunto: En Zavaleta gana la clinica que responde primero -- te cuento como lograrlo\n"
            "Hola equipo de DentalEsp,\n\n"
            "La zona Zavaleta tiene una de las mayores concentraciones de clinicas dentales en Puebla. "
            "En ese contexto, el factor que mas influye en la decision del paciente es quien responde primero.\n\n"
            "En Ryventis implementamos bots de WhatsApp que responden de forma inmediata, agenda la cita "
            "y envia confirmaciones automaticas -- sin importar la hora.\n\n"
            "Resultado: mas pacientes captados, sin contratar personal adicional.\n\n"
            "Me gustaria mostrarles como funciona en 15 minutos. Disponibles esta semana?\n\n"
            "Saludos,\nPablo | Ryventis Solutions | ryventis.mx"
        ),
    },
    {
        "numero": 3,
        "nombre": "AD Contadores Publicos",
        "sector": "Despacho Contable",
        "zona": "Humboldt Norte, Puebla",
        "telefono": "222 299 6451",
        "sitio_web": "adcontadorespublicos.com",
        "redes": "Sin redes prominentes detectadas",
        "calificacion": "Alta",
        "por_que": (
            "Usa email con dominio Outlook (no profesional), sin chatbot ni respuesta automatica. "
            "Toda la comunicacion con prospectos es reactiva y manual. "
            "Cuando una PYME necesita un contador urgente y no recibe respuesta rapida, "
            "busca al siguiente en la lista. Sin sitio web fuerte ni automatizacion, "
            "pierden clientes de alto valor antes de poder hablar con ellos."
        ),
        "servicios": (
            "- Bot de WhatsApp: primer contacto automatico, calificacion de prospecto (tipo de empresa, "
            "necesidad contable, urgencia).\n"
            "- Landing page profesional con imagen de marca solida.\n"
            "- Precio estimado: $9,000 - $13,000 MXN + retencion $1,500/mes"
        ),
        "msg_wa": (
            "Hola! Vi AD Contadores en Humboldt Norte. Note que todo el contacto va por WhatsApp "
            "y correo -- funciona, pero cuando el volumen de clientes crece, contestar uno por uno "
            "se vuelve un cuello de botella. Nosotros ayudamos a despachos contables a automatizar "
            "ese primer contacto para que el contador se enfoque en el trabajo tecnico, no en "
            "responder mensajes. Te cuento como en 15 minutos. Soy Pablo de Ryventis."
        ),
        "msg_email": (
            "Asunto: Como automatizar el primer contacto con clientes en tu despacho contable\n"
            "Hola equipo de AD Contadores,\n\n"
            "El primer contacto con un prospecto es critico -- si tarda mas de unos minutos, "
            "el cliente ya esta hablando con otro contador.\n\n"
            "En Ryventis implementamos sistemas que responden automaticamente por WhatsApp, "
            "califican el tipo de necesidad contable y agendan una reunion -- sin intervension "
            "manual del contador.\n\n"
            "Adicionalmente, podemos fortalecer su presencia digital con una landing page "
            "profesional que posicione el despacho en busquedas de Google en Puebla.\n\n"
            "Les propongo 15 minutos para mostrarles el sistema en funcionamiento.\n\n"
            "Saludos,\nPablo | Ryventis Solutions | ryventis.mx"
        ),
    },
    {
        "numero": 4,
        "nombre": "Cabanas Servicio Automotriz Integral",
        "sector": "Taller Mecanico",
        "zona": "Centro Historico, Puebla",
        "telefono": "222 364 4055",
        "sitio_web": "tallerdeautospuebla.com",
        "redes": "Sin redes activas detectadas",
        "calificacion": "Alta",
        "por_que": (
            "Su propio sitio web dice explicitamente: 'Llamanos o mandanos un WhatsApp para agendar tu cita' -- "
            "proceso 100% manual y dependiente de que alguien este disponible para contestar. "
            "Sin confirmaciones automaticas, sin recordatorios, sin atencion fuera de horario. "
            "El dolor es visible y documentado en su propia comunicacion digital."
        ),
        "servicios": (
            "- Bot de WhatsApp: agendado automatico de citas, confirmaciones y recordatorios.\n"
            "- Clasificacion de tipo de servicio (afinacion, frenos, suspension, etc.).\n"
            "- Precio estimado: $8,000 - $10,000 MXN + retencion $1,800/mes"
        ),
        "msg_wa": (
            "Hola! Vi la pagina de Cabanas Servicio Automotriz en el Centro de Puebla. "
            "Noto que todo el agendado de citas depende de que alguien conteste el telefono "
            "o WhatsApp. Lo que hacemos en Ryventis es que ese proceso funcione solo -- "
            "el cliente escribe, elige su hora, y tu recibes la cita confirmada sin levantar "
            "el telefono. Te lo muestro en 15 minutos esta semana, sin compromiso. Soy Pablo."
        ),
        "msg_email": (
            "Asunto: Tu taller puede agendar citas automaticamente sin contestar cada mensaje\n"
            "Hola equipo de Cabanas Servicio Automotriz,\n\n"
            "Vi en su pagina que el agendado de citas se hace por WhatsApp o llamada. "
            "Es un sistema que funciona, pero tiene un limite: cuando no hay alguien disponible "
            "para contestar, la cita se pierde.\n\n"
            "En Ryventis implementamos bots que toman el lugar de esa tarea: el cliente escribe, "
            "elige el tipo de servicio y la hora, y la cita queda confirmada automaticamente.\n\n"
            "El taller recibe la agenda llena sin que nadie tenga que estar pendiente del telefono.\n\n"
            "Platiquemos 15 minutos esta semana para mostrarselo en vivo.\n\n"
            "Saludos,\nPablo | Ryventis Solutions | ryventis.mx"
        ),
    },
    {
        "numero": 5,
        "nombre": "Inmobiliaria CC",
        "sector": "Inmobiliaria",
        "zona": "Av. Juarez 1905, Puebla",
        "telefono": "222 120 6655",
        "sitio_web": "Sin sitio web propio -- opera por Facebook",
        "redes": "Facebook: facebook.com/InmoCC",
        "calificacion": "Alta",
        "por_que": (
            "No tiene sitio web propio: todo el pipeline de leads depende del alcance organico de Facebook. "
            "Los clientes que buscan inmobiliarias en Google no los encuentran. "
            "Los leads que llegan por Facebook fuera de horario no reciben respuesta inmediata -- "
            "alta probabilidad de perder compradores potenciales que contactan a varias inmobiliarias a la vez."
        ),
        "servicios": (
            "- Landing page profesional: presencia en Google, formulario de contacto, catalogo de propiedades.\n"
            "- Bot de WhatsApp: respuesta inmediata a leads, calificacion automatica "
            "(tipo de propiedad, presupuesto, zona de interes).\n"
            "- Precio estimado: $12,000 - $18,000 MXN + retencion $2,000/mes"
        ),
        "msg_wa": (
            "Hola! Vi Inmobiliaria CC en Facebook. Tienen buena presencia en redes, pero note que "
            "sin una pagina web propia, los clientes que buscan en Google no los encuentran facilmente -- "
            "y los que llegan al Facebook y escriben de noche se quedan sin respuesta hasta el dia siguiente. "
            "Resolvemos los dos problemas: pagina que posicione en Google y un bot que atienda al instante. "
            "Platiquemos 15 minutos esta semana? Soy Pablo de Ryventis."
        ),
        "msg_email": (
            "Asunto: Como Inmobiliaria CC puede captar leads de Google y atenderlos automaticamente\n"
            "Hola equipo de Inmobiliaria CC,\n\n"
            "Revisando su presencia digital, note dos oportunidades de mejora:\n\n"
            "1. Sin sitio web propio, los compradores que buscan inmobiliarias en Google en Puebla "
            "no los encuentran -- perdiendo trafico organico valioso.\n\n"
            "2. Los leads que llegan por Facebook fuera de horario quedan sin atencion inmediata, "
            "y en inmobiliarias la velocidad de respuesta es critica.\n\n"
            "En Ryventis resolvemos ambos con una landing page profesional + bot de WhatsApp que "
            "califica automaticamente a cada prospecto (presupuesto, zona, tipo de propiedad).\n\n"
            "Les propongo 15 minutos para mostrarles el sistema. Disponibles esta semana?\n\n"
            "Saludos,\nPablo | Ryventis Solutions | ryventis.mx"
        ),
    },
    {
        "numero": 6,
        "nombre": "Servicio Automotriz Nava",
        "sector": "Taller Mecanico",
        "zona": "Vicente Suarez, Puebla",
        "telefono": "221 167 6998",
        "sitio_web": "servicioautomotriznava.com",
        "redes": "Sin redes activas detectadas",
        "calificacion": "Media-Alta",
        "por_que": (
            "Tiene sitio web estatico y atiende solo de lun-sab 9am-7pm. "
            "Fuera de ese horario no hay atencion para nuevas citas. "
            "Calificacion de 4.9 estrellas en Google -- tienen clientes satisfechos pero "
            "pierden oportunidades por no tener atencion automatica fuera de horario."
        ),
        "servicios": (
            "- Bot de WhatsApp: agendado de citas 24/7, confirmaciones automaticas.\n"
            "- Mejora de landing page con llamada a accion directa al bot.\n"
            "- Precio estimado: $8,000 - $11,000 MXN + retencion $1,800/mes"
        ),
        "msg_wa": (
            "Hola! Vi que Servicio Automotriz Nava tiene muy buena reputacion en Puebla -- "
            "4.9 en Google impresiona. Soy Pablo de Ryventis. Notamos que varios talleres en la zona "
            "pierden clientes porque afuera del horario ya no hay quien tome el pedido. Nosotros ayudamos "
            "a talleres como el tuyo a que los clientes agenden solos las 24 horas, sin que tengas que "
            "contestar cada mensaje. Tienes 15 minutos esta semana para que te muestre como funciona?"
        ),
        "msg_email": (
            "Asunto: 4.9 estrellas en Google -- como captar mas clientes incluso fuera de horario\n"
            "Hola equipo de Servicio Automotriz Nava,\n\n"
            "Su calificacion de 4.9 en Google es impresionante -- refleja la calidad de su trabajo.\n\n"
            "El siguiente paso es asegurarse de no perder clientes potenciales que buscan agendar "
            "fuera de su horario de atencion. Actualmente, esos mensajes quedan sin respuesta hasta "
            "el dia siguiente.\n\n"
            "En Ryventis implementamos un sistema que recibe esas solicitudes automaticamente, "
            "agenda la cita y confirma al cliente -- sin importar la hora.\n\n"
            "Les propongo una demostracion de 15 minutos esta semana.\n\n"
            "Saludos,\nPablo | Ryventis Solutions | ryventis.mx"
        ),
    },
    {
        "numero": 7,
        "nombre": "KC Consilium S.C.",
        "sector": "Despacho Contable",
        "zona": "Ladrillera de Benitez, Puebla",
        "telefono": "221 380 8050",
        "sitio_web": "kcconsilium.com",
        "redes": "Facebook e Instagram activos",
        "calificacion": "Media",
        "por_que": (
            "Solo ofrecen formulario estatico y correo para captar clientes nuevos. "
            "Sin respuesta automatica ni calificacion de prospectos. "
            "Tienen presencia en Facebook e Instagram lo que indica que buscan captar clientes digitalmente, "
            "pero no tienen herramienta que cierre ese ciclo con atencion inmediata."
        ),
        "servicios": (
            "- Bot de WhatsApp: primer contacto automatico e inmediato, calificacion de prospecto.\n"
            "- Integracion con su presencia en redes sociales.\n"
            "- Precio estimado: $6,000 - $10,000 MXN + retencion $1,500/mes"
        ),
        "msg_wa": (
            "Hola Karla! Vi KC Consilium -- impresiona que tengan presencia en varios estados. "
            "Noto que la unica forma de contactarlos es el formulario o el correo, que suele ser "
            "lento para una PYME que necesita respuesta el mismo dia. Nosotros ayudamos a despachos "
            "como el tuyo a que el primer contacto sea automatico e inmediato, aunque sea sabado o "
            "fuera de horario. Si te interesa platicamos 15 minutos esta semana. Soy Pablo de Ryventis."
        ),
        "msg_email": (
            "Asunto: Como KC Consilium puede responder a prospectos de forma inmediata, cualquier dia\n"
            "Hola Karla,\n\n"
            "Vi que KC Consilium atiende clientes en varios estados -- eso implica un volumen "
            "considerable de primeros contactos e inquietudes entrantes.\n\n"
            "El reto con formularios y correo es que la respuesta no es inmediata -- y un prospecto "
            "que no recibe respuesta rapida, busca la siguiente opcion.\n\n"
            "En Ryventis implementamos un bot de WhatsApp que responde al instante, cualquier dia, "
            "califica la necesidad del prospecto y agenda la primera reunion -- sin intervension manual.\n\n"
            "Platiquemos 15 minutos esta semana?\n\n"
            "Saludos,\nPablo | Ryventis Solutions | ryventis.mx"
        ),
    },
    {
        "numero": 8,
        "nombre": "Taller Duo Mecanico Puebla",
        "sector": "Taller Mecanico",
        "zona": "Puebla (ubicacion exacta no publicada)",
        "telefono": "222 521 0002",
        "sitio_web": "duomecanicopuebla.com",
        "redes": "Presencia web activa",
        "calificacion": "Media",
        "por_que": (
            "Ya tienen un boton de chat de WhatsApp en su sitio -- lo que muestra que entienden "
            "el valor del canal. Sin embargo el chat va directo a un WhatsApp humano, "
            "sin ninguna automatizacion. Cada conversacion requiere atencion manual para "
            "clasificar el tipo de reparacion, dar presupuesto y confirmar cita."
        ),
        "servicios": (
            "- Upgrade de su WhatsApp actual a bot inteligente con pre-calificacion de servicio.\n"
            "- Flujo automatico: tipo de reparacion -> presupuesto inicial -> confirmacion de cita.\n"
            "- Precio estimado: $8,000 - $10,000 MXN + retencion $1,800/mes"
        ),
        "msg_wa": (
            "Hola! Vi el sitio de Duo Mecanico -- me gusto que ya tienen el chat de WhatsApp. "
            "El siguiente nivel es que ese chat trabaje solo: clasifica el tipo de reparacion, "
            "da presupuesto inicial, y confirma la cita, sin que nadie tenga que estar al pendiente. "
            "En Ryventis hacemos eso en menos de 72 horas. Te cuento como en 15 minutos "
            "si tienes oportunidad esta semana. Soy Pablo."
        ),
        "msg_email": (
            "Asunto: Tu WhatsApp ya casi trabaja solo -- el siguiente paso es completarlo\n"
            "Hola equipo de Duo Mecanico,\n\n"
            "Vi que ya tienen integrado un boton de WhatsApp en su sitio -- eso es un buen paso. "
            "El siguiente nivel es que ese canal funcione completamente solo:\n\n"
            "- Clasifica automaticamente el tipo de reparacion que necesita el cliente.\n"
            "- Da un presupuesto inicial sin necesidad de llamar.\n"
            "- Confirma la cita y la registra en su agenda.\n\n"
            "En Ryventis implementamos ese upgrade en menos de 72 horas, sin cambiar el numero "
            "de WhatsApp que ya tienen.\n\n"
            "Platiquemos 15 minutos esta semana?\n\n"
            "Saludos,\nPablo | Ryventis Solutions | ryventis.mx"
        ),
    },
]


pdf = ProspectosPDF()
pdf.set_auto_page_break(auto=True, margin=18)
pdf.set_margins(0, 0, 0)

# Portada
pdf.add_page()
pdf.set_fill_color(10, 10, 15)
pdf.rect(0, 0, 210, 297, 'F')
pdf.set_fill_color(0, 229, 204)
pdf.rect(0, 0, 210, 4, 'F')
pdf.rect(0, 293, 210, 4, 'F')

pdf.set_y(60)
pdf.set_font('Helvetica', 'B', 36)
pdf.set_text_color(0, 229, 204)
pdf.cell(0, 15, 'RYVENTIS', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('Helvetica', 'B', 36)
pdf.set_text_color(240, 240, 248)
pdf.cell(0, 15, 'SOLUTIONS', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.ln(5)
pdf.set_font('Helvetica', '', 13)
pdf.set_text_color(136, 136, 168)
pdf.cell(0, 8, 'Tecnologia que trabaja para ti', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.ln(20)
pdf.set_fill_color(28, 28, 40)
pdf.rect(30, pdf.get_y(), 150, 40, 'F')
pdf.set_fill_color(0, 229, 204)
pdf.rect(30, pdf.get_y(), 4, 40, 'F')
pdf.set_y(pdf.get_y() + 8)
pdf.set_x(40)
pdf.set_font('Helvetica', 'B', 14)
pdf.set_text_color(240, 240, 248)
pdf.cell(0, 7, 'REPORTE DE PROSPECCION', new_x='LMARGIN', new_y='NEXT')
pdf.set_x(40)
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(136, 136, 168)
pdf.cell(0, 6, '8 Prospectos Calificados | Puebla, Mexico', new_x='LMARGIN', new_y='NEXT')
pdf.set_x(40)
pdf.cell(0, 6, 'Abril 2026 | The Hunter -- Nivel 2', new_x='LMARGIN', new_y='NEXT')

pdf.set_y(200)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(0, 229, 204)
pdf.cell(0, 6, 'SECTORES IDENTIFICADOS', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.ln(4)
sectores = [
    ('Clinicas Dentales', '2 prospectos', (0, 229, 204)),
    ('Talleres Mecanicos', '3 prospectos', (124, 58, 237)),
    ('Despachos Contables', '2 prospectos', (0, 229, 204)),
    ('Inmobiliarias', '1 prospecto', (124, 58, 237)),
]
for sector, cantidad, color in sectores:
    pdf.set_x(50)
    pdf.set_fill_color(*color)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(10, 10, 15)
    pdf.cell(80, 6, f'  {sector}', fill=True, new_x='RIGHT', new_y='LAST')
    pdf.set_fill_color(28, 28, 40)
    pdf.set_text_color(240, 240, 248)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(60, 6, f'  {cantidad}', fill=True, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(1)

# Paginas de prospectos
for p in prospectos:
    pdf.add_page()
    pdf.set_y(28)
    pdf.prospecto_card(
        numero=p["numero"],
        nombre=safe(p["nombre"]),
        sector=safe(p["sector"]),
        zona=safe(p["zona"]),
        telefono=p["telefono"],
        sitio_web=p["sitio_web"],
        redes=safe(p["redes"]),
        pain_point=safe(p.get("pain_point", "")),
        servicios=safe(p["servicios"]),
        calificacion=p["calificacion"],
        por_que=safe(p["por_que"]),
        msg_wa=safe(p["msg_wa"]),
        msg_email=safe(p["msg_email"]),
    )

# Pagina resumen final
pdf.add_page()
pdf.set_fill_color(10, 10, 15)
pdf.rect(0, 0, 210, 297, 'F')
pdf.set_y(28)
pdf.set_font('Helvetica', 'B', 14)
pdf.set_text_color(0, 229, 204)
pdf.cell(0, 8, 'RESUMEN EJECUTIVO -- ORDEN DE CONTACTO', align='C', new_x='LMARGIN', new_y='NEXT')
pdf.ln(4)

prioridades = [
    ('PRIORIDAD 1', 'Centro Dental Ayon', 'Bot WA + recordatorios', '222 323 4235', 'Alta'),
    ('PRIORIDAD 2', 'DentalEsp', 'Bot WA + Landing page', '222 848 9254', 'Alta'),
    ('PRIORIDAD 3', 'AD Contadores Publicos', 'Bot WA + Landing page', '222 299 6451', 'Alta'),
    ('PRIORIDAD 4', 'Cabanas Servicio Automotriz', 'Bot WA', '222 364 4055', 'Alta'),
    ('PRIORIDAD 5', 'Inmobiliaria CC', 'Bot WA + Landing page', '222 120 6655', 'Alta'),
    ('PRIORIDAD 6', 'Servicio Automotriz Nava', 'Bot WA + Landing page', '221 167 6998', 'Media-Alta'),
    ('PRIORIDAD 7', 'KC Consilium S.C.', 'Bot WA', '221 380 8050', 'Media'),
    ('PRIORIDAD 8', 'Taller Duo Mecanico', 'Bot WA calificador', '222 521 0002', 'Media'),
]

for prioridad, nombre, servicio, tel, cal in prioridades:
    pdf.set_x(12)
    if cal == 'Alta':
        pdf.set_fill_color(0, 229, 204)
        pdf.set_text_color(10, 10, 15)
    elif cal == 'Media-Alta':
        pdf.set_fill_color(124, 58, 237)
        pdf.set_text_color(240, 240, 248)
    else:
        pdf.set_fill_color(40, 40, 60)
        pdf.set_text_color(136, 136, 168)
    pdf.set_font('Helvetica', 'B', 7)
    pdf.cell(28, 6, f'  {prioridad}', fill=True, new_x='RIGHT', new_y='LAST')
    pdf.set_fill_color(22, 22, 35)
    pdf.set_text_color(240, 240, 248)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.cell(60, 6, f'  {safe(nombre)}', fill=True, new_x='RIGHT', new_y='LAST')
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(136, 136, 168)
    pdf.cell(60, 6, f'  {servicio}', fill=True, new_x='RIGHT', new_y='LAST')
    pdf.set_text_color(0, 229, 204)
    pdf.cell(0, 6, f'  {tel}', fill=True, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(1)

pdf.ln(8)
pdf.set_x(12)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_text_color(0, 229, 204)
pdf.cell(0, 6, 'ESTRATEGIA DE ACERCAMIENTO:', new_x='LMARGIN', new_y='NEXT')
pdf.ln(2)
estrategia = [
    '1. Iniciar por las 2 clinicas dentales de Zavaleta -- zona con alta competencia, dolor claro y ciclo de decision rapido.',
    '2. Continuar con talleres mecanicos del Centro Historico -- el dolor esta documentado en su propio sitio web.',
    '3. Cerrar con despachos contables -- ciclo de decision ligeramente mas largo pero ticket de retencion alto.',
    '4. Inmobiliaria CC: pitch diferenciado en 2 problemas (visibilidad en Google + atencion de leads).',
]
for punto in estrategia:
    pdf.set_x(14)
    pdf.set_font('Helvetica', '', 8)
    pdf.set_text_color(240, 240, 248)
    pdf.multi_cell(182, 5, safe(punto), new_x='LMARGIN', new_y='NEXT')
    pdf.ln(1)

output_path = r'C:\Agencia Ryventis Solutions\Prospectos_Ryventis_Abril2026.pdf'
pdf.output(output_path)
print(f'PDF generado en: {output_path}')
