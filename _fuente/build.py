import json, pathlib
SRC = pathlib.Path(__file__).parent
CSS = (SRC/"base.css").read_text() + (SRC/"extra.css").read_text()
OUT = SRC.parent
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

SERVICIOS=[("index.html#terapia","Terapia individual","Ansiedad, autoestima, duelo, trauma"),
 ("terapia-pareja-zaragoza.html","Terapia de pareja y sexología","Comunicación, conflictos, deseo"),
 ("index.html#terapia","Terapia online","Individual y de pareja, por videollamada"),
 ("index.html#terapia","Dependencia emocional","Relaciones que te hacen daño"),
 ("terapia-toc-online.html","TOC","Con Elena, especialista en TOC")]
OTROS=[("index.html#sobre-mi","Sobre mí"),("index.html#equipo","Equipo"),("index.html#tarifas","Tarifas"),("index.html#contacto","Contacto")]

def header(active="", landing=False):
    cur=lambda t:' aria-current="page"' if t==active else ''
    serv_activo=' activo' if active in [t for _,t,_ in SERVICIOS] else ''
    sub="".join(f'<li><a href="{h}"{cur(t)}><b>{t}</b><span>{d}</span></a></li>' for h,t,d in SERVICIOS)
    nav = f'''<nav class="menu" aria-label="Principal"><div class="desp{serv_activo}"><button type="button" aria-expanded="false" aria-controls="sub-serv">Servicios <svg viewBox="0 0 12 8" aria-hidden="true"><path d="M1 1.5l5 5 5-5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button><ul class="sub" id="sub-serv">{sub}</ul></div>''' + "".join(f'<a href="{h}"{cur(t)}>{t}</a>' for h,t in OTROS) + '</nav>'
    movil = '<details class="menu-movil"><summary aria-label="Abrir menú"><span></span><span></span><span></span></summary><div class="panel"><p class="tit">Servicios</p>' + "".join(f'<a href="{h}">{t}</a>' for h,t,_ in SERVICIOS) + '<p class="tit">Más</p>' + "".join(f'<a href="{h}">{t}</a>' for h,t in OTROS) + f'<a class="btn" href="tel:{TEL}">Llamar al {TEL_TXT}</a></div></details>'
    if landing: nav, movil = "", ""
    tel = f'<a class="tel" href="tel:{TEL}" data-conv="llamada">{TEL_TXT}</a>' if landing else ''
    return f'''<header class="cab"><div class="wrap"><a class="logo" href="index.html"><img src="{IMG['logo']}" alt="Logotipo de Andrea Royo Psicología, una amapola en acuarela"><span>Andrea Royo<small>Psicología · Zaragoza</small></span></a>{nav}{tel}<a class="btn" href="#contacto" data-conv="cta-cabecera">Pedir cita</a>{movil}</div></header>'''

FOOTER = f'''<footer class="pie"><div class="wrap"><div class="cols">
<div><h4>Andrea Royo Psicología</h4><p>Psicólogas en Zaragoza. Terapia individual, de pareja y sexología, presencial en el Coso y online.</p><p style="margin-top:12px;font-size:13px;opacity:.75">Andrea Royo · Psicóloga General Sanitaria · Nº colegiada [pendiente]</p></div>
<div><h4>Contacto</h4><ul><li>C. del Coso 98-100, 6ª planta, puerta 5</li><li>50001 Zaragoza</li><li><a href="tel:{TEL}">{TEL_TXT}</a></li><li><a href="mailto:psico.andrearoyo@gmail.com">psico.andrearoyo@gmail.com</a></li><li><a href="https://www.instagram.com/hablemosconandrea/">@hablemosconandrea</a></li></ul></div>
<div><h4>Terapia</h4><ul><li><a href="index.html">Psicólogo en Zaragoza</a></li><li><a href="index.html#terapia">Terapia individual</a></li><li><a href="terapia-pareja-zaragoza.html">Terapia de pareja en Zaragoza</a></li><li><a href="index.html#terapia">Dependencia emocional</a></li><li><a href="terapia-toc-online.html">Terapia para el TOC online</a></li></ul></div>
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
document.querySelectorAll('.desp button').forEach(b=>{b.addEventListener('click',()=>{const a=b.getAttribute('aria-expanded')==='true';b.setAttribute('aria-expanded',String(!a))});document.addEventListener('click',e=>{if(!b.parentElement.contains(e.target))b.setAttribute('aria-expanded','false')});document.addEventListener('keydown',e=>{if(e.key==='Escape')b.setAttribute('aria-expanded','false')})});
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

# ============================ SVG DE MARCA ============================
AZ, AZH, RJ, PS, CR, CB = "#6EC1E4", "#2B7FA6", "#ED5B4D", "#FACECA", "#FBF6F2", "#3A2F2C"

def petalo(color=RJ):
    return f'<svg viewBox="0 0 40 30" aria-hidden="true"><path d="M3 18C6 6 22 0 34 6c5 3 5 10-1 14-9 6-24 9-30-2z" fill="{color}"/><path d="M8 17c8-3 16-6 24-8" stroke="#fff" stroke-opacity=".35" stroke-width="1.4" fill="none"/></svg>'

def petalos(lista):
    # lista de (left%, top%, tamaño px, rotación, opacidad, color)
    s = ""
    for i,(x,y,t,r,o,c) in enumerate(lista):
        s += f'<span style="position:absolute;left:{x}%;top:{y}%"><svg style="--s:{t}px;--r:{r}deg;--o:{o};--d:{7+i%5*1.3}s;position:static" viewBox="0 0 40 30" aria-hidden="true"><path d="M3 18C6 6 22 0 34 6c5 3 5 10-1 14-9 6-24 9-30-2z" fill="{c}"/><path d="M8 17c8-3 16-6 24-8" stroke="#fff" stroke-opacity=".35" stroke-width="1.4" fill="none"/></svg></span>'
    return f'<div class="petalos" aria-hidden="true">{s}</div>'

PET_HERO = petalos([(3,14,26,-20,.7,RJ),(46,88,18,-35,.55,RJ),(94,8,20,60,.6,RJ)])
PET_BANDA = petalos([(4,18,34,-20,.35,"#fff"),(88,10,26,50,.3,"#fff"),(78,78,40,-40,.3,"#fff"),(40,85,20,10,.25,"#fff"),(60,12,16,80,.25,"#fff")])

def amapola_linea(stroke=CB, centro=RJ, w=160, estilo=""):
    return f'''<svg class="amapola-linea" style="width:{w}px;{estilo}" viewBox="0 0 120 170" fill="none" stroke="{stroke}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M60 62c-9-2-22-1-27-11-5-11 5-22 15-21 3-9 16-13 24-6 9-5 22 0 22 11 10 3 12 16 4 22-4 8-16 8-22 5"/><path d="M48 30c4 6 3 14-2 19M72 24c-2 7 0 14 6 18M50 50c5 6 15 7 22 2"/><circle cx="61" cy="45" r="5.5" fill="{centro}"/><path d="M60 62c0 30-3 60 2 104"/><path d="M60 100c-10-7-20-6-26 0M61 124c9-8 19-9 26-4"/><path d="M34 100c-4 6-2 12 4 14M87 120c5 5 4 12-2 14"/></svg>'''

def blob(cls, color, d="M43.7,-58.1C55.6,-50.1,63.2,-35.4,67.6,-19.8C72,-4.2,73.2,12.3,66.9,25.3C60.6,38.3,46.8,47.8,32.2,55.6C17.6,63.4,2.2,69.5,-14.1,69C-30.4,68.5,-47.6,61.4,-58.5,48.6C-69.4,35.8,-74,17.4,-72.8,-0.1C-71.6,-17.6,-64.6,-35.2,-52.3,-43.6C-40,-52,-20,-51.2,-2.1,-48.4C15.8,-45.6,31.8,-66.1,43.7,-58.1Z"):
    return f'<svg class="blob {cls}" viewBox="-80 -80 160 160" aria-hidden="true"><path d="{d}" fill="{color}"/></svg>'
PUNTOS_SVG = lambda cls: f'<svg class="blob {cls}" viewBox="0 0 100 100" aria-hidden="true">' + "".join(f'<circle cx="{8+c*14}" cy="{8+r*14}" r="2.6" fill="{AZ}"/>' for r in range(7) for c in range(7)) + '</svg>'

def subraya(texto, color=AZ):
    return f'<span class="subraya">{texto}<svg viewBox="0 0 200 20" preserveAspectRatio="none" aria-hidden="true"><path d="M3 13C40 5 90 4 197 9" stroke="{color}" stroke-width="7" stroke-linecap="round" fill="none" opacity=".85"/><path d="M20 17C70 11 130 11 185 14" stroke="{color}" stroke-width="3" stroke-linecap="round" fill="none" opacity=".5"/></svg></span>'

def ola(color, invert=False, fondo="var(--crema)"):
    d = "M0,42 C180,78 360,8 600,30 C840,52 1080,82 1260,48 C1350,32 1400,30 1440,34 L1440,80 L0,80 Z"
    return f'<div class="ola-wrap" style="background:{fondo};{'transform:scaleY(-1)' if invert else ''}"><svg class="ola" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true"><path d="{d}" fill="{color}"/></svg></div>'

# iconos de línea propios (trazo 1.6, azul + toque rojo)
def ico(n, size=None):
    st = f'fill="none" stroke="{AZH}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"'
    p = {
     "estrella": f'<circle cx="24" cy="24" r="22" fill="{"#E6F4FA"}"/><path d="M24 12l3.6 7.6 8.2 1-6 5.7 1.6 8.2L24 30.4l-7.4 4.1 1.6-8.2-6-5.7 8.2-1z" fill="{RJ}" stroke="none"/>',
     "titulo": f'<circle cx="24" cy="24" r="22" fill="#E6F4FA"/><g {st}><path d="M14 30V18l10-5 10 5v12"/><path d="M18 31v-8M24 31v-8M30 31v-8M12 33h24"/></g>',
     "reloj": f'<circle cx="24" cy="24" r="22" fill="#E6F4FA"/><g {st}><circle cx="24" cy="25" r="10"/><path d="M24 19v6l4 3"/><path d="M20 12h8"/></g>',
     "mapa": f'<circle cx="24" cy="24" r="22" fill="#E6F4FA"/><g {st}><path d="M24 35s-9-8.5-9-15a9 9 0 0118 0c0 6.5-9 15-9 15z"/></g><circle cx="24" cy="20" r="3" fill="{RJ}"/>',
     "sofa": f'<g {st}><path d="M10 34v-9a4 4 0 014-4h20a4 4 0 014 4v9"/><path d="M8 27h6v7H8zM34 27h6v7h-6zM14 30h20"/><path d="M12 34v3M36 34v3"/></g><circle cx="24" cy="15" r="4" fill="{RJ}"/>',
     "pareja": f'<g {st}><circle cx="18" cy="16" r="5"/><circle cx="31" cy="16" r="5"/><path d="M9 37c0-6 4-10 9-10s9 4 9 10M22 37c0-6 4-10 9-10s9 4 9 10"/></g><path d="M24.5 9.5c1.2-2 4.2-1.6 4.2.8 0 2-4.2 4.2-4.2 4.2s-4.2-2.2-4.2-4.2c0-2.4 3-2.8 4.2-.8z" fill="{RJ}"/>',
     "portatil": f'<g {st}><rect x="11" y="13" width="26" height="17" rx="2"/><path d="M7 35h34l-3-5H10z"/></g><circle cx="24" cy="21.5" r="3.5" fill="{RJ}"/>',
     "verguenza": f'<circle cx="24" cy="24" r="22" fill="#FDEFED"/><g {st}><circle cx="24" cy="24" r="11"/><path d="M19 28c3 2 7 2 10 0"/><path d="M19.5 21h1M27.5 21h1"/></g><circle cx="17" cy="26" r="2.2" fill="{RJ}" opacity=".5"/><circle cx="31" cy="26" r="2.2" fill="{RJ}" opacity=".5"/>',
     "balanza": f'<circle cx="24" cy="24" r="22" fill="#FDEFED"/><g {st}><path d="M24 12v22M16 34h16M14 17h20"/><path d="M14 17l-4 8h8zM34 17l-4 8h8z"/></g>',
     "agenda": f'<circle cx="24" cy="24" r="22" fill="#FDEFED"/><g {st}><rect x="13" y="14" width="22" height="20" rx="3"/><path d="M13 20h22M19 11v5M29 11v5"/></g><circle cx="24" cy="27" r="2.6" fill="{RJ}"/>',
     "encaje": f'<circle cx="24" cy="24" r="22" fill="#FDEFED"/><g {st}><path d="M14 26l6 6 14-15"/></g>',
     "candado": f'<g {st}><rect x="14" y="22" width="20" height="14" rx="3"/><path d="M18 22v-4a6 6 0 0112 0v4"/></g><circle cx="24" cy="29" r="2" fill="{RJ}"/>',
     "telefono": f'<g {st}><path d="M17 11h-4a2 2 0 00-2 2c0 13 11 24 24 24a2 2 0 002-2v-4l-6-3-3 3c-4-2-7-5-9-9l3-3z"/></g>',
     "check": f'<circle cx="12" cy="12" r="11" fill="{AZ}"/><path d="M7 12.5l3.2 3.2L17 9" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
     "x": f'<circle cx="12" cy="12" r="11" fill="#F3E3DF"/><path d="M8.5 8.5l7 7M15.5 8.5l-7 7" stroke="#B88E86" stroke-width="2" stroke-linecap="round"/>',
    }[n]
    vb = "0 0 24 24" if n in ("check","x") else "0 0 48 48"
    return f'<svg viewBox="{vb}" aria-hidden="true"{f" style=\"width:{size}px;height:{size}px\"" if size else ""}>{p}</svg>'

def foto_hero(src, alt, nota_t, nota_s, estilo="", icon="sofa"):
    return f'''<div class="foto-hero">{blob("a",PS)}
 <img src="{src}" alt="{alt}" style="{estilo}">
 <div class="nota">{ico(icon)}<div><b>{nota_t}</b>{nota_s}</div></div></div>'''

def confianza(ult=("Coso 98-100","Zaragoza centro y online")):
    return f'''<div class="confianza"><div class="wrap"><ul>
 <li>{ico("estrella")}<div><b>Opiniones 5★</b>en Doctoralia</div></li>
 <li>{ico("titulo")}<div><b>4 psicólogas</b>generales sanitarias</div></li>
 <li>{ico("reloj")}<div><b>Respuesta en 24 h</b>llamada gratuita de 15 min</div></li>
 <li>{ico("mapa")}<div><b>{ult[0]}</b>{ult[1]}</div></li>
</ul></div></div>'''

def banda(titulo, texto, boton="Pide tu llamada gratuita"):
    return f'''<section class="banda"><div class="wrap">
 <div><h2>{titulo}</h2><p class="lead" style="color:#FFF1EE;margin-top:14px">{texto}</p></div>
 <div class="acciones"><a class="btn" href="#contacto" data-conv="cta-banda">{boton}</a><a class="enlace" href="tel:{TEL}" data-conv="llamada">o llama al {TEL_TXT}</a></div>
</div></section>'''

DESPUES = f'''<ol class="despues"><li>Rellenas el formulario (1 minuto).</li><li>Te llamamos en menos de 24 horas laborables.</li><li>Resolvemos dudas y, si quieres, buscamos un hueco.</li></ol>
<p class="garantia">{ico("candado")}Sin compromiso. Si no somos la opción adecuada para ti, te orientamos hacia otra profesional.</p>'''

# =============================== INICIO ===============================
FAQ_HOME = [
 ("¿Cómo sé si necesito ir al psicólogo?","No hace falta «estar muy mal». Si algo te preocupa, te duele, se repite o sientes que no consigues gestionarlo sola o solo, es buen momento para pedir ayuda."),
 ("¿Cuánto dura una sesión?","Las sesiones individuales duran entre 50 y 60 minutos; las de pareja, unos 75. Al principio solemos vernos cada semana o cada dos."),
 ("¿Cuánto dura un proceso de terapia?","Depende de lo que te trae y de tus objetivos. En la primera sesión te damos una orientación realista y lo revisamos juntas cada cierto tiempo."),
 ("¿La terapia online funciona igual?","Sí, si tienes un espacio privado y tranquilo. Usamos el mismo enfoque que en consulta y puedes combinar sesiones presenciales y online."),
 ("¿Lo que cuente es confidencial?","Sí. Está protegido por el secreto profesional, con las únicas excepciones que marca la ley ante un riesgo grave para ti o para otras personas."),
 ("¿Y si no sé por dónde empezar?","Llámanos. En 15 minutos gratuitos resolvemos dudas y te orientamos sobre qué psicóloga del equipo encaja mejor contigo."),
]
MOTIVOS = ["Ansiedad","Autoestima","Autoexigencia","Dependencia emocional","Crisis de pareja","Sexualidad y deseo","Duelo y rupturas","Trauma","TOC","Estrés y agotamiento"]

home = f'''
<section class="hero bg-crema decor">{PET_HERO}<div class="wrap">
 <div>
  <p class="eyebrow">Andrea Royo · Psicología en Zaragoza</p>
  <h1>Psicólogas en {subraya("Zaragoza")} para volver a ti<span class="p">.</span></h1>
  <p class="lead" style="margin-top:28px">Terapia individual y de pareja en el Coso y online. Un espacio cálido, sin juicios y sin prisas, donde adaptamos la terapia a ti, y no al revés.</p>
  {cta()}
  <ul class="sellos"><li><b>★★★★★</b> Doctoralia</li><li>Primera llamada gratis</li><li>Desde 65 € la sesión</li></ul>
 </div>
 {foto_hero(IMG['consulta'],"Andrea Royo, psicóloga en Zaragoza, sentada en su consulta del Coso","Consulta en el Coso","Zaragoza centro · también online","aspect-ratio:5/6;object-position:72% 50%")}
</div></section>
{confianza()}

<section class="bg-pastel decor rev">{amapola_linea(w=170,estilo="right:3%;bottom:-10px")}<div class="wrap"><div class="tarjeta">
 <div class="dos" style="align-items:start">
  <div><p class="eyebrow">Por qué vienen</p><h2>No hace falta tenerlo claro para empezar<span class="p">.</span></h2>
  <p style="margin-top:20px">Y si no sabes ponerle nombre a lo que te pasa, también puedes venir. <a class="enlace" href="#contacto">Cuéntanoslo</a></p></div>
  <div><p class="lead">Quizá llevas tiempo dándole vueltas, te cuesta poner límites o sientes que algo se repite en tu vida. Estos son algunos de los motivos con los que más acompañamos:</p>
  <div class="motivos">{"".join(f'<span style="background:var(--pastel-claro)">{m}</span>' for i,m in enumerate(MOTIVOS))}</div></div>
 </div>
</div></div></section>

<section class="bg-crema rev" id="terapia"><div class="wrap">
 <div class="centro"><p class="eyebrow">Terapia en Zaragoza y online</p><h2>¿Por dónde quieres empezar<span class="p">?</span></h2></div>
 <div class="servicios tres">
  <article class="serv">
   <span class="ico-serv">{ico("sofa")}</span><h3>Terapia individual</h3>
   <p>Para entender qué te pasa y cambiarlo poco a poco. Sesiones de 60 minutos en la consulta del Coso.</p>
   <ul><li>Ansiedad</li><li>Autoestima</li><li>Dependencia emocional</li><li><a href="terapia-toc-online.html" style="color:inherit">TOC</a></li><li>Trauma</li></ul>
   <a class="btn linea" href="#">Ver terapia individual</a>
  </article>
  <article class="serv">
   <span class="ico-serv">{ico("pareja")}</span><h3>Terapia de pareja y sexología</h3>
   <p>Para cuando cada conversación acaba en la misma discusión, hay distancia o el deseo ha cambiado. Sesiones de 75 minutos.</p>
   <ul><li>Comunicación</li><li>Celos e infidelidad</li><li>Deseo</li><li>Decidir si seguir</li></ul>
   <a class="btn linea" href="terapia-pareja-zaragoza.html">Ver terapia de pareja</a>
  </article>
  <article class="serv">
   <span class="ico-serv">{ico("portatil")}</span><h3>Terapia online</h3>
   <p>El mismo acompañamiento por videollamada, estés donde estés. Ideal si tienes poco tiempo o vives fuera de Zaragoza.</p>
   <ul><li>Individual</li><li>Pareja</li><li>Combinable con presencial</li></ul>
   <a class="btn linea" href="#">Ver terapia online</a>
  </article>
 </div>
</div></section>

<section class="bg-blanco rev"><div class="wrap">
 <div class="centro"><p class="eyebrow">Lo que suele frenar</p><h2>Es normal tener dudas antes de llamar<span class="p">.</span></h2></div>
 <div class="objeciones">
  <div class="obj">{ico("verguenza")}<div><h3>«Me da vergüenza contarlo»</h3><p>No tienes que contarlo todo el primer día. Vamos a tu ritmo y sin juicios: aquí nada de lo que digas suena raro.</p></div></div>
  <div class="obj">{ico("balanza")}<div><h3>«No sé si lo mío es para tanto»</h3><p>No hace falta estar muy mal para pedir ayuda. Si te preocupa o se repite, merece un espacio.</p></div></div>
  <div class="obj">{ico("agenda")}<div><h3>«No tengo tiempo»</h3><p>Puedes hacer las sesiones online y combinarlas con las presenciales cuando te venga mejor.</p></div></div>
  <div class="obj">{ico("encaje")}<div><h3>«¿Y si no encajo con la psicóloga?»</h3><p>En la llamada gratuita vemos quién del equipo encaja mejor contigo. Y si no somos la opción adecuada, te lo diremos.</p></div></div>
 </div>
</div></section>

<section class="bg-pastel decor rev" id="sobre-mi"><div class="wrap"><div class="tarjeta">
 <div class="dos">
  <div class="foto-hero"><img class="redonda" src="{IMG['andrea']}" alt="Retrato de Andrea Royo, psicóloga sanitaria, terapeuta de pareja y sexóloga en Zaragoza" style="aspect-ratio:1/1"></div>
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
   <li><span class="n">02</span><span class="s"></span><div><h3>Primera sesión</h3><p>Nos cuentas qué te pasa y qué te gustaría cambiar. Sin prisa y sin guion.</p></div></li>
   <li><span class="n">03</span><span class="s"></span><div><h3>Un plan a tu medida</h3><p>Herramientas adaptadas a ti y a tu historia.</p></div></li>
   <li><span class="n">04</span><span class="s"></span><div><h3>A tu ritmo</h3><p>Revisamos juntas cómo te sientes y ajustamos el proceso.</p></div></li>
  </ol>
 </div>
 {foto_hero(IMG['consulta'],"Consulta de psicología en el Coso, Zaragoza","Un espacio tranquilo","6ª planta, con ascensor","aspect-ratio:4/5;object-position:22% 50%",icon="mapa")}
</div></div></section>

{banda("Da el primer paso hoy<span style='color:var(--pastel)'>.</span>","Una llamada de 15 minutos, gratis y sin compromiso. Nos cuentas qué te pasa y te decimos cómo podemos ayudarte.")}

<section class="bg-crema rev" id="equipo"><div class="wrap">
 <div class="dos" style="align-items:end"><div><p class="eyebrow">El equipo</p><h2>Cuatro psicólogas, un mismo cuidado<span class="p">.</span></h2></div><p>Si tu caso encaja mejor con otra compañera, te lo diremos en la llamada. Todas somos psicólogas generales sanitarias.</p></div>
 <div class="equipo">
  <article class="persona"><img src="{IMG['andrea']}" alt="Andrea Royo, psicóloga"><h3>Andrea Royo</h3><p class="rol">Pareja · sexología · trauma</p></article>
  <article class="persona"><img src="{IMG['olga']}" alt="Olga Torres, psicóloga"><h3>Olga Torres</h3><p class="rol">Pareja · sexología · EMDR</p></article>
  <article class="persona"><a href="terapia-toc-online.html" style="text-decoration:none"><img src="{IMG['elena']}" alt="Elena, psicóloga especializada en TOC"><h3>Elena</h3><p class="rol">TOC · ansiedad · duelo</p></a></article>
  <article class="persona"><img src="{IMG['nerea']}" alt="Nerea, psicóloga"><h3>Nerea</h3><p class="rol">Terapia individual</p></article>
 </div>
</div></section>

<section class="bg-crema decor rev"><div class="wrap">
 <p class="eyebrow">Opiniones</p><h2>Lo que cuentan quienes ya han venido<span class="p">.</span></h2>
 <div class="nota-doc"><div><div class="est">★★★★★</div><span style="font-size:14px">Opiniones de pacientes en Doctoralia</span></div></div>
 {opiniones()}
</div></section>

<section class="bg-blanco rev" id="tarifas"><div class="wrap">
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

<section class="bg-pastel decor rev" id="contacto">{amapola_linea(w=140,estilo="left:2%;bottom:20px")}<div class="wrap"><div class="tarjeta"><div class="dos" style="align-items:start">
 <div>
  <p class="eyebrow">Pide cita</p><h2>Empecemos con una llamada<span class="p">.</span></h2>
  <p class="lead" style="margin-top:16px">Déjanos tu teléfono y te llamamos para una conversación gratuita de 15 minutos.</p>
  {DESPUES}
  <p style="margin-top:26px"><span class="resalte">¿Prefieres llamar tú?</span></p>
  <p style="font-family:var(--serif);font-size:36px;color:var(--carbon);margin-top:10px"><a href="tel:{TEL}" style="text-decoration:none" data-conv="llamada">{TEL_TXT}</a></p>
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
C, X = ico("check"), ico("x")
pareja = f'''
<section class="hero bg-crema decor">{PET_HERO}<div class="wrap">
 <div>
  <p class="eyebrow">Psicóloga de pareja y sexóloga · Coso 98-100</p>
  <h1>Terapia de pareja en {subraya("Zaragoza")}<span class="p">.</span></h1>
  <p class="lead" style="margin-top:28px">Para cuando siempre acabáis discutiendo por lo mismo. Un espacio para entender qué pasa entre vosotros y aprender a relacionaros de otra manera.</p>
  <div class="acciones"><a class="btn" href="#contacto" data-conv="cta-hero">Pedir llamada gratuita</a><a class="enlace" href="tel:{TEL}" data-conv="llamada">o llama al {TEL_TXT}</a></div>
  <ul class="sellos"><li>Sesiones de 75 min · <b>90 €</b></li><li>Presencial u online</li><li>También sexualidad</li></ul>
 </div>
 {foto_hero(IMG['andrea'],"Andrea Royo, terapeuta de pareja y sexóloga en Zaragoza","Andrea Royo","Terapeuta de pareja y sexóloga","aspect-ratio:5/6",icon="pareja")}
</div></section>
{confianza()}

<section class="bg-pastel decor rev"><div class="wrap"><div class="dos">
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
 <div class="centro"><p class="eyebrow">Lo que cambia</p><h2>Dejar de dar vueltas en círculo<span class="p">.</span></h2></div>
 <div class="compara">
  <div class="col no"><h3>Si seguís igual</h3><ul>
   <li>{X}<span>La misma discusión vuelve cada pocos días.</span></li>
   <li>{X}<span>Cada uno se siente solo dentro de la relación.</span></li>
   <li>{X}<span>Evitáis hablar de sexo o de lo que duele.</span></li>
   <li>{X}<span>La distancia crece aunque os queráis.</span></li></ul></div>
  <div class="col si"><h3>Con terapia de pareja</h3><ul>
   <li>{C}<span>Entendéis qué hay debajo de cada discusión.</span></li>
   <li>{C}<span>Aprendéis a decir lo que necesitáis sin atacar.</span></li>
   <li>{C}<span>Podéis hablar de deseo e intimidad con calma.</span></li>
   <li>{C}<span>Decidís qué queréis con más claridad.</span></li></ul></div>
 </div>
</div></section>

<section class="bg-crema rev" style="padding-top:0"><div class="wrap">
 <div class="centro"><p class="eyebrow">Qué trabajamos</p><h2>No se trata de quién tiene razón<span class="p">.</span></h2><p class="lead" style="margin-top:18px">Se trata de entender qué está pasando entre vosotros y qué necesita cada uno.</p></div>
 <div class="servicios tres">
  <article class="serv"><span class="num">01</span><h3>Comunicación</h3><p>Cuando habláis pero no conseguís escucharos ni sentiros comprendidos.</p></article>
  <article class="serv"><span class="num">02</span><h3>Conflictos que se repiten</h3><p>Las mismas discusiones una y otra vez, sin llegar a ninguna solución.</p></article>
  <article class="serv"><span class="num">03</span><h3>Intimidad y deseo</h3><p>Cuando el deseo ha cambiado o tenéis necesidades distintas.</p></article>
  <article class="serv"><span class="num">04</span><h3>Confianza y celos</h3><p>Heridas, distancia o una infidelidad que ha afectado a la relación.</p></article>
  <article class="serv"><span class="num">05</span><h3>Cambios de etapa</h3><p>Hijos, convivencia, boda, familia o decisiones de futuro.</p></article>
  <article class="serv"><span class="num">06</span><h3>Decidir si seguir</h3><p>Un espacio para decidir con claridad y respeto qué queréis hacer.</p></article>
 </div>
</div></section>

{banda("Vuestra relación merece una conversación distinta<span style='color:var(--pastel)'>.</span>","15 minutos gratis por teléfono para resolver dudas y ver si podemos ayudaros.","Pedir llamada gratuita")}

<section class="bg-pastel decor rev"><div class="wrap"><div class="tarjeta"><div class="dos">
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

<section class="bg-blanco rev"><div class="wrap">
 <div class="centro"><p class="eyebrow">Dudas habituales</p><h2>Lo que muchas parejas se preguntan antes de venir<span class="p">.</span></h2></div>
 <div class="objeciones">
  <div class="obj">{ico("pareja")}<div><h3>«Mi pareja no quiere venir»</h3><p>Es más común de lo que parece. Podemos empezar contigo y ver juntos cómo plantearlo.</p></div></div>
  <div class="obj">{ico("balanza")}<div><h3>«¿Y si la terapeuta se pone de un lado?»</h3><p>No buscamos culpables. Nuestro trabajo es entender la relación, no dar la razón a nadie.</p></div></div>
  <div class="obj">{ico("reloj")}<div><h3>«Ya es tarde para nosotros»</h3><p>Nunca es tarde para entender qué ha pasado, tanto si decidís seguir como si no.</p></div></div>
  <div class="obj">{ico("verguenza")}<div><h3>«Nos da vergüenza hablar de sexo»</h3><p>Somos sexólogas: es un tema más. Iremos al ritmo que os resulte cómodo.</p></div></div>
 </div>
</div></section>

<section class="bg-crema rev"><div class="wrap"><div class="dos">
 <div><p class="eyebrow">Quién os acompaña</p><h2>Dos terapeutas de pareja y sexólogas<span class="p">.</span></h2>
 <p style="margin-top:18px">En la llamada gratuita os orientamos sobre quién encaja mejor con vuestra situación y horarios.</p>
 <div class="nota-doc"><div><div class="est">★★★★★</div><span style="font-size:14px">Opiniones de pacientes en Doctoralia</span></div></div>
 <p class="script" style="margin-top:20px">Escucharos de otra manera.</p></div>
 <div class="equipo" style="grid-template-columns:1fr 1fr;margin-top:0">
  <article class="persona"><img src="{IMG['andrea']}" alt="Andrea Royo, terapeuta de pareja"><h3>Andrea Royo</h3><p class="rol">Máster en Terapia de Pareja y Sexología</p></article>
  <article class="persona"><img src="{IMG['olga']}" alt="Olga Torres, terapeuta de pareja"><h3>Olga Torres</h3><p class="rol">Máster en Sexología y Terapia de Pareja</p></article>
 </div>
</div></div></section>

<section class="bg-crema rev"><div class="wrap"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">Precio</p><h2>Sin letra pequeña<span class="p">.</span></h2>
  <div class="tarifas" style="grid-template-columns:1fr 1fr;margin-top:30px">
   <div class="tar gratis"><h3>Llamada informativa</h3><div class="precio">Gratis</div><p>15 minutos por teléfono.</p></div>
   <div class="tar" style="border:1px solid var(--linea)"><h3>Sesión de pareja</h3><div class="precio">90 €</div><p>75 minutos, presencial en el Coso u online.</p></div>
  </div>
  <p class="garantia">{ico("portatil")}¿Vivís en ciudades distintas? También hacemos terapia de pareja online.</p></div>
 <div><p class="eyebrow">Preguntas frecuentes</p>{faq_html(FAQ_P)}</div>
</div></div></section>

<section class="bg-pastel decor rev" id="contacto">{amapola_linea(w=140,estilo="left:2%;bottom:20px")}<div class="wrap"><div class="tarjeta"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">Hablemos</p><h2>No tenéis que decidir hoy qué pasará<span class="p">.</span></h2>
 <p class="lead" style="margin-top:16px">Solo necesitáis un espacio para empezar a entender qué está pasando.</p>
 {DESPUES}
 <p style="margin-top:26px"><span class="resalte">¿Preferís llamar?</span></p>
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

# =============================== TOC ===============================
def ciclo_toc():
    nodos=[(260,74,"Pensamiento","intrusivo",RJ,(260,30),(260,50)),(440,220,"Ansiedad","y duda",AZ,(440,256),(440,276)),
           (260,366,"Compulsión","comprobar, preguntar…",RJ,(260,404),(260,424)),(80,220,"Alivio","que dura poco",AZ,(80,256),(80,276))]
    g=""
    for x,y,t,s2,c,(tx,ty),(sx,sy) in nodos:
        g+=f'<g><circle cx="{x}" cy="{y}" r="9" fill="{c}"/><text class="t" x="{tx}" y="{ty}" text-anchor="middle">{t}</text><text x="{sx}" y="{sy}" text-anchor="middle" opacity=".8">{s2}</text></g>'
    flechas=''.join(f'<path d="{d}" fill="none" stroke="{CB}" stroke-width="1.4" stroke-dasharray="2 7" stroke-linecap="round" marker-end="url(#pf)"/>' for d in [
      "M282 80 C370 100 422 150 436 196","M434 300 C412 340 360 362 290 368","M230 368 C160 362 110 340 86 300","M84 196 C98 150 150 100 238 80"])
    return f'''<svg class="ciclo" viewBox="0 0 520 440" role="img" aria-label="El círculo del TOC: pensamiento intrusivo, ansiedad y duda, compulsión, alivio que dura poco, y vuelta a empezar">
<defs><marker id="pf" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1l7 4-7 4" fill="none" stroke="{CB}" stroke-width="1.4"/></marker></defs>
<circle cx="260" cy="220" r="96" fill="{PS}" opacity=".55"/>
<text class="t" x="260" y="214" text-anchor="middle">El círculo</text><text class="t" x="260" y="240" text-anchor="middle">del TOC<tspan fill="{RJ}">.</tspan></text>
{flechas}{g}</svg>'''

FAQ_T = [
 ("¿Qué es el TOC?","El trastorno obsesivo-compulsivo combina pensamientos, imágenes o dudas que aparecen sin querer y generan mucho malestar (obsesiones) con conductas o rituales mentales para calmarlo (compulsiones), como comprobar, preguntar, repasar o evitar."),
 ("¿El TOC se puede tratar?","Sí. Responde bien a la terapia psicológica. Trabajamos para que puedas tolerar la duda sin tener que responder a ella con compulsiones, y así el TOC va perdiendo fuerza."),
 ("¿Tengo que contar mis pensamientos aunque me den miedo?","Solo cuando te sientas preparado/a. Elena está acostumbrada a escuchar pensamientos intrusivos de todo tipo: tener un pensamiento no dice nada de quién eres."),
 ("¿La terapia online sirve para el TOC?","Sí. Las sesiones por videollamada permiten trabajar desde un espacio privado, sin desplazamientos, y practicar entre sesiones en tu propio entorno."),
 ("¿Necesito un diagnóstico para pedir cita?","No. Si te reconoces en lo que lees aquí, basta con la llamada gratuita: valoramos juntos qué te pasa y si este enfoque encaja contigo."),
 ("¿Cuánto cuesta y cuánto dura una sesión?","Cada sesión individual dura unos 60 minutos y cuesta 70 € (65 € con el bono de 4 sesiones). La llamada de valoración de 15 minutos es gratuita."),
]
TIPOS_TOC=["Comprobación","Contaminación y limpieza","Pensamientos intrusivos","TOC relacional","Orden y simetría","Rumiación y dudas","TOC de daño","Necesidad de certeza"]

toc = f'''
<section class="hero bg-crema decor">{PET_HERO}<div class="wrap">
 <div>
  <p class="eyebrow">Psicóloga especializada en TOC · Online</p>
  <h1>Terapia para el {subraya("TOC")} online<span class="p">.</span></h1>
  <p class="lead" style="margin-top:28px">Cuando tu mente no deja de buscar certezas. Te ayudamos a dejar de vivir pendiente de las dudas y a recuperar, poco a poco, espacio para tu vida.</p>
  <div class="acciones"><a class="btn" href="#contacto" data-conv="cta-hero">Pedir valoración gratuita</a><a class="enlace" href="tel:{TEL}" data-conv="llamada">o llama al {TEL_TXT}</a></div>
  <ul class="sellos"><li>Especializada en TOC</li><li>Sesiones por videollamada</li><li>Valoración gratis · <b>15 min</b></li></ul>
 </div>
 {foto_hero(IMG['elena'],"Elena, psicóloga sanitaria especializada en el tratamiento del TOC","Elena","Psicóloga especializada en TOC","aspect-ratio:5/6",icon="portatil")}
</div></section>
{confianza(("100 % online","sesiones por videollamada"))}

<section class="bg-pastel decor rev">{amapola_linea(w=140,estilo="right:2%;bottom:-6px")}<div class="wrap"><div class="dos">
 <div><p class="eyebrow">Quizá te pase</p><h2>Estás cansado/a de darle tantas vueltas<span class="p">.</span></h2>
 <p class="lead" style="margin-top:20px">Lo agotador no es solo tener esos pensamientos. Es sentir que necesitas resolverlos para poder estar tranquilo/a.</p>
 <div class="motivos">{"".join(f'<span>{t}</span>' for t in TIPOS_TOC)}</div></div>
 <ul class="frases">
  <li>«Lo compruebo una vez más y ya está.»</li>
  <li>«Necesito que me digas que no pasa nada.»</li>
  <li>«Busco en internet hasta quedarme tranquilo/a.»</li>
  <li>«Repaso la conversación una y otra vez.»</li>
  <li>«¿Y si ese pensamiento dice algo de mí?»</li>
 </ul>
</div></div></section>

<section class="bg-crema rev"><div class="wrap"><div class="dos">
 <div><p class="eyebrow">Por qué no se va</p><h2>Cada vez que respondes a la duda, vuelve con más fuerza<span class="p">.</span></h2>
 <p style="margin-top:18px">Comprobar, preguntar o analizar alivia durante un rato. Pero ese alivio le enseña a tu mente que la duda era peligrosa, y la duda vuelve. Por eso intentar convencerte de que «no significa nada» no suele funcionar.</p>
 <p style="margin-top:14px">En terapia no se trata de controlar cada pensamiento, sino de <span class="resalte" style="padding:0 8px">romper el círculo</span>.</p></div>
 <div>{ciclo_toc()}</div>
</div></div></section>

<section class="bg-blanco rev"><div class="wrap">
 <div class="centro"><p class="eyebrow">Lo que cambia</p><h2>Recuperar espacio para tu vida<span class="p">.</span></h2></div>
 <div class="compara">
  <div class="col no"><h3>Si sigues igual</h3><ul>
   <li>{X}<span>Las comprobaciones ocupan cada vez más tiempo.</span></li>
   <li>{X}<span>Necesitas que otros te tranquilicen una y otra vez.</span></li>
   <li>{X}<span>Evitas lugares, personas o situaciones.</span></li>
   <li>{X}<span>La duda decide por ti.</span></li></ul></div>
  <div class="col si"><h3>Con terapia para el TOC</h3><ul>
   <li>{C}<span>Entiendes cómo funciona tu TOC y qué lo mantiene.</span></li>
   <li>{C}<span>Aprendes a convivir con la duda sin obedecerla.</span></li>
   <li>{C}<span>Las compulsiones pierden fuerza poco a poco.</span></li>
   <li>{C}<span>Vuelves a hacer planes sin pedirle permiso al TOC.</span></li></ul></div>
 </div>
</div></section>

{banda("Antes de empezar, podemos hablar<span style='color:var(--amapola)'>.</span>","Una llamada de valoración de 15 minutos, gratis y sin compromiso. Nos cuentas qué te pasa y vemos si este enfoque encaja contigo.","Pedir valoración gratuita")}

<section class="bg-pastel rev"><div class="wrap"><div class="tarjeta"><div class="dos">
 <div class="foto-hero">{blob("a",PS)}<img class="redonda" src="{IMG['elena']}" alt="Retrato de Elena, psicóloga especializada en TOC" style="aspect-ratio:1/1"></div>
 <div>
  <p class="eyebrow">Al otro lado</p>
  <h2>Soy Elena<span class="p">.</span></h2>
  <p class="lead" style="margin-top:12px">Psicóloga General Sanitaria, especializada en el tratamiento del trastorno obsesivo-compulsivo.</p>
  <p style="margin-top:18px">Sé que hay pensamientos que dan miedo incluso de contar en voz alta. Y que, si ya has hecho terapia sin sentir que avanzabas, cuesta volver a confiar en que las cosas pueden cambiar. No se trata de aprender a controlar cada pensamiento, sino de dejar de vivir pendiente de ellos.</p>
  <p class="script" style="margin-top:22px">Te acompaño a cuidar de ti.</p>
  <ul class="formacion">
   <li><b>Grado en Psicología</b> · Universidad Miguel Hernández</li>
   <li><b>Doble Máster en Psicología General Sanitaria y Neuropsicología</b> · Universidad de Lleida</li>
   <li><b>Máster en Psicoterapia Integradora</b> · Método Atlas</li>
   <li><b>Terapias contextuales</b> · Universidad de Almería · <b>EMDR</b> nivel I</li>
  </ul>
 </div>
</div></div></div></section>

<section class="bg-crema rev"><div class="wrap"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">Cómo trabajaremos</p><h2>Paso a paso, para que el TOC ocupe menos<span class="p">.</span></h2>
 <ol class="pasos" style="margin-top:22px">
  <li><span class="n">01</span><span class="s"></span><div><h3>Entender qué está pasando</h3><p>Cómo funciona tu TOC, qué lo activa y qué haces para sentirte seguro/a.</p></div></li>
  <li><span class="n">02</span><span class="s"></span><div><h3>Romper el círculo</h3><p>Identificamos lo que te alivia en el momento pero mantiene el TOC.</p></div></li>
  <li><span class="n">03</span><span class="s"></span><div><h3>Empezar a hacerlo diferente</h3><p>Nuevas formas de relacionarte con la duda y la ansiedad, a tu ritmo.</p></div></li>
 </ol></div>
 <div><p class="eyebrow">Por qué online</p><h2>Un espacio terapéutico, estés donde estés<span class="p">.</span></h2>
 <ul class="col si" style="margin-top:26px;list-style:none;display:grid;gap:12px">
  <li style="display:grid;grid-template-columns:22px 1fr;gap:10px">{C}<span>Sin desplazamientos ni salas de espera.</span></li>
  <li style="display:grid;grid-template-columns:22px 1fr;gap:10px">{C}<span>Desde un espacio conocido y privado.</span></li>
  <li style="display:grid;grid-template-columns:22px 1fr;gap:10px">{C}<span>Más fácil de encajar en tu rutina.</span></li>
  <li style="display:grid;grid-template-columns:22px 1fr;gap:10px">{C}<span>Practicas lo aprendido en tu propio entorno.</span></li>
 </ul></div>
</div></div></section>

<section class="bg-blanco rev"><div class="wrap">
 <div class="centro"><p class="eyebrow">Dudas habituales</p><h2>Lo que muchas personas con TOC se preguntan<span class="p">.</span></h2></div>
 <div class="objeciones">
  <div class="obj">{ico("verguenza")}<div><h3>«Me da miedo contar lo que pienso»</h3><p>Los pensamientos intrusivos no dicen nada de quién eres. Aquí puedes contarlos sin juicio, cuando estés preparado/a.</p></div></div>
  <div class="obj">{ico("reloj")}<div><h3>«Ya hice terapia y no avancé»</h3><p>El TOC necesita un abordaje específico. Trabajarás con una psicóloga especializada en él.</p></div></div>
  <div class="obj">{ico("portatil")}<div><h3>«¿De verdad funciona online?»</h3><p>Sí. Además, te permite practicar en los lugares donde aparece el TOC en tu día a día.</p></div></div>
  <div class="obj">{ico("balanza")}<div><h3>«¿Y si lo mío no es TOC?»</h3><p>Lo valoramos en la llamada gratuita. Si no es lo que necesitas, te orientamos.</p></div></div>
 </div>
</div></section>

<section class="bg-crema rev"><div class="wrap"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">Precio</p><h2>Sin letra pequeña<span class="p">.</span></h2>
  <div class="tarifas" style="grid-template-columns:1fr 1fr;margin-top:30px">
   <div class="tar gratis"><h3>Llamada de valoración</h3><div class="precio">Gratis</div><p>15 minutos por teléfono.</p></div>
   <div class="tar" style="border:1px solid var(--linea)"><h3>Sesión individual</h3><div class="precio">70 €</div><p>60 minutos por videollamada. Bono de 4: 260 €.</p></div>
  </div></div>
 <div><p class="eyebrow">Preguntas frecuentes</p>{faq_html(FAQ_T)}</div>
</div></div></section>

<section class="bg-pastel decor rev" id="contacto">{amapola_linea(w=140,estilo="left:2%;bottom:20px")}<div class="wrap"><div class="tarjeta"><div class="dos" style="align-items:start">
 <div><p class="eyebrow">Da el primer paso</p><h2>Antes de empezar, podemos hablar<span class="p">.</span></h2>
 <p class="lead" style="margin-top:16px">Déjanos tu teléfono y te llamamos para una valoración gratuita de 15 minutos.</p>
 {DESPUES}
 <p style="margin-top:26px"><span class="resalte">¿Prefieres llamar?</span></p>
 <p style="font-family:var(--serif);font-size:36px;color:var(--carbon);margin-top:10px"><a href="tel:{TEL}" style="text-decoration:none" data-conv="llamada">{TEL_TXT}</a></p></div>
 <div>{form("terapia-toc-online")}</div>
</div></div></div></section>
'''
SERV_T = {"@type":"Service","name":"Terapia para el TOC online","serviceType":"Tratamiento psicológico del trastorno obsesivo-compulsivo","provider":{"@id":DOM+"/#centro"},
 "areaServed":"España","availableChannel":{"@type":"ServiceChannel","serviceUrl":DOM+"/terapia-toc-online/","name":"Videollamada"},
 "offers":{"@type":"Offer","price":"70","priceCurrency":"EUR","description":"Sesión individual de 60 minutos"}}
BREAD_T = {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Inicio","item":DOM+"/"},{"@type":"ListItem","position":2,"name":"Terapia para el TOC online","item":DOM+"/terapia-toc-online/"}]}
page("terapia-toc-online.html","Psicóloga especialista en TOC online | Andrea Royo Psicología",
 "Terapia para el TOC por videollamada con Elena, psicóloga sanitaria especializada en trastorno obsesivo-compulsivo. Llamada de valoración gratuita de 15 minutos.",
 "/terapia-toc-online/",[NEGOCIO,SERV_T,BREAD_T,faq_schema(FAQ_T)],toc,active="TOC",landing=True)

# =========================== GRACIAS (conversión) ===========================
gracias = f'''
<section class="hero bg-crema decor" style="min-height:70vh">{PET_HERO}<div class="wrap" style="grid-template-columns:1fr">
 <div class="centro"><p class="eyebrow">Solicitud recibida</p><h1>Gracias por dar el paso<span class="p">.</span></h1>
 <p class="lead" style="margin-top:24px">Te llamaremos en menos de 24 horas laborables. Si lo prefieres, puedes llamarnos tú al <a class="enlace" href="tel:{TEL}">{TEL_TXT}</a>.</p>
 <div class="acciones" style="justify-content:center"><a class="btn linea" href="index.html">Volver al inicio</a></div></div>
</div></section>
<!-- Google Ads: pegar aquí el fragmento de evento de conversión (o dispararlo desde Tag Manager al cargar /gracias/) -->
'''
page("gracias.html","Gracias | Andrea Royo Psicología","Hemos recibido tu solicitud. Te llamaremos en menos de 24 horas laborables.","/gracias/",[NEGOCIO],gracias)
print("ok")
