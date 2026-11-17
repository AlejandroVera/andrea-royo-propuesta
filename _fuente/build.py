import json, pathlib
SRC = pathlib.Path(__file__).parent
CSS = (SRC/"base.css").read_text()
OUT = SRC/"out"; OUT.mkdir(exist_ok=True)
DOM = "https://andrearoyopsicologia.com"
U = DOM + "/wp-content/uploads/"
IMG = dict(
  logo=U+"2026/02/logo-300x300.png",
  andrea=U+"2026/09/Andrea-1r-1024x1024.jpg",
  consulta=U+"2026/02/1771876307000-1024x768.jpg",
  olga=U+"2026/08/Olga-768x768.jpeg", elena=U+"2026/08/Elena.png", nerea=U+"2026/08/Nerea-768x768.jpeg")
TEL, TEL_TXT = "+34614151736", "614 151 736"

HEAD = '''<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website"><meta property="og:locale" content="es_ES">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{can}"><meta property="og:image" content="{ogimg}">
<meta name="theme-color" content="#FACECA">
<link rel="icon" href="{logo}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Allura&family=Figtree:wght@400;500;600&family=Playfair+Display:wght@500;600&display=swap" rel="stylesheet">
<style>{css}</style>
<script type="application/ld+json">{schema}</script>
</head><body>
<a class="skip" href="#contenido">Saltar al contenido</a>
'''

def header(active="", landing=False):
    links=[("index.html#terapia","Terapia individual"),("terapia-pareja-zaragoza.html","Terapia de pareja"),("index.html#sobre-mi","Sobre mí"),("index.html#equipo","Equipo"),("index.html#tarifas","Tarifas"),("index.html#contacto","Contacto")]
    nav = "" if landing else '<nav class="menu" aria-label="Principal">'+"".join(
        f'<a href="{h}"' + (' aria-current="page"' if t==active else '') + f'>{t}</a>' for h,t in links)+'</nav>'
    tel = f'<a class="tel" href="tel:{TEL}" data-conv="llamada">{TEL_TXT}</a>' if landing else ''
    return f'''<header class="cab"><div class="wrap"><a class="logo" href="index.html"><img src="{IMG['logo']}" alt="Logotipo de Andrea Royo Psicología, una amapola en acuarela"><span>Andrea Royo<small>Psicología · Zaragoza</small></span></a>{nav}{tel}<a class="btn" href="#contacto" data-conv="cta-cabecera">Pedir cita</a></div></header>'''

FOOTER = f'''<footer class="pie"><div class="wrap"><div class="cols">
<div><h4>Andrea Royo Psicología</h4><p>Psicólogas en Zaragoza. Terapia individual, de pareja y sexología, presencial en el Coso y online.</p><p style="margin-top:12px;font-size:13px;opacity:.75">Andrea Royo · Psicóloga General Sanitaria · Nº colegiada [pendiente]</p></div>
<div><h4>Contacto</h4><ul><li>C. del Coso 98-100, 6ª planta, puerta 5</li><li>50001 Zaragoza</li><li><a href="tel:{TEL}">{TEL_TXT}</a></li><li><a href="mailto:psico.andrearoyo@gmail.com">psico.andrearoyo@gmail.com</a></li><li><a href="https://www.instagram.com/hablemosconandrea/">@hablemosconandrea</a></li></ul></div>
<div><h4>Terapia</h4><ul><li><a href="index.html">Psicólogo en Zaragoza</a></li><li><a href="index.html#terapia">Terapia individual</a></li><li><a href="terapia-pareja-zaragoza.html">Terapia de pareja en Zaragoza</a></li><li><a href="index.html#terapia">Dependencia emocional</a></li><li><a href="index.html#terapia">TOC</a></li></ul></div>
</div><div class="legal"><span>© 2026 Andrea Royo Psicología</span><a href="#">Aviso legal</a><a href="#">Privacidad</a><a href="#">Cookies</a></div></div></footer>
<nav class="barra" aria-label="Contacto rápido"><a href="tel:{TEL}" data-conv="llamada">Llamar</a><a class="p" href="#contacto" data-conv="cta-movil">Pedir cita</a></nav>'''

def form(origen, plural=False):
    t = "Os llamamos" if plural else "Te llamamos"
    return f'''<form class="form" id="formulario" novalidate data-origen="{origen}">
<label>Nombre<input name="nombre" autocomplete="given-name" required><span class="err">Escribe tu nombre.</span></label>
<label>Teléfono<input name="telefono" type="tel" inputmode="tel" autocomplete="tel" required pattern="[0-9 +]{{9,15}}"><span class="err">Revisa el teléfono: necesitamos 9 cifras.</span></label>
<label>Modalidad<select name="modalidad"><option>Presencial en Zaragoza</option><option>Online</option><option>Aún no lo sé</option></select></label>
<label>¿Cuándo prefieres la llamada?<select name="franja"><option>Mañanas</option><option>Tardes</option><option>Me da igual</option></select></label>
<label class="full">Cuéntanos en una frase qué te trae (opcional)<textarea name="motivo" rows="3"></textarea></label>
<label class="check full"><input type="checkbox" required><span>He leído y acepto la <a href="#" class="enlace">política de privacidad</a>.</span></label>
<div class="full"><button class="btn" type="submit">Quiero mi llamada gratuita</button></div>
</form>
<div class="ok" id="ok" role="status"><strong style="font-family:var(--serif);font-size:22px">Recibido.</strong><br>{t} en menos de 24 horas laborables.</div>'''

JS = '''<script>
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('vis');io.unobserve(e.target)}}),{threshold:.1});
document.querySelectorAll('.rev').forEach(el=>io.observe(el));
const f=document.getElementById('formulario');
if(f)f.addEventListener('submit',ev=>{ev.preventDefault();let ok=true;
 f.querySelectorAll('input[required]').forEach(i=>{const l=i.closest('label');const v=i.type==='checkbox'?i.checked:(i.checkValidity()&&i.value.trim()!=='');l.classList.toggle('invalid',!v);if(!v)ok=false});
 if(!ok)return; /* En WordPress: formulario de Elementor Pro con redirección a /gracias/ para medir la conversión en Google Ads */
 f.style.display='none';document.getElementById('ok').style.display='block'});
</script></body></html>'''

NEGOCIO = {"@type":["MedicalBusiness","LocalBusiness"],"@id":DOM+"/#centro","name":"Andrea Royo Psicología",
 "description":"Psicólogas en Zaragoza: terapia individual, terapia de pareja y sexología, presencial y online.",
 "url":DOM+"/","image":IMG["consulta"],"logo":IMG["logo"],"telephone":TEL,"email":"psico.andrearoyo@gmail.com","priceRange":"65 €–90 €",
 "address":{"@type":"PostalAddress","streetAddress":"Calle del Coso 98-100, 6ª planta, puerta 5","postalCode":"50001","addressLocality":"Zaragoza","addressRegion":"Aragón","addressCountry":"ES"},
 "areaServed":["Zaragoza","España"],"founder":{"@id":DOM+"/#andrea"},"sameAs":["https://www.instagram.com/hablemosconandrea/"]}
ANDREA = {"@type":"Person","@id":DOM+"/#andrea","name":"Andrea Royo","image":IMG["andrea"],"jobTitle":"Psicóloga General Sanitaria, terapeuta de pareja y sexóloga",
 "alumniOf":["Universidad de Zaragoza","UDIMA","Universidad Isabel I"],"worksFor":{"@id":DOM+"/#centro"}}
def faq_schema(q): return {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":a,"acceptedAnswer":{"@type":"Answer","text":b}} for a,b in q]}
def faq_html(q): return '<div class="faq">'+"".join(f'<details><summary>{a}</summary><p>{b}</p></details>' for a,b in q)+'</div>'

OPS = [("Fue mi primera vez en el psicólogo y ha sido una experiencia positiva que me hizo sentir apoyada y escuchada. La profesionalidad y empatía me hicieron sentir un ambiente cálido y seguro.","Terapia individual"),
 ("Andrea es una excelente psicóloga y persona. Es empática, cercana y las sesiones son reconfortantes.","Terapia individual"),
 ("La consulta ha sido por videollamada pero se ha sentido como en persona.","Terapia online"),
 ("Se le ve muy profesional, se preocupa realmente por tu caso y por poder ayudarte.","Terapia individual"),
 ("Te hace sentir a gusto y cómodo en todo momento. Me siento bien en cada cita.","Terapia individual")]
def opiniones(n=5):
    h='<div class="opiniones">'
    for i,(t,c) in enumerate(OPS[:n]):
        h+=f'<article class="op{" grande" if i==0 else ""}"><div class="est" aria-label="5 de 5 estrellas">★★★★★</div><blockquote>«{t}»</blockquote><cite>{c} · opinión verificada en Doctoralia</cite></article>'
    return h+'</div>'

def page(fname,title,desc,path,graph,body,active="",landing=False):
    schema=json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)
    (OUT/fname).write_text(HEAD.format(title=title,desc=desc,can=DOM+path,ogimg=IMG["consulta"],logo=IMG["logo"],css=CSS,schema=schema)
        +header(active,landing)+'<main id="contenido">'+body+'</main>'+FOOTER+JS)

def cta(tel_txt="o llama al"):
    return f'<div class="acciones"><a class="btn" href="#contacto" data-conv="cta-hero">Pide tu llamada gratuita</a><a class="enlace" href="tel:{TEL}" data-conv="llamada">{tel_txt} {TEL_TXT}</a></div>'

# =============================== INICIO ===============================
FAQ_HOME = [
 ("¿Cómo sé si necesito ir al psicólogo?","No hace falta «estar muy mal». Si algo te preocupa, te duele, se repite o sientes que no consigues gestionarlo sola o solo, es buen momento para pedir ayuda."),
 ("¿Cuánto dura una sesión?","Las sesiones individuales duran entre 50 y 60 minutos; las de pareja, unos 75. Al principio solemos vernos cada semana o cada dos."),
 ("¿Cuánto dura un proceso de terapia?","Depende de lo que te trae y de tus objetivos. En la primera sesión te damos una orientación realista y lo revisamos juntas cada cierto tiempo."),
 ("¿La terapia online funciona igual?","Sí, si tienes un espacio privado y tranquilo. Usamos el mismo enfoque que en consulta y puedes combinar sesiones presenciales y online."),
 ("¿Lo que cuente es confidencial?","Sí. Está protegido por el secreto profesional, con las únicas excepciones que marca la ley ante un riesgo grave para ti o para otras personas."),
 ("¿Y si no sé por dónde empezar?","Llámanos. En 15 minutos gratuitos resolvemos dudas y te orientamos sobre qué psicóloga del equipo encaja mejor contigo."),
]
home = f'''
<section class="hero bg-crema"><div class="wrap">
 <div>
  <p class="eyebrow">Andrea Royo · Psicología en Zaragoza</p>
  <h1>Psicólogas en Zaragoza para volver a ti<span class="p">.</span></h1>
  <span class="raya"></span>
  <p class="lead">Terapia individual y de pareja en el Coso y online. Un espacio cálido, sin juicios y sin prisas, donde adaptamos la terapia a ti, y no al revés.</p>
  {cta()}
  <ul class="sellos"><li><b>★★★★★</b> Doctoralia</li><li>Psicólogas sanitarias</li><li>Desde 65 € la sesión</li></ul>
 </div>
 <div class="foto-hero">
  <img src="{IMG['consulta']}" alt="Andrea Royo, psicóloga en Zaragoza, sentada en su consulta del Coso" style="aspect-ratio:5/6;object-position:72% 50%">
  <div class="nota"><b>Consulta en el Coso</b>Zaragoza centro · también online</div>
 </div>
</div></section>

<section class="bg-pastel rev"><div class="wrap"><div class="tarjeta">
 <div class="dos" style="align-items:start">
  <div><p class="eyebrow">Por qué vienen</p><h2>No hace falta tenerlo claro para empezar<span class="p">.</span></h2></div>
  <div><p class="lead">Quizá llevas tiempo dándole vueltas, te cuesta poner límites o sientes que algo se repite en tu vida. Estos son algunos de los motivos con los que más acompañamos:</p>
  <div class="motivos" style="--x:0"><span style="background:var(--pastel-claro)">Ansiedad</span><span style="background:var(--pastel-claro)">Autoestima</span><span style="background:var(--pastel-claro)">Autoexigencia</span><span style="background:var(--pastel-claro)">Dependencia emocional</span><span style="background:var(--pastel-claro)">Crisis de pareja</span><span style="background:var(--pastel-claro)">Sexualidad y deseo</span><span style="background:var(--pastel-claro)">Duelo y rupturas</span><span style="background:var(--pastel-claro)">Trauma</span><span style="background:var(--pastel-claro)">TOC</span><span style="background:var(--pastel-claro)">Estrés y agotamiento</span></div>
  <p class="mt" style="margin-top:22px">Y si no sabes ponerle nombre a lo que te pasa, también puedes venir. <a class="enlace" href="#contacto">Cuéntanoslo</a></p></div>
 </div>
</div></div></section>

<section class="bg-crema rev" id="terapia"><div class="wrap">
 <div class="centro"><p class="eyebrow">Terapia en Zaragoza y online</p><h2>¿Por dónde quieres empezar<span class="p">?</span></h2></div>
 <div class="servicios">
  <article class="serv">
   <span class="num">01</span><h3>Terapia individual</h3>
   <p>Para entender qué te pasa y cambiarlo poco a poco. Sesiones de 60 minutos, en la consulta del Coso o por videollamada.</p>
   <ul><li>Ansiedad</li><li>Autoestima</li><li>Dependencia emocional</li><li>TOC</li><li>Trauma y duelo</li></ul>
   <a class="btn linea" href="#">Ver terapia individual</a>
  </article>
  <article class="serv destacado">
   <span class="num">02</span><h3>Terapia de pareja y sexología</h3>
   <p>Para cuando cada conversación acaba en la misma discusión, hay distancia o el deseo ha cambiado. Sesiones de 75 minutos.</p>
   <ul><li>Comunicación</li><li>Celos e infidelidad</li><li>Deseo e intimidad</li><li>Decidir si seguir</li></ul>
   <a class="btn linea" href="terapia-pareja-zaragoza.html">Ver terapia de pareja</a>
  </article>
 </div>
</div></section>

<section class="bg-pastel rev" id="sobre-mi"><div class="wrap"><div class="tarjeta">
 <div class="dos">
  <img class="redonda" src="{IMG['andrea']}" alt="Retrato de Andrea Royo, psicóloga sanitaria, terapeuta de pareja y sexóloga en Zaragoza" style="aspect-ratio:1/1">
  <div>
   <p class="eyebrow">Quién te acompaña</p>
   <h2>Soy Andrea Royo<span class="p">.</span></h2>
   <p class="lead" style="margin-top:12px">Psicóloga General Sanitaria, terapeuta de pareja y sexóloga.</p>
   <p style="margin-top:18px">Trabajo desde un enfoque integrador: no aplico un modelo rígido, adapto las herramientas a cada persona. Me importa que entiendas qué mantiene tu malestar —los patrones que se repiten, cómo te relacionas, cómo te tratas— para construir cambios que se queden.</p>
   <p class="script" style="margin-top:22px">Pasito a pasito.</p>
   <ul class="formacion">
    <li><b>Grado en Psicología</b> · Universidad de Zaragoza</li>
    <li><b>Máster en Psicología General Sanitaria</b> · Universidad Isabel I</li>
    <li><b>Máster en Terapia de Pareja y Sexología</b> · UDIMA</li>
    <li><b>Máster en Trauma desde un enfoque integrador</b> · Máster Origen</li>
   </ul>
  </div>
 </div>
</div></div></section>

<section class="bg-crema rev"><div class="wrap"><div class="dos">
 <div>
  <p class="eyebrow">Cómo empezamos</p>
  <h2>Un camino fácil de recorrer<span class="p">.</span></h2>
  <ol class="pasos" style="margin-top:22px">
   <li><span class="n">01</span><span class="s"></span><div><h3>Llamada gratuita</h3><p>15 minutos por teléfono para resolver tus dudas.</p></div></li>
   <li><span class="n">02</span><span class="s"></span><div><h3>Primera sesión</h3><p>Nos cuentas qué te pasa y qué te gustaría cambiar.</p></div></li>
   <li><span class="n">03</span><span class="s"></span><div><h3>Un plan a tu medida</h3><p>Herramientas adaptadas a ti y a tu historia.</p></div></li>
   <li><span class="n">04</span><span class="s"></span><div><h3>A tu ritmo</h3><p>Revisamos juntas cómo te sientes y ajustamos el proceso.</p></div></li>
  </ol>
 </div>
 <div class="foto-hero"><img src="{IMG['consulta']}" alt="Consulta de psicología en el Coso, Zaragoza" style="aspect-ratio:4/5;object-position:22% 50%"></div>
</div></div></section>

<section class="bg-claro rev" id="equipo"><div class="wrap">
 <div class="dos" style="align-items:end"><div><p class="eyebrow">El equipo</p><h2>Cuatro psicólogas, un mismo cuidado<span class="p">.</span></h2></div><p>Si tu caso encaja mejor con otra compañera, te lo diremos en la llamada. Todas somos psicólogas generales sanitarias.</p></div>
 <div class="equipo">
  <article class="persona"><img src="{IMG['andrea']}" alt="Andrea Royo, psicóloga"><h3>Andrea Royo</h3><p class="rol">Pareja · sexología · trauma</p></article>
  <article class="persona"><img src="{IMG['olga']}" alt="Olga Torres, psicóloga"><h3>Olga Torres</h3><p class="rol">Pareja · sexología · EMDR</p></article>
  <article class="persona"><img src="{IMG['elena']}" alt="Elena, psicóloga especializada en TOC"><h3>Elena</h3><p class="rol">TOC · ansiedad · duelo</p></article>
  <article class="persona"><img src="{IMG['nerea']}" alt="Nerea, psicóloga"><h3>Nerea</h3><p class="rol">Terapia individual</p></article>
 </div>
</div></section>

<section class="bg-crema rev"><div class="wrap">
 <p class="eyebrow">Opiniones</p><h2>Lo que cuentan quienes ya han venido<span class="p">.</span></h2>
 {opiniones()}
</div></section>

<section class="bg-azul rev" id="tarifas"><div class="wrap">
 <div class="centro"><p class="eyebrow">Tarifas</p><h2>Precios claros desde el principio<span class="p">.</span></h2></div>
 <div class="tarifas">
  <div class="tar gratis"><h3>Llamada informativa</h3><div class="precio">Gratis</div><p>15 minutos por teléfono para conocernos.</p></div>
  <div class="tar"><h3>Terapia individual</h3><div class="precio">70 € <small>/ sesión</small></div><p>60 minutos, presencial u online.</p></div>
  <div class="tar"><h3>Bono 4 sesiones</h3><div class="precio">260 €</div><p>65 € por sesión. Ahorras 20 €.</p></div>
  <div class="tar"><h3>Terapia de pareja</h3><div class="precio">90 € <small>/ sesión</small></div><p>75 minutos, presencial u online.</p></div>
 </div>
 <p class="centro" style="margin-top:26px;font-size:15px">¿Atraviesas una situación económica difícil? Pregúntanos por la tarifa reducida.</p>
</div></section>

<section class="bg-crema rev"><div class="wrap"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">Preguntas frecuentes</p><h2>Antes de dar el paso<span class="p">.</span></h2>{faq_html(FAQ_HOME)}</div>
 <div>
  <p class="eyebrow">Dónde estamos</p><h2>En pleno centro<span class="p">.</span></h2>
  <p class="lead" style="margin-top:16px">C. del Coso 98-100, 6ª planta, puerta 5 · 50001 Zaragoza</p>
  <div class="mapa" style="margin-top:22px"><iframe title="Mapa de la consulta en el Coso, Zaragoza" loading="lazy" src="https://www.google.com/maps?q=Calle%20del%20Coso%2098%2C%2050001%20Zaragoza&output=embed"></iframe></div>
  <a class="enlace" style="display:inline-block;margin-top:16px" href="https://www.google.com/maps/search/?api=1&query=Calle+del+Coso+98+Zaragoza">Cómo llegar</a>
 </div>
</div></div></section>

<section class="bg-pastel rev" id="contacto"><div class="wrap"><div class="tarjeta"><div class="dos" style="align-items:start">
 <div>
  <p class="eyebrow">Pide cita</p><h2>Empecemos con una llamada<span class="p">.</span></h2>
  <p class="lead" style="margin-top:16px">Déjanos tu teléfono y te llamamos para una conversación gratuita de 15 minutos. Sin compromiso.</p>
  <p style="margin-top:28px"><span class="resalte">¿Prefieres llamar tú?</span></p>
  <p style="font-family:var(--serif);font-size:36px;color:var(--carbon);margin-top:10px"><a href="tel:{TEL}" style="text-decoration:none" data-conv="llamada">{TEL_TXT}</a></p>
  <p style="margin-top:6px">o escríbenos a <a class="enlace" href="mailto:psico.andrearoyo@gmail.com">psico.andrearoyo@gmail.com</a></p>
 </div>
 <div>{form("inicio")}</div>
</div><p class="pie-kit">Buscar apoyo no es una señal de debilidad. Es un paso hacia cuidarte.</p></div></div></section>
'''
page("index.html","Psicólogo en Zaragoza | Andrea Royo Psicología · Coso 98",
 "Psicólogas sanitarias en el centro de Zaragoza. Terapia individual y de pareja, presencial y online. Llamada informativa gratuita de 15 minutos. Desde 65 €.",
 "/",[NEGOCIO,ANDREA,faq_schema(FAQ_HOME)],home)

# =========================== TERAPIA DE PAREJA ===========================
FAQ_P = [
 ("¿Tenemos que estar los dos de acuerdo para empezar?","Lo ideal es que ambos queráis participar. Si uno todavía no está preparado, podemos empezar con un proceso individual."),
 ("¿Sirve si estamos pensando en separarnos?","Sí. Puede ayudaros a reconstruir la relación o a decidir con más claridad y respeto qué queréis hacer."),
 ("¿Y si discutimos constantemente?","Las discusiones que se repiten son uno de los motivos más frecuentes de consulta. Trabajamos qué hay detrás y cómo gestionarlas de otra manera."),
 ("¿Podemos trabajar problemas sexuales?","Sí. Andrea y Olga son sexólogas, así que el deseo, la intimidad y la sexualidad pueden formar parte del proceso."),
 ("¿Cuánto dura y cuánto cuesta una sesión?","Unos 75 minutos y 90 € por sesión. La llamada informativa previa de 15 minutos es gratuita."),
 ("¿Cada cuánto tendremos sesión?","Normalmente cada semana o cada dos semanas, según vuestra situación y objetivos."),
 ("¿Hacéis terapia de pareja online?","Sí, si los dos tenéis un espacio privado. Es útil si vivís en ciudades distintas o tenéis horarios complicados."),
]
pareja = f'''
<section class="hero bg-crema"><div class="wrap">
 <div>
  <p class="eyebrow">Psicóloga de pareja y sexóloga · Coso 98-100</p>
  <h1>Terapia de pareja en Zaragoza<span class="p">.</span></h1>
  <span class="raya"></span>
  <p class="lead">Para cuando siempre acabáis discutiendo por lo mismo. Un espacio para entender qué pasa entre vosotros y aprender a relacionaros de otra manera.</p>
  <div class="acciones"><a class="btn" href="#contacto" data-conv="cta-hero">Pedir llamada gratuita</a><a class="enlace" href="tel:{TEL}" data-conv="llamada">o llama al {TEL_TXT}</a></div>
  <ul class="sellos"><li>Sesiones de 75 min · <b>90 €</b></li><li>Presencial u online</li><li>También sexualidad</li></ul>
 </div>
 <div class="foto-hero"><img src="{IMG['andrea']}" alt="Andrea Royo, terapeuta de pareja y sexóloga en Zaragoza" style="aspect-ratio:5/6"><div class="nota"><b>Andrea Royo</b>Terapeuta de pareja y sexóloga</div></div>
</div></section>

<section class="bg-pastel rev"><div class="wrap"><div class="dos">
 <div><p class="eyebrow">Quizá os suene</p><h2>Os queréis, pero estáis cada vez más lejos<span class="p">.</span></h2>
 <p class="lead" style="margin-top:20px">Si os reconocéis, no significa que lo estéis haciendo mal. Probablemente habéis entrado en un patrón que ya no sabéis cambiar solos.</p></div>
 <ul class="frases">
  <li>«Siempre acabamos teniendo la misma discusión.»</li>
  <li>«Siento que ya no me escucha.»</li>
  <li>«Hablamos, pero nunca llegamos a entendernos.»</li>
  <li>«Nuestra vida sexual ya no es como antes.»</li>
  <li>«No queremos separarnos, pero tampoco seguir así.»</li>
 </ul>
</div></div></section>

<section class="bg-crema rev"><div class="wrap">
 <div class="centro"><p class="eyebrow">Qué trabajamos</p><h2>No se trata de quién tiene razón<span class="p">.</span></h2><span class="raya"></span><p class="lead">Se trata de entender qué está pasando entre vosotros y qué necesita cada uno.</p></div>
 <div class="servicios" style="grid-template-columns:repeat(3,1fr)">
  <article class="serv"><span class="num">01</span><h3>Comunicación</h3><p>Cuando habláis pero no conseguís escucharos ni sentiros comprendidos.</p></article>
  <article class="serv destacado"><span class="num">02</span><h3>Conflictos que se repiten</h3><p>Las mismas discusiones una y otra vez, sin llegar a ninguna solución.</p></article>
  <article class="serv"><span class="num">03</span><h3>Intimidad y deseo</h3><p>Cuando el deseo ha cambiado o tenéis necesidades distintas.</p></article>
  <article class="serv"><span class="num">04</span><h3>Confianza y celos</h3><p>Heridas, distancia o una infidelidad que ha afectado a la relación.</p></article>
  <article class="serv"><span class="num">05</span><h3>Cambios de etapa</h3><p>Hijos, convivencia, boda, familia o decisiones de futuro.</p></article>
  <article class="serv destacado"><span class="num">06</span><h3>Decidir si seguir</h3><p>Un espacio para decidir con claridad y respeto qué queréis hacer.</p></article>
 </div>
 <style>@media(max-width:900px){{.servicios[style]{{grid-template-columns:1fr!important}}}}</style>
</div></section>

<section class="bg-pastel rev"><div class="wrap"><div class="tarjeta"><div class="dos">
 <div><p class="eyebrow">Sexología</p><h2>Y sí, también podemos hablar de sexo<span class="p">.</span></h2>
 <p class="lead" style="margin-top:18px">A veces es más fácil discutir que decir «ya no tengo deseo» o «siento que estamos desconectados».</p>
 <p style="margin-top:14px">El deseo, la intimidad y la forma en que os comunicáis están conectados. Como sexólogas y terapeutas de pareja, os acompañamos también en las dificultades sexuales, sin juicios.</p></div>
 <div><p class="eyebrow">Cómo trabajaremos</p>
 <ol class="pasos">
  <li><span class="n">01</span><span class="s"></span><div><h3>Entender qué pasa</h3><p>Cómo empiezan los conflictos y qué ocurre después.</p></div></li>
  <li><span class="n">02</span><span class="s"></span><div><h3>Ver qué hay debajo</h3><p>Emociones, necesidades y miedos de cada uno.</p></div></li>
  <li><span class="n">03</span><span class="s"></span><div><h3>Cambiar el patrón</h3><p>Nuevas formas de hablaros y de resolver los conflictos.</p></div></li>
 </ol></div>
</div></div></div></section>

<section class="bg-claro rev"><div class="wrap"><div class="dos">
 <div><p class="eyebrow">Quién os acompaña</p><h2>Dos terapeutas de pareja y sexólogas<span class="p">.</span></h2>
 <p style="margin-top:18px">En la llamada gratuita os orientamos sobre quién encaja mejor con vuestra situación y horarios.</p>
 <p class="script" style="margin-top:20px">Escucharos de otra manera.</p></div>
 <div class="equipo" style="grid-template-columns:1fr 1fr;margin-top:0">
  <article class="persona"><img src="{IMG['andrea']}" alt="Andrea Royo, terapeuta de pareja"><h3>Andrea Royo</h3><p class="rol">Máster en Terapia de Pareja y Sexología</p></article>
  <article class="persona"><img src="{IMG['olga']}" alt="Olga Torres, terapeuta de pareja"><h3>Olga Torres</h3><p class="rol">Máster en Sexología y Terapia de Pareja</p></article>
 </div>
</div></div></section>

<section class="bg-azul rev"><div class="wrap"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">Precio</p><h2>Sin letra pequeña<span class="p">.</span></h2>
  <div class="tarifas" style="grid-template-columns:1fr 1fr;margin-top:30px">
   <div class="tar gratis"><h3>Llamada informativa</h3><div class="precio">Gratis</div><p>15 minutos por teléfono.</p></div>
   <div class="tar"><h3>Sesión de pareja</h3><div class="precio">90 €</div><p>75 minutos, presencial en el Coso u online.</p></div>
  </div></div>
 <div><p class="eyebrow">Preguntas frecuentes</p>{faq_html(FAQ_P[:4])}</div>
</div></div></section>

<section class="bg-crema rev"><div class="wrap"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">Más dudas</p>{faq_html(FAQ_P[4:])}</div>
 <div class="opiniones" style="grid-template-columns:1fr;margin-top:0">
  <article class="op grande"><div class="est">★★★★★</div><blockquote>«Andrea es una excelente psicóloga y persona. Es empática, cercana y las sesiones son reconfortantes.»</blockquote><cite>Opinión verificada en Doctoralia</cite></article>
 </div>
</div></div></section>

<section class="bg-pastel rev" id="contacto"><div class="wrap"><div class="tarjeta"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">Hablemos</p><h2>No tenéis que decidir hoy qué pasará<span class="p">.</span></h2>
 <p class="lead" style="margin-top:16px">Solo necesitáis un espacio para empezar a entender qué está pasando. Os llamamos para una conversación gratuita de 15 minutos.</p>
 <p style="margin-top:28px"><span class="resalte">¿Preferís llamar?</span></p>
 <p style="font-family:var(--serif);font-size:36px;color:var(--carbon);margin-top:10px"><a href="tel:{TEL}" style="text-decoration:none" data-conv="llamada">{TEL_TXT}</a></p></div>
 <div>{form("terapia-pareja-zaragoza", plural=True)}</div>
</div></div></div></section>
'''
SERV = {"@type":"Service","name":"Terapia de pareja en Zaragoza","serviceType":"Terapia de pareja y sexología","provider":{"@id":DOM+"/#centro"},
 "areaServed":"Zaragoza","offers":{"@type":"Offer","price":"90","priceCurrency":"EUR","description":"Sesión de 75 minutos"}}
BREAD = {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":DOM+"/"},{"@type":"ListItem","position":2,"name":"Terapia de pareja en Zaragoza","item":DOM+"/terapia-pareja-zaragoza/"}]}
page("terapia-pareja-zaragoza.html","Terapia de pareja en Zaragoza | Andrea Royo Psicología",
 "Terapia de pareja y sexología en el Coso (Zaragoza) y online. Sesiones de 75 minutos por 90 €. Llamada gratuita de 15 minutos para resolver vuestras dudas.",
 "/terapia-pareja-zaragoza/",[NEGOCIO,SERV,BREAD,faq_schema(FAQ_P)],pareja,active="Terapia de pareja",landing=True)
print("ok")
