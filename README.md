# Germán Rodrigo Mejía Pavony

Sitio estático en español. La versión publicable está en `dist/`: servir esta carpeta como raíz de un servidor HTTP, conservando sus subdirectorios. Los archivos publicados no requieren instalación ni compilación. Los enlaces y recursos usan rutas absolutas desde `/`.

## Rutas y contenido

- `/`: portada editorial aprobada.
- `/trayectoria/`, `/conferencias/`, `/obra/`, `/conversaciones/`, `/prensa/` y `/contacto/`: seis índices o páginas principales.
- `/obra/{id}/`: 66 fichas bibliográficas; búsqueda, tipo, tema, orden y paginación en el índice mediante parámetros de URL.
- `/conversaciones/{id}/`: 70 episodios del archivo de Javeriana Estéreo con reproductores de YouTube mediante `youtube-nocookie.com`.
- `/prensa/{id}/`: tres presentaciones con enlace al medio original.

En total: 145 rutas internas más la portada. Las páginas internas incluyen HTML prerenderizado y metadatos propios; JavaScript activa filtros, referencias y otras interacciones. `dist/archive.css` y `dist/archive.js` amplían los estilos y comportamientos compartidos de la portada. La identidad aprobada permanece documentada en `DESIGN.md` y `.impeccable/design.json`.

## Fuentes y actualización

`build-content.py` mantiene las referencias bibliográficas y produce `dist/catalog.json` y `dist/catalog.js`. El JSON descargable contiene tanto publicaciones como episodios. La fuente principal de la bibliografía es la [hoja de vida histórica del autor](https://javeriana.academia.edu/Germ%C3%A1nMej%C3%ADa/CurriculumVitae), complementada por enlaces editoriales e institucionales en cada registro. Las ediciones identificadas se agrupan; no se presenta el catálogo como exhaustivo ni los cargos abiertos del CV como actuales.

Los episodios se extraen de la copia local `review/radio-source.html`, procedente del [archivo de Javeriana Estéreo](https://javerianaestereo.com/tiempos-del-ruido). Su numeración reproduce las inconsistencias de la fuente. Actualizar esta copia explícitamente si cambia el archivo original: el generador no la descarga.

Para regenerar, ejecutar desde la raíz del proyecto:

```powershell
python build-content.py
python build-pages.py
```

`build-pages.py` actualiza los enlaces de la portada y genera las páginas internas a partir de ella. Después, mantener un servidor en otra terminal:

```powershell
python -m http.server 8793 --directory dist --bind 127.0.0.1
```

Con el servidor activo, completar el HTML y los metadatos:

```powershell
node prerender.cjs
```

La generación necesita Python 3, Node.js, Playwright y Chrome. Actualmente `prerender.cjs` y `check-internals.cjs` apuntan al Playwright del runtime local de Codex y a Chrome en Windows mediante rutas absolutas; adaptar esas rutas si se ejecutan en otro equipo. El prerender bloquea solicitudes externas y no verifica reproducción remota. Regenerar siempre en ese orden; `build-pages.py` vuelve a escribir las páginas internas antes del prerender.

## Comprobaciones

Con el servidor anterior activo:

```powershell
node check-internals.cjs
```

El comprobador prueba portada y páginas representativas a 1440px y 390px: ausencia de desbordamiento horizontal, un único H1, filtros, paginación y retroceso, búsqueda sin resultados, ficha de publicación, iframe de episodio, descarga local de invitación y menú móvil. Comprueba la existencia de las 66 fichas y ausencia de errores JavaScript registrados. Guarda capturas del catálogo, la biografía y una ficha en `review/internal-*.png`. No comprueba disponibilidad de todos los enlaces externos ni reproducción efectiva de los 70 videos.

## Pendiente antes del lanzamiento público

- Confirmar el correo o endpoint de contacto. El formulario solo descarga un borrador local: no envía mensajes ni confirma disponibilidad.
- Aportar el video autorizado del hero; los videos reales del archivo de radio son independientes de ese pendiente.
- Revisar el contenido editorial con Germán y ampliar homenajes solo con fuentes documentadas.

## Imágenes y créditos

Retrato y fotografía de radio suministrados por el usuario. Las fotografías usan recorte proporcional o altura natural, sin estiramiento. La portada actual utiliza `hero-approved.png`, recreación generada al atardecer del diseño aprobado, identificada en créditos. Los libros de la portada utilizan `book-dummies.png`, con cubiertas provisionales crema, terracota y verde; las fichas conservan las portadas editoriales disponibles y distinguen las representaciones tipográficas de las portadas reales.

Panorama documental de la Plaza de Bolívar: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Panor%C3%A1mica_Plaza_de_Bol%C3%ADvar_Bogot%C3%A1.jpg), Gabriel Leonardo Guerrero (DeMentePhoto), CC BY-SA 4.0. Portadas: Librería Merlín, Digitalia/Editorial Javeriana y Penguin Libros. Ilustraciones generadas con la herramienta de imágenes: torre de iglesia bogotana, montañas andinas y mapa latinoamericano, con tratamiento de grabado de grafito sobre marfil.
