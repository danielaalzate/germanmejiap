from pathlib import Path
import json,re
root=Path(__file__).parent; dist=root/'dist'
home=(dist/'index.html').read_text(encoding='utf-8')
home=re.sub(r'href="style.css[^\"]*"','href="/style.css?v=5"',home)
home=re.sub(r'src="app.js[^\"]*"','src="/app.js?v=3"',home)
home=home.replace('src="assets/','src="/assets/')
if '/archive.css' not in home: home=home.replace('</head>','<link rel="stylesheet" href="/archive.css?v=1"><script src="/catalog.js?v=1" defer></script><script src="/archive.js?v=1" defer></script></head>')
data=json.loads((dist/'catalog.json').read_text(encoding='utf-8'))
ids=[p['id'] for p in data['publications']]
for key,target in [('bio','trayectoria'),('talks','conferencias'),('invite','contacto'),('book1','obra/'+ids[0]),('book2','obra/'+ids[1]),('book3','obra/'+ids[2])]:
 home=re.sub(r'<button([^>]*?)data-open="'+key+r'"([^>]*?)>(.*?)</button>',lambda m:'<a'+m[1]+'href="/'+target+'/"'+m[2]+'>'+m[3]+'</a>',home,flags=re.S)
for anchor in ['trayectoria','obra','conversaciones','prensa','contacto']:
 home=home.replace('href="#'+anchor+'"','href="/'+anchor+'/"')
home=home.replace('href="#inicio"','href="/"')
home=re.sub(r'<div class="library-links">.*?</div>','<div class="library-links"><a href="/obra/">Explorar toda la obra</a><a href="/obra/?tipo=Art%C3%ADculos">Artículos y textos académicos</a></div>',home,flags=re.S)
home=home.replace('href="https://javerianaestereo.com/tiempos-del-ruido" target="_blank" rel="noopener"','href="/conversaciones/"')
for external,internal in [('https://www.radionacional.co/cultura/san-victorino-pasado-y-presente-de-la-capital','san-victorino'),('https://www.portaluniciso.com/producto/podcast-un-poco-de-historia-y-tps-para-tus-proyectos-invitado-german-mejia-pavony/','entrevista-uniciso'),('https://cienciassociales.javeriana.edu.co/w/germ%C3%A1n-mej%C3%ADa-pavony','perfil-javeriana')]:
 home=home.replace('href="'+external+'" target="_blank" rel="noopener"','href="/prensa/'+internal+'/"')
(dist/'index.html').write_text(home,encoding='utf-8')
shell=re.sub(r'<main id="contenido">.*?</main>','<main id="contenido"><div class="inner-page wrap"><p>Cargando el archivo…</p></div></main>',home,flags=re.S)
routes=['obra','trayectoria','conferencias','conversaciones','prensa','contacto']+['obra/'+p['id'] for p in data['publications']]+['conversaciones/'+p['id'] for p in data['episodes']]+['prensa/'+s for s in ['san-victorino','entrevista-uniciso','perfil-javeriana']]
for route in routes:
 path=dist/route/'index.html';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(shell,encoding='utf-8')
print(str(len(routes))+' páginas internas generadas')
