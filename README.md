# Andrea Royo Psicología · Propuesta de rediseño (Kit Suave)

Propuesta de rediseño de andrearoyopsicologia.com con el Kit Suave adaptado a sus colores corporativos.

## Páginas
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

Tipografías: Playfair Display (titulares), Figtree (texto), Allura (acento manuscrito).

## Fuente
`_fuente/build.py` + `_fuente/base.css` + `_fuente/extra.css` generan los HTML (`python3 _fuente/build.py`, escribe en la raíz).
Las imágenes se cargan desde la web actual de Andrea.

## Pendiente
- Confirmar con Andrea el compromiso de llamar en menos de 24 h laborables
- Nº de colegiada
- Apellidos de Elena y Nerea
- Páginas de terapia individual, dependencia emocional y online (en el menú apuntan de momento a la sección de servicios de la portada)
- Confirmar si Elena atiende también presencial (la landing de TOC es solo online, como su web actual)
