# Andrea Royo Psicología · Propuesta de rediseño (Kit Suave)

Propuesta de rediseño de andrearoyopsicologia.com con el Kit Suave adaptado a sus colores corporativos.

## Páginas
- `terapia-individual-zaragoza.html`, `terapia-online.html`, `terapia-individual-online.html`, `terapia-duelo-zaragoza.html`, `dependencia-emocional-zaragoza.html` → landings de servicio (cabecera mínima, para Ads)
- `equipo.html` + perfiles `andrea-royo.html`, `olga-torres.html`, `elena-llopico.html`, `nerea-rascado.html`
- `blog.html` + `terapia-para-la-ansiedad.html` (artículo migrado de la web actual)
- `aviso-legal.html`, `politica-privacidad.html`, `politica-cookies.html` (textos de la clienta)
- `index.html` → portada, pensada para Google Ads con la palabra clave «psicólogo zaragoza»
- `terapia-pareja-zaragoza.html` → landing de «terapia de pareja zaragoza» (sin menú, para Ads)
- `terapia-toc-online.html` → landing de TOC online con Elena (sin menú, para Ads)
- `gracias.html` → página de gracias (noindex) para medir la conversión de Google Ads

## Menú
Pestaña desplegable «Servicios» (terapia individual, pareja y sexología, online, dependencia emocional y TOC) y menú hamburguesa en móvil. Las landings de Ads llevan cabecera mínima (logo, teléfono y «Pedir cita»).

## Secciones de conversión
- Barra de confianza bajo la cabecera (opiniones, equipo sanitario, respuesta en 24 h, ubicación)
- Objeciones resueltas («me da vergüenza», «no tengo tiempo», «mi pareja no quiere venir»…)
- Comparativa «si seguís igual / con terapia» (landing de pareja)
- Banda roja de llamada a la acción a mitad de página
- Formulario corto con «qué pasa después» y garantía sin compromiso
- Barra fija en móvil con «Llamar» y «Pedir cita»; botones con `data-conv` para medir clics

## Recursos visuales (SVG en el propio HTML)
Pocos pétalos de amapola en la cabecera, amapola dibujada a línea, forma rosa detrás de las fotos, subrayado azul a mano en la palabra clave e iconos de línea propios. Fondos: solo crema, blanco y rosa pastel; el azul queda para detalles.

## Paleta
| Uso | Color |
|---|---|
| Fondo crema (tarjeta del kit) | `#FBF6F2` |
| Rojo pastel corporativo | `#FACECA` |
| Rosa claro | `#FDEFED` |
| Rojo amapola (titulares, numerales, punto final) | `#ED5B4D` |
| Botones | `#F0857A` con texto `#3A2F2C` |
| Azul cielo de apoyo | `#6EC1E4` / `#E6F4FA` |
| Texto | `#3A2F2C` / `#5E514D` |

Tipografías: Playfair Display (titulares y textos destacados), Figtree (texto), Allura (acento manuscrito).

Amapola decorativa: una sola línea fina sobre mancha de acuarela rosa, como el logo.

Instagram: @andrearoyopsicologia

## Fuente
`_fuente/build.py` + `_fuente/base.css` + `_fuente/extra.css` generan los HTML (`python3 _fuente/build.py`, escribe en la raíz).
Las fotos nuevas del despacho están en `img/`; el logo y las fotos de Olga, Elena y Nerea se cargan desde la web actual de Andrea.

## Pendiente
- Al pasar a WordPress: quitar el noindex de las páginas y el robots.txt (están para que Google no indexe la propuesta como contenido duplicado)
- Política de cookies: corregidos dominios de otras webs que venían en la plantilla y enlaces caducados; sigue nombrando Internet Explorer
- Revisar la política de cookies: habla de consentimiento por seguir navegando (en WordPress, montar banner con aceptar/rechazar)
- Nuevas landings que prepare la clienta
- Confirmar con Andrea el compromiso de llamar en menos de 24 h laborables
- Confirmar si Elena atiende también presencial (la landing de TOC es solo online, como su web actual)

## WhatsApp
Botón flotante en escritorio y botón en la barra fija del móvil (wa.me/34614151736 con mensaje predefinido); medido con `data-conv="whatsapp"`.
