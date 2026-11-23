
# ================== PÁGINAS NUEVAS (v8): servicios, equipo, perfiles, legal y blog ==================
import re as _re

def pasos_equipo(final):
    return f'''<ol class="pasos" style="margin-top:22px">
 <li><span class="n">01</span><span class="s"></span><div><h3>Cuéntanos qué necesitas</h3><p>Por el formulario, por teléfono o por WhatsApp: qué te preocupa y tu disponibilidad.</p></div></li>
 <li><span class="n">02</span><span class="s"></span><div><h3>Te ayudamos a encontrar psicóloga</h3><p>Desde la coordinación del equipo te orientamos hacia la profesional más adecuada.</p></div></li>
 <li><span class="n">03</span><span class="s"></span><div><h3>Primer contacto con tu psicóloga</h3><p>Te llama y, si lo necesitas, hacéis una llamada gratuita de 15 minutos para conoceros.</p></div></li>
 <li><span class="n">04</span><span class="s"></span><div><h3>Empiezas tu terapia</h3><p>{final}</p></div></li>
</ol>'''

def lista_check(items, dos=False):
    return f'<ul class="lista-check{" dos-col" if dos else ""}">' + "".join(f'<li>{C}<span>{t}</span></li>' for t in items) + '</ul>'

UBICACION = f'''<section class="bg-blanco rev"><div class="wrap"><div class="dos">
 <div><p class="eyebrow">Dónde estamos</p><h2>Tu espacio de terapia en el centro de Zaragoza<span class="p">.</span></h2>
 <p class="lead" style="margin-top:16px">C. del Coso 98-100, 6ª planta, puerta 5 · 50001 Zaragoza</p>
 <p style="margin-top:12px">Un lugar tranquilo y acogedor donde dedicarte tiempo y hablar con libertad, con atención presencial mediante cita concertada.</p>
 <a class="btn linea" style="margin-top:22px" href="https://www.google.com/maps/search/?api=1&query=Calle+del+Coso+98+Zaragoza">Cómo llegar</a></div>
 <div class="mapa"><iframe title="Mapa de la consulta en el Coso, Zaragoza" loading="lazy" src="https://www.google.com/maps?q=Calle%20del%20Coso%2098%2C%2050001%20Zaragoza&output=embed"></iframe></div>
</div></div></section>'''

def contacto(titulo, texto, origen, extra=""):
    return f'''<section class="bg-pastel decor rev" id="contacto"><div class="wrap"><div class="tarjeta">{amapola_linea(w=150,estilo="right:7%;bottom:34px")}<div class="dos" style="align-items:start">
 <div><p class="eyebrow">Cuéntanos qué necesitas</p><h2>{titulo}<span class="p">.</span></h2>
 <p class="lead" style="margin-top:16px">{texto}</p>{f'<p style="margin-top:12px">{extra}</p>' if extra else ''}
 {DESPUES}
 <p style="margin-top:26px"><span class="resalte">¿Prefieres llamar o escribir?</span></p>
 <p style="font-family:var(--serif);font-size:34px;color:var(--carbon);margin-top:10px"><a href="tel:{TEL}" style="text-decoration:none" data-conv="llamada">{TEL_TXT}</a></p>
 <p style="margin-top:6px"><a class="enlace" href="{WA}" data-conv="whatsapp">Escríbenos por WhatsApp</a></p></div>
 <div>{form(origen)}</div>
</div></div></div></section>'''

def tarifas_cortas(items):
    return '<div class="tarifas" style="grid-template-columns:repeat(%d,1fr);margin-top:30px">' % len(items) + "".join(
        f'<div class="tar{" gratis" if g else ""}" style="{"" if g else "border:1px solid var(--linea)"}"><h3>{t}</h3><div class="precio">{p}</div><p>{d}</p></div>' for t,p,d,g in items) + '</div>'

def servicio(fname, title, desc, path, *, eyebrow, h1, kw, lead, img, alt, nota, sellos, conf, problema_tit, problema_txt, lista_tit, lista, lista_pie="",
             medio_tit, medio_txt, medio_lista=None, equipo_tit, equipo_txt, equipo_keys, paso_final, presencial, precios, faq, contacto_tit, contacto_txt, origen,
             serv_nombre, serv_tipo, area, foto_pos="50% 40%", icon="sofa", extra=""):
    h1_html = h1.replace(kw, subraya(kw), 1)
    body = f'''
<section class="hero bg-crema decor"><div class="wrap">
 <div><p class="eyebrow">{eyebrow}</p><h1>{h1_html}<span class="p">.</span></h1>
 <p class="lead" style="margin-top:28px">{lead}</p>
 <div class="acciones"><a class="btn" href="#contacto" data-conv="cta-hero">Cuéntanos qué necesitas</a><a class="enlace" href="tel:{TEL}" data-conv="llamada">o llama al {TEL_TXT}</a></div>
 <ul class="sellos">{"".join(f"<li>{x}</li>" for x in sellos)}</ul></div>
 {foto_hero(IMG[img], alt, nota[0], nota[1], f"aspect-ratio:4/5;object-position:{foto_pos}", icon=icon)}
</div></section>
{confianza(*conf)}

<section class="bg-pastel rev"><div class="wrap"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">{problema_tit[0]}</p><h2>{problema_tit[1]}<span class="p">.</span></h2>
 {"".join(f'<p style="margin-top:16px">{p}</p>' for p in problema_txt)}</div>
 <div class="tarjeta" style="padding:clamp(26px,3vw,40px)"><h3>{lista_tit}</h3>{lista_check(lista)}{f'<p style="margin-top:18px;font-size:15px">{lista_pie}</p>' if lista_pie else ''}</div>
</div></div></section>

<section class="bg-crema rev"><div class="wrap"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">{medio_tit[0]}</p><h2>{medio_tit[1]}<span class="p">.</span></h2>
 {"".join(f'<p style="margin-top:16px">{p}</p>' for p in medio_txt)}</div>
 <div>{lista_check(medio_lista) if medio_lista else ''}</div>
</div></div></section>
{extra}
{banda("Dar el primer paso también forma parte del proceso<span style='color:var(--amapola)'>.</span>","No tienes que esperar a encontrarte peor para empezar a cuidarte. Cuéntanos qué necesitas y te ayudamos a encontrar el acompañamiento adecuado.","Cuéntanos qué necesitas")}

<section class="bg-crema rev"><div class="wrap">
 <div class="dos" style="align-items:end"><div><p class="eyebrow">Quién te acompaña</p><h2>{equipo_tit}<span class="p">.</span></h2></div><p>{equipo_txt} <a class="enlace" href="equipo.html">Conoce a todo el equipo</a></p></div>
 <div class="equipo" style="grid-template-columns:repeat({len(equipo_keys)},1fr)">{"".join(persona(k) for k in equipo_keys)}</div>
</div></section>

<section class="bg-blanco rev"><div class="wrap"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">Cómo empezar</p><h2>Cuatro pasos, sin complicaciones<span class="p">.</span></h2>{pasos_equipo(paso_final)}</div>
 <div><p class="eyebrow">Precio</p><h2>Sin letra pequeña<span class="p">.</span></h2>{tarifas_cortas(precios)}</div>
</div></div></section>
{UBICACION if presencial else ''}
<section class="bg-crema rev"><div class="wrap" style="max-width:900px">
 <div class="centro"><p class="eyebrow">Preguntas frecuentes</p><h2>Antes de dar el paso<span class="p">.</span></h2></div>{faq_html(faq)}
</div></section>
{contacto(contacto_tit, contacto_txt, origen)}
'''
    sv = {"@type":"Service","name":serv_nombre,"serviceType":serv_tipo,"provider":{"@id":DOM+"/#centro"},"areaServed":area}
    br = {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":DOM+"/"},{"@type":"ListItem","position":2,"name":serv_nombre,"item":DOM+path}]}
    page(fname, title, desc, path, [NEGOCIO, sv, br, faq_schema(faq)], body, active=serv_nombre if False else "", landing=True)

P_IND = [("Llamada informativa","Gratis","15 minutos por teléfono.",True),("Sesión individual","70 €","60 minutos. Bono de 4 sesiones: 260 €.",False)]
P_ONL = [("Llamada informativa","Gratis","15 minutos por teléfono.",True),("Individual online","70 €","60 minutos por videollamada.",False),("Pareja online","90 €","75 minutos por videollamada.",False)]

# ---------- Terapia individual en Zaragoza ----------
servicio("terapia-individual-zaragoza.html","Terapia individual en Zaragoza | Andrea Royo Psicología · Coso 98",
 "Terapia psicológica individual presencial en el centro de Zaragoza (Coso 98-100). Sesiones de 60 minutos por 70 €. Psicólogas sanitarias con distintas especialidades.",
 "/terapia-individual-zaragoza/",
 eyebrow="Psicólogas en el centro de Zaragoza", h1="Terapia individual en Zaragoza", kw="Zaragoza",
 lead="Un espacio para ti. A veces sabemos exactamente qué nos preocupa; otras, simplemente necesitamos parar, hablar y entender qué nos está pasando.",
 img="sillon", alt="Sillón de la consulta de terapia individual en el Coso, Zaragoza", nota=("Consulta en el Coso","Sesiones presenciales de 60 min"), foto_pos="30% 60%",
 sellos=["Sesiones de 60 min · 70 €","Coso 98-100","Llamada gratis de 15 min"], conf=(),
 problema_tit=("Cuándo puede ayudarte","No necesitas esperar a encontrarte peor"),
 problema_txt=["Quizá llevas tiempo acumulando preocupaciones, te cuesta gestionar lo que sientes o estás atravesando una situación que no sabes muy bien cómo afrontar.",
               "No necesitas tener un diagnóstico para acudir a terapia. También puedes venir si quieres conocerte mejor, comprender determinados patrones o dedicar un espacio a tu bienestar emocional."],
 lista_tit="Podemos acompañarte en", lista=["<b>Ansiedad y estrés:</b> preocupaciones constantes o dificultad para desconectar.","<b>Autoestima e inseguridad:</b> autocrítica o dificultad para poner límites.","<b>Estado de ánimo:</b> tristeza persistente, apatía o falta de motivación.","<b>Relaciones personales:</b> conflictos o dependencia emocional.","<b>Duelo y pérdidas</b> o cambios vitales difíciles.","<b>Experiencias traumáticas</b> que siguen afectándote hoy."],
 medio_tit=("Una terapia adaptada a ti","Diferentes especialidades, una misma forma de acompañar"),
 medio_txt=["En Andrea Royo Psicología contamos con psicólogas con diferentes especialidades y enfoques terapéuticos, lo que nos permite ofrecerte un acompañamiento adaptado a tu historia y tus necesidades.",
            "Te ayudaremos a encontrar a la profesional que mejor encaje con tu motivo de consulta y su disponibilidad presencial en Zaragoza."],
 medio_lista=["Un espacio tranquilo en pleno centro de Zaragoza.","Sesiones de 60 minutos, a tu ritmo.","Posibilidad de combinar con sesiones online.","Coordinación del equipo para elegir bien a tu psicóloga."],
 equipo_tit="Psicólogas en la consulta del Coso", equipo_txt="Andrea y Nerea atienden de forma presencial en Zaragoza.", equipo_keys=["andrea","nerea"],
 paso_final="Las sesiones individuales duran 60 minutos y se hacen en nuestra consulta de la calle Coso 98-100.", presencial=True, precios=P_IND,
 faq=[("¿Y si nunca he ido al psicólogo?","No necesitas saber cómo funciona la terapia ni preparar nada especial. Tu psicóloga te explicará cómo será el proceso y podrás plantearle tus dudas."),
      ("¿Puedo combinar terapia presencial y online?","Podemos valorar esa posibilidad en función de tus necesidades y de la disponibilidad de tu psicóloga."),
      ("¿Cuánto dura una sesión y cuánto cuesta?","Las sesiones individuales duran 60 minutos y cuestan 70 € (65 € con el bono de 4 sesiones)."),
      ("¿Cuánto dura un proceso terapéutico?","Dependerá de tu situación, tus objetivos y cómo evolucione el proceso. Cada persona necesita tiempos diferentes.")],
 contacto_tit="Empecemos con una llamada", contacto_txt="Déjanos tu teléfono y te orientamos hacia la psicóloga que mejor encaja contigo.", origen="terapia-individual-zaragoza",
 serv_nombre="Terapia individual en Zaragoza", serv_tipo="Terapia psicológica individual", area="Zaragoza")

# ---------- Terapia online ----------
ONLINE_EXTRA = f'''<section class="bg-blanco rev"><div class="wrap">
 <div class="centro"><p class="eyebrow">Encuentra el acompañamiento que necesitas</p><h2>Terapia online para adultos<span class="p">.</span></h2></div>
 <div class="servicios" style="margin-top:40px">
  <article class="serv"><span class="ico-serv">{ico("portatil")}</span><h3>Terapia individual online</h3><p>Sesiones de 60 minutos por videollamada para trabajar lo que te preocupa, estés donde estés.</p><a class="btn linea" href="#contacto">Terapia individual online</a></article>
  <article class="serv"><span class="ico-serv">{ico("pareja")}</span><h3>Terapia de pareja online</h3><p>Sesiones de 75 minutos por videollamada, también si vivís en ciudades distintas.</p><a class="btn linea" href="terapia-pareja-zaragoza.html">Terapia de pareja online</a></article>
 </div>
</div></section>'''
servicio("terapia-online.html","Terapia psicológica online | Andrea Royo Psicología",
 "Terapia psicológica online en toda España con un equipo de psicólogas sanitarias especializadas. Individual (60 min, 70 €) y de pareja (75 min, 90 €). Llamada gratuita de 15 minutos.",
 "/terapia-online/",
 eyebrow="Psicólogas online · Toda España", h1="Terapia psicológica online", kw="online",
 lead="Un espacio para ti, estés donde estés. Atención cercana y profesional con un equipo de psicólogas especializadas en diferentes áreas.",
 img="escribiendo", alt="Andrea Royo, psicóloga, preparando una sesión de terapia online", nota=("Por videollamada","Individual y de pareja"), foto_pos="40% 70%", icon="portatil",
 sellos=["Individual · 60 min · 70 €","Pareja · 75 min · 90 €","Toda España"], conf=(("100 % online","desde cualquier lugar de España"),"portatil"),
 problema_tit=("Cómo puede ayudarte","No hace falta llegar a un límite para pedir ayuda"),
 problema_txt=["A veces sabemos que algo no va bien, pero no encontramos las palabras para explicarlo. Quizá llevas tiempo sintiéndote desbordada o estás atravesando una etapa complicada.",
               "La terapia puede ayudarte a comprender mejor tus emociones, identificar patrones que influyen en tu bienestar y desarrollar nuevas formas de afrontar lo que estás viviendo. No necesitas tenerlo todo claro antes de empezar."],
 lista_tit="Por qué elegir la terapia online", lista=["<b>Desde donde estés:</b> en casa o en cualquier lugar privado y tranquilo.","<b>Más fácil de organizar:</b> sin desplazamientos, dentro de tu rutina.","<b>Continuidad:</b> si viajas o cambias de ciudad, mantienes a tu psicóloga.","<b>Acceso a especialidades:</b> la profesional que necesitas, vivas donde vivas."],
 medio_tit=("También a través de la pantalla","Lo importante es la confianza con tu psicóloga"),
 medio_txt=["La terapia online puede ser una forma cercana y cómoda de recibir acompañamiento psicológico. Lo importante es construir una relación de confianza con tu psicóloga, también a través de la pantalla.",
            "Solo necesitas un dispositivo con cámara y micrófono, conexión a internet y un lugar privado donde puedas hablar con tranquilidad."],
 medio_lista=None, extra=ONLINE_EXTRA,
 equipo_tit="Un equipo para acompañarte según lo que necesitas", equipo_txt="Te ayudaremos a encontrar a la psicóloga cuyo perfil mejor se adapte a ti.", equipo_keys=ORDEN,
 paso_final="Las sesiones se hacen por videollamada, desde un espacio privado y tranquilo.", presencial=False, precios=P_ONL,
 faq=[("¿La terapia online es tan eficaz como la presencial?","Sí, la terapia online ha demostrado ser igual de efectiva que la presencial cuando existe un buen vínculo terapéutico y un compromiso con el proceso. Además, ofrece flexibilidad y comodidad sin perder calidad."),
      ("¿Qué necesito para hacer terapia online?","Un dispositivo con cámara y micrófono, conexión a internet y un lugar privado donde puedas hablar con tranquilidad."),
      ("¿Puedo hacer terapia online si nunca he ido al psicólogo?","Por supuesto. No necesitas experiencia previa. Tu psicóloga te acompañará desde el principio y podrás plantear todas tus dudas."),
      ("¿Cuánto dura un proceso terapéutico?","Depende de cada persona, de sus necesidades y de sus objetivos. Desde el inicio iremos revisando cómo te sientes para que el proceso tenga sentido y dirección.")],
 contacto_tit="Dar el primer paso también forma parte del proceso", contacto_txt="Estaremos encantadas de escucharte y ayudarte a encontrar el acompañamiento que necesitas.", origen="terapia-online",
 serv_nombre="Terapia psicológica online", serv_tipo="Terapia psicológica online", area="España")

# ---------- Terapia de duelo ----------
servicio("terapia-duelo-zaragoza.html","Terapia de duelo en Zaragoza y online | Andrea Royo Psicología",
 "Psicólogas con formación en duelo en Zaragoza (Coso 98-100) y online: muerte de un ser querido, duelo perinatal, pérdida de una mascota o una ruptura. Llamada gratuita de 15 minutos.",
 "/terapia-duelo-zaragoza/",
 eyebrow="Terapia de duelo · Presencial y online", h1="No tienes que atravesar la pérdida a solas", kw="a solas",
 lead="Perder a alguien o algo importante puede cambiar nuestra manera de sentir, de relacionarnos y de vivir el día a día. Te acompañamos a encontrar una manera de seguir adelante sin tener que olvidar.",
 img="flores", alt="Ramo de flores secas junto a la ventana de la consulta", nota=("Terapia de duelo","En Zaragoza y online"), foto_pos="40% 40%", icon="sofa",
 sellos=["Presencial en Zaragoza u online","Psicólogas con formación en duelo","Llamada gratis de 15 min"], conf=(),
 problema_tit=("Cada pérdida tiene su propia historia","No existe una única forma de vivir el duelo"),
 problema_txt=["Quizá hay momentos en los que el dolor parece insoportable y otros en los que intentas continuar como si nada hubiera pasado. Puede que sientas tristeza, rabia, culpa, vacío o emociones que te cuesta comprender.",
               "No existe un tiempo establecido para dejar de sentir dolor. Sea cual sea tu pérdida, lo que sientes merece ser escuchado y acompañado."],
 lista_tit="Podemos acompañarte si estás viviendo", lista=["La muerte de un ser querido: un familiar, una pareja o una amistad.","Duelo perinatal, tras la pérdida de un embarazo o de tu bebé durante el parto o poco después.","La pérdida de un animal de compañía.","Una ruptura o separación, sobre todo si implica despedirse de un proyecto de vida.","Otros cambios importantes: una enfermedad, una mudanza o una etapa que termina."],
 medio_tit=("Cómo puede ayudarte la terapia","No se trata de olvidar ni de pasar página rápido"),
 medio_txt=["La terapia no busca que olvides a quien has perdido ni que dejes de sentir tristeza. Es un espacio donde expresar lo que estás viviendo, comprender tus emociones y adaptarte a una realidad que ha cambiado.",
            "El objetivo es ayudarte a integrar la pérdida en tu historia y encontrar tu propia manera de continuar."],
 medio_lista=["Dar espacio a las emociones que aparecen tras la pérdida.","Comprender las reacciones que pueden surgir durante el duelo.","Abordar la culpa, los asuntos pendientes o los pensamientos que generan malestar.","Encontrar recursos para los momentos especialmente difíciles.","Reconstruir tu día a día manteniendo un vínculo con lo que has perdido."],
 equipo_tit="Psicólogas con formación en duelo", equipo_txt="Te ayudaremos a encontrar a una psicóloga cuyo perfil se adapte a tu situación y a tu manera de vivir la pérdida.", equipo_keys=["nerea","elena","andrea"],
 paso_final="Las sesiones se hacen por videollamada o en nuestra consulta de Zaragoza, adaptadas a tu historia y a tus necesidades.", presencial=True,
 precios=[("Llamada informativa","Gratis","15 minutos por teléfono.",True),("Sesión individual","70 €","60 minutos, presencial u online.",False)],
 faq=[("¿Y si ha pasado mucho tiempo desde la pérdida?","No existe un plazo para pedir ayuda. Aunque hayan pasado meses o años, puedes acudir a terapia si la pérdida sigue generándote malestar o necesitas un espacio para hablar de ella."),
      ("¿Es normal sentir culpa por empezar a estar mejor?","La culpa puede aparecer durante el duelo, sobre todo cuando sentimos que recuperar el bienestar significa olvidar a quien hemos perdido. En terapia podemos explorar esos sentimientos y lo que significan para ti."),
      ("¿Y si no me siento preparada para hablar de lo ocurrido?","No tienes que contarlo todo desde la primera sesión. Tu psicóloga respetará tus tiempos y te acompañará a tu ritmo."),
      ("¿Puedo ir a terapia por la muerte de mi mascota?","Por supuesto. La pérdida de un animal de compañía puede generar un dolor profundo. Ese vínculo es importante y merece ser reconocido, sin comparaciones ni juicios.")],
 contacto_tit="Estamos aquí para escucharte", contacto_txt="Déjanos tu teléfono y te orientamos hacia una psicóloga con formación en duelo.", origen="terapia-duelo-zaragoza",
 serv_nombre="Terapia de duelo en Zaragoza", serv_tipo="Terapia psicológica de duelo", area=["Zaragoza","España"])

# ---------- Dependencia emocional ----------
servicio("dependencia-emocional-zaragoza.html","Terapia para la dependencia emocional en Zaragoza | Andrea Royo Psicología",
 "Terapia para la dependencia emocional en Zaragoza (Coso 98-100) y online. Aprende a construir relaciones desde la seguridad, sin perderte a ti misma. Llamada gratuita de 15 minutos.",
 "/dependencia-emocional-zaragoza/",
 eyebrow="Terapia psicológica · Presencial en Zaragoza y online", h1="Terapia para la dependencia emocional en Zaragoza", kw="dependencia emocional",
 lead="¿Te cuesta alejarte de alguien aunque sabes que esa relación no te hace bien? La dependencia emocional no significa que haya nada malo en ti.",
 img="nerea", alt="Nerea Rascado, psicóloga que acompaña la dependencia emocional", nota=("Nerea Rascado","Psicóloga sanitaria"), foto_pos="50% 30%", icon="sofa",
 sellos=["Presencial en Zaragoza u online","Sesiones de 60 min · 70 €","Llamada gratis de 15 min"], conf=(),
 problema_tit=("¿Te reconoces?","Quizá sabes que algo no te hace bien, pero no encuentras la manera de cambiarlo"),
 problema_txt=["Puede que tengas mucho miedo a perder a esa persona, que necesites constantemente su atención o aprobación, que te cueste estar sola o que pongas sus necesidades por delante de las tuyas.",
               "Si te reconoces, no significa que seas débil, demasiado sensible o que no sepas estar sola. Quizá estás atravesando un patrón que merece ser comprendido y acompañado."],
 lista_tit="Algunas señales", lista=["Mucho miedo a que tu pareja te deje o deje de quererte.","Necesitas sentir constantemente que te eligen.","Te cuesta estar sola o sientes vacío sin pareja.","Te cuesta decir que no por miedo al rechazo.","Sabes que una relación no te hace bien, pero no consigues alejarte.","Repites relaciones que terminan haciéndote sufrir."],
 medio_tit=("Lo que trabajamos","No necesitas aprender a necesitar menos a los demás"),
 medio_txt=["Necesitas aprender a no perderte a ti misma dentro de una relación. La terapia no consiste en enseñarte a no necesitar a nadie.",
            "Se trata de que puedas construir relaciones desde un lugar de mayor seguridad, sin que tu bienestar dependa completamente de otra persona. Tú marcas el ritmo; tu psicóloga te acompaña."],
 medio_lista=["Entender qué está pasando y por qué se repite.","Volver a escucharte y confiar en tus decisiones.","Aprender a poner límites sin miedo a perder al otro.","Querer a los demás sin dejar de estar de tu lado."],
 equipo_tit="Quién te acompaña", equipo_txt="Nerea cuenta con un Máster en Violencia de Género, que aporta una mirada especializada sobre las dinámicas relacionales. Andrea trabaja la autoestima y la dependencia emocional con perspectiva de trauma.", equipo_keys=["nerea","andrea"],
 paso_final="Sesiones de 60 minutos en nuestra consulta del Coso o por videollamada.", presencial=True, precios=P_IND,
 faq=[("¿Cómo sé si tengo dependencia emocional?","Puede manifestarse como miedo intenso a perder a alguien, dificultad para estar sola, necesidad constante de aprobación, problemas para poner límites o dificultad para alejarte de relaciones que te hacen sufrir. Si te reconoces, podemos explorarlo juntas."),
      ("¿Tengo que dejar a mi pareja para hacer terapia?","No. La terapia no está para decirte si debes continuar o terminar una relación, sino para ayudarte a comprender qué ocurre y decidir desde un lugar de mayor seguridad."),
      ("¿Puedo trabajarla si ahora no tengo pareja?","Sí. También puedes trabajar el miedo a estar sola, la autoestima, los límites y los patrones que se repiten en diferentes relaciones."),
      ("¿La terapia es presencial en Zaragoza?","Las sesiones pueden ser presenciales en nuestra consulta del Coso o por videollamada.")],
 contacto_tit="Podemos empezar por entender qué está pasando", contacto_txt="No tienes que resolverlo todo antes de pedir ayuda. Déjanos tu teléfono y te llamamos.", origen="dependencia-emocional-zaragoza",
 serv_nombre="Terapia para la dependencia emocional", serv_tipo="Terapia psicológica para la dependencia emocional", area=["Zaragoza","España"])

# ---------- Equipo ----------
def tarjeta_equipo(k):
    p=EQUIPO[k]
    return (f'<article class="persona"><a href="{p["url"]}" class="persona-link"><img src="{IMG[p["img"]]}" alt="{p["nombre"]}, psicóloga" style="object-position:{p["pos"]}">'
            f'<h3>{p["nombre"]}</h3><p class="rol">{p["corta"]}</p><p class="mod">{p["modalidad"]}</p><span class="conoce">Conoce a {p["nombre"].split()[0]} →</span></a></article>')
equipo = f'''
<section class="hero bg-crema"><div class="wrap" style="grid-template-columns:1fr">
 <div class="centro" style="max-width:820px;margin:0 auto"><p class="eyebrow">Nuestro equipo</p><h1>Diferentes especialidades, una misma forma de acompañarte<span class="p">.</span></h1>
 <p class="lead" style="margin-top:24px">Sabemos que elegir psicóloga es una decisión importante. No solo buscas formación y experiencia, sino también a una persona con la que sentirte cómoda, escuchada y comprendida.</p></div>
</div></section>
<section class="bg-blanco" style="padding-top:clamp(48px,6vw,80px)"><div class="wrap">
 <p class="centro" style="max-width:62ch;margin:0 auto">Somos un equipo de cuatro psicólogas con diferentes especialidades y enfoques. Compartimos una manera de trabajar cercana, respetuosa y adaptada a cada persona. Queremos ayudarte a encontrar a la profesional que mejor encaje contigo.</p>
 <div class="equipo">{"".join(tarjeta_equipo(k) for k in ORDEN)}</div>
</div></section>
{contacto("Te ayudamos a elegir", "Cuéntanos qué te pasa y, desde la coordinación del equipo, te orientamos hacia la psicóloga que mejor encaja contigo.", "equipo")}
'''
page("equipo.html","Nuestro equipo de psicólogas en Zaragoza | Andrea Royo Psicología",
 "Conoce al equipo de Andrea Royo Psicología: cuatro psicólogas sanitarias especializadas en trauma, pareja y sexología, TOC, fobias, duelo y dificultades emocionales. Zaragoza y online.",
 "/equipo/",[NEGOCIO]+[{"@type":"Person","name":EQUIPO[k]["nombre_largo"],"jobTitle":EQUIPO[k]["titulo"],"worksFor":{"@id":DOM+"/#centro"}} for k in ORDEN],equipo,active="Equipo")

# ---------- Perfiles ----------
for k in ORDEN:
    p=EQUIPO[k]; n1=p["nombre"].split()[0]
    cuerpo = f'''
<section class="hero bg-crema"><div class="wrap">
 <div><p class="migas"><a href="index.html">Inicio</a> · <a href="equipo.html">Equipo</a> · {p["nombre"]}</p>
 <p class="eyebrow">{p["modalidad"]}</p><h1>¡Hola! Soy {n1}<span class="p">.</span></h1>
 <p class="lead" style="margin-top:22px">{p["titulo"]}</p>
 {f'<p style="margin-top:10px;font-size:14px">{p["colegiada"]}</p>' if p["colegiada"] else ''}
 <div class="acciones"><a class="btn" href="#contacto" data-conv="cta-hero">Cuéntanos qué necesitas</a><a class="enlace" href="tel:{TEL}" data-conv="llamada">o llama al {TEL_TXT}</a></div></div>
 <div class="foto-hero">{blob("a",PS)}<img src="{IMG[p["img"]]}" alt="{p["nombre_largo"]}, {p["titulo"].split('.')[0].lower()}" style="aspect-ratio:4/5;object-position:{p["pos"]}"></div>
</div></section>
<section class="bg-pastel rev"><div class="wrap"><div class="tarjeta"><div class="dos" style="align-items:start">
 <div class="prosa">{"".join(f"<p>{x}</p>" for x in p["intro"])}</div>
 <div><h2 style="font-size:clamp(26px,3vw,34px)">¿En qué puedo ayudarte<span class="p">?</span></h2>{lista_check(p["ayuda"])}</div>
</div></div></div></section>
<section class="bg-crema rev"><div class="wrap"><div class="dos" style="align-items:start">
 <div class="prosa"><p class="eyebrow">Mi manera de trabajar</p>{"".join(f"<p>{x}</p>" for x in p["manera"])}</div>
 <div><p class="eyebrow">Mi formación</p><ul class="formacion" style="border-top:0;padding-top:0;margin-top:4px">{"".join(f"<li><b>{x}</b></li>" for x in p["formacion"])}</ul>
 <p style="margin-top:28px;font-size:15px">Puedes trabajar con {n1} en: {" · ".join(f'<a class="enlace" href="{h}">{t}</a>' for h,t in p["enlaces"])}</p></div>
</div></div></section>
{contacto("¿Empezamos?", p["cierre"][0], p["url"].replace(".html",""), p["cierre"][1])}
'''
    page(p["url"], f'{p["nombre"]}, psicóloga · {p["corta"]} | Andrea Royo Psicología',
         f'{p["nombre_largo"]}: {p["titulo"]} {p["modalidad"]}.'[:158], "/"+p["url"].replace(".html","/"),
         [NEGOCIO,{"@type":"Person","name":p["nombre_largo"],"jobTitle":p["titulo"],"knowsAbout":p["ayuda"],"worksFor":{"@id":DOM+"/#centro"}}], cuerpo,
         active="Sobre mí" if k=="andrea" else "Equipo")

# ---------- Legales ----------
def legal_html(f):
    h=(SRC/"legal"/f).read_text()
    h=h.replace('<h1','<h2').replace('</h1>','</h2>')
    h=_re.sub(r'<p><strong>([^<]{3,120})</strong></p>', lambda m: f'<h2>{m.group(1).strip().capitalize()}</h2>', h)
    h=_re.sub(r'<h2>[^<]*</h2>', '', h, count=1)  # el primer título ya va como H1
    return h
for f,tit,slug in [("aviso.html","Aviso legal y condiciones de uso","aviso-legal"),("privacidad.html","Política de privacidad","politica-privacidad"),("cookies.html","Política de cookies","politica-cookies")]:
    cuerpo=f'''<section class="bg-crema"><div class="wrap"><div class="prosa" style="margin:0 auto">
 <p class="migas"><a href="index.html">Inicio</a> · {tit}</p><h1 style="font-size:clamp(36px,5vw,56px)">{tit}<span class="p">.</span></h1>
 {legal_html(f)}</div></div></section>'''
    page(slug+".html", f"{tit} | Andrea Royo Psicología", f"{tit} de www.andrearoyopsicologia.com, titularidad de Andrea Royo Alejandre, psicóloga colegiada A-03988.", "/"+slug+"/", [NEGOCIO], cuerpo)

# ---------- Blog ----------
POSTS=[dict(url="terapia-para-la-ansiedad.html", titulo="Terapia para la ansiedad: síntomas, causas y cómo se trabaja en consulta", corto="Terapia para la ansiedad",
  fecha="2026-03-12", fecha_txt="12 de marzo de 2026", autora="andrea",
  resumen="Qué es la ansiedad, por qué aparece, qué la mantiene en el tiempo y cómo se trabaja en terapia, con un pequeño ejercicio para empezar a entenderla.",
  cuerpo='''<p>La ansiedad es uno de los motivos de consulta más frecuentes en terapia psicológica. Muchas personas buscan ayuda cuando sienten que la preocupación constante, la tensión o el miedo empiezan a interferir en su vida diaria.</p>
<p>Si te preguntas si necesitas terapia para la ansiedad, entender qué te está ocurriendo es el primer paso.</p>
<h2>Síntomas de ansiedad: ¿cómo se manifiesta?</h2><p>La ansiedad puede aparecer de diferentes formas:</p>
<ul><li>Sensación constante de preocupación o anticipación negativa.</li><li>Tensión muscular, presión en el pecho o dificultad para respirar.</li><li>Pensamientos repetitivos que no se detienen.</li><li>Problemas de sueño.</li><li>Irritabilidad o sensación de estar desbordada/o.</li></ul>
<p>En niveles moderados, la ansiedad es una respuesta natural del cuerpo. El problema surge cuando los síntomas se vuelven persistentes y afectan a tu bienestar, tus relaciones o tu trabajo.</p>
<h2>¿Por qué aparece la ansiedad?</h2><p>Desde un enfoque integrador, entendemos que la ansiedad no tiene una única causa. Suele ser el resultado de varios factores:</p>
<ul><li><b>Factores biológicos:</b> un sistema nervioso más sensible a la activación.</li><li><b>Factores psicológicos:</b> autoexigencia, necesidad de control o dificultad para tolerar la incertidumbre.</li><li><b>Experiencias pasadas:</b> vivencias de inseguridad, heridas emocionales o estilos de apego que influyen en la forma de relacionarnos.</li><li><b>Situaciones actuales de estrés:</b> conflictos de pareja, cambios laborales o sobrecarga emocional.</li></ul>
<p>La ansiedad, en muchos casos, es una forma de protección. El problema es que ese mecanismo puede mantenerse activo incluso cuando ya no es necesario.</p>
<h2>¿Qué mantiene la ansiedad en el tiempo?</h2><p>Hay ciertos patrones que refuerzan el malestar:</p>
<ul><li>Evitar aquello que genera miedo.</li><li>Buscar seguridad constante o confirmación externa.</li><li>Anticipar escenarios negativos repetidamente.</li><li>Intentar controlar cada detalle para reducir la incertidumbre.</li></ul>
<p>Paradójicamente, cuanto más intentamos eliminar la ansiedad de forma inmediata, más fuerza puede tomar.</p>
<h2>Tratamiento de la ansiedad en terapia</h2><p>El tratamiento de la ansiedad no consiste únicamente en aplicar técnicas de relajación, aunque pueden formar parte del proceso. En terapia trabajamos de manera más profunda:</p>
<ul><li>Comprendiendo la función que cumple la ansiedad en tu vida.</li><li>Identificando patrones que la activan y la mantienen.</li><li>Regulando el sistema nervioso de forma progresiva.</li><li>Revisando creencias, miedos y autoexigencias.</li><li>Abordando experiencias pasadas que puedan estar influyendo en el presente.</li></ul>
<p>La terapia para la ansiedad busca cambios sostenibles, no soluciones rápidas.</p>
<h2>Un ejercicio para empezar a entender tu ansiedad</h2><p>En lugar de preguntarte «¿cómo hago para que esto desaparezca?», prueba a plantearte:</p>
<ul><li>¿Qué intenta proteger esta ansiedad?</li><li>¿Qué temo que ocurra si dejo de estar en alerta?</li><li>¿Cuándo comenzó a intensificarse?</li></ul>
<p>Este ejercicio no sustituye un proceso terapéutico, pero puede ayudarte a empezar a observar tu ansiedad con mayor conciencia.</p>
<p>Si sientes que la ansiedad está afectando a tu día a día, buscar ayuda profesional puede marcar la diferencia. Si buscas apoyo presencial en Zaragoza o terapia online, puedes <a href="#contacto">escribirnos</a> para una primera llamada informativa.</p>''')]

blog = f'''
<section class="hero bg-crema"><div class="wrap" style="grid-template-columns:1fr">
 <div class="centro" style="max-width:780px;margin:0 auto"><p class="eyebrow">Blog</p><h1>Psicología para entenderte mejor<span class="p">.</span></h1>
 <p class="lead" style="margin-top:22px">Artículos del equipo de Andrea Royo Psicología sobre ansiedad, relaciones, pareja, duelo y bienestar emocional.</p></div>
</div></section>
<section class="bg-blanco" style="padding-top:clamp(48px,6vw,80px)"><div class="wrap"><div class="servicios tres" style="margin-top:0">
 {"".join(f'<a class="post-card" href="{p["url"]}"><span class="fecha">{p["fecha_txt"]}</span><h3>{p["corto"]}</h3><p style="font-size:15.5px">{p["resumen"]}</p><span class="conoce" style="margin-top:auto;font-weight:600;border-bottom:1.5px solid var(--amapola);align-self:flex-start">Leer artículo →</span></a>' for p in POSTS)}
</div></div></section>
{contacto("¿Te has sentido identificada?", "Si algo de lo que lees te resuena, podemos hablar. Déjanos tu teléfono y te llamamos.", "blog")}
'''
page("blog.html","Blog de psicología | Andrea Royo Psicología · Zaragoza","Artículos de psicología del equipo de Andrea Royo Psicología: ansiedad, relaciones, pareja, duelo y bienestar emocional.","/blog/",[NEGOCIO],blog,active="Blog")

for p in POSTS:
    a=EQUIPO[p["autora"]]
    cuerpo=f'''
<section class="bg-crema"><div class="wrap"><article class="prosa" style="margin:0 auto">
 <p class="migas"><a href="index.html">Inicio</a> · <a href="blog.html">Blog</a> · {p["corto"]}</p>
 <p class="eyebrow">{p["fecha_txt"]} · Por <a href="{a["url"]}" style="border:0">{a["nombre"]}</a></p>
 <h1 style="font-size:clamp(36px,5vw,58px)">{p["titulo"]}<span class="p">.</span></h1>
 <p class="lead" style="margin-top:20px">{p["resumen"]}</p>
 {p["cuerpo"]}
 <div style="display:flex;gap:16px;align-items:center;margin-top:46px;padding-top:24px;border-top:1px solid var(--linea)"><img src="{IMG[a["img"]]}" alt="{a["nombre"]}" style="width:64px;height:64px;border-radius:50%;object-fit:cover;object-position:{a["pos"]}"><div><b style="color:var(--carbon)">{a["nombre_largo"]}</b><br><span style="font-size:14px">{a["titulo"]}</span></div></div>
</article></div></section>
{contacto("¿Hablamos?", "Si la ansiedad está afectando a tu día a día, déjanos tu teléfono y te orientamos.", "blog-"+p["url"].replace(".html",""))}
'''
    page(p["url"], f'{p["corto"]} | Blog de Andrea Royo Psicología', p["resumen"][:158], "/"+p["url"].replace(".html","/"),
         [NEGOCIO,{"@type":"BlogPosting","headline":p["titulo"],"datePublished":p["fecha"],"author":{"@type":"Person","name":a["nombre_largo"]},"publisher":{"@id":DOM+"/#centro"}}], cuerpo, active="Blog")
print("nuevas ok")
