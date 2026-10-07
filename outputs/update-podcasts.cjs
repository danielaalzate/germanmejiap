const fs=require('fs');const data=JSON.parse(fs.readFileSync('dist/catalog.json','utf8').replace(/^\uFEFF/,''));
for(const e of data.episodes){e.series='ruido';e.source=`https://www.youtube.com/watch?v=${e.video}&list=PLFMWIiw4lyaFlUfHM3JF5NjXrL6naiPw2`;}
const pais=JSON.parse(fs.readFileSync('outputs/pais-youtube.json','utf8'));for(const [i,e] of pais.reverse().entries())data.episodes.push({...e,id:e.video,series:'pais',order:i+1});
fs.writeFileSync('dist/catalog.json',JSON.stringify(data,null,2));fs.writeFileSync('dist/catalog.js','window.ARCHIVE='+JSON.stringify(data)+';');
let js=fs.readFileSync('dist/archive.js','utf8');
js=js.replace('items=episodes?D.episodes:D.publications','series=params.get("serie")==="pais"?"pais":"ruido",seriesName=series==="pais"?"La construcción de un país":"En los tiempos del ruido",items=episodes?D.episodes.filter(e=>e.series===series):D.publications');
js=js.replaceAll("episodes?'En los tiempos del ruido'","episodes?seriesName");
js=js.replace('La reproducción se realiza en Javeriana Estéreo.','Cada capítulo se escucha en YouTube.');
js=js.replace('<form class="catalog-controls"','${episodes?`<nav class="press-filters" aria-label="Series de podcast"><a href="/conversaciones/?serie=ruido" ${series===\'ruido\'?\'aria-current="page"\':\'\'}>En los tiempos del ruido</a><a href="/conversaciones/?serie=pais" ${series===\'pais\'?\'aria-current="page"\':\'\'}>La construcción de un país</a></nav>`:\'\'}<form class="catalog-controls"');
js=js.replace("Number(a.title.match(/episodio\\s+(\\d+)/i)?.[1]??Infinity)-Number(b.title.match(/episodio\\s+(\\d+)/i)?.[1]??Infinity)","(a.order??Number(a.title.match(/episodio\\s+(\\d+)/i)?.[1]??Infinity))-(b.order??Number(b.title.match(/episodio\\s+(\\d+)/i)?.[1]??Infinity))");
js=js.replace('<p>En los tiempos del ruido · Javeriana Estéreo</p>','<p>${esc(seriesName)} · Javeriana Estéreo</p>').replaceAll('Escuchar en Javeriana Estéreo','Escuchar en YouTube');
js=js.replace('Títulos y videos organizados a partir del archivo de Javeriana Estéreo. La numeración reproduce la fuente, que contiene algunas inconsistencias.','Capítulos disponibles de Javeriana Estéreo, con reproducción en YouTube. Los videos privados o no disponibles no se incluyen.');
js=js.replace('const q=new URLSearchParams();for(const [k,v]','const q=new URLSearchParams();if(episodes)q.set("serie",series);for(const [k,v]');
js=js.replace("episodes?'/conversaciones/':'/obra/'","episodes?'/conversaciones/?serie='+series:'/obra/'");
fs.writeFileSync('dist/archive.js',js);
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(d+'/'+e.name):[d+'/'+e.name]);}for(const f of walk('dist').filter(f=>f.endsWith('.html'))){let s=fs.readFileSync(f,'utf8').replaceAll('catalog.js?v=2','catalog.js?v=3').replaceAll('archive.js?v=6','archive.js?v=7');if(f==='dist/index.html')s=s.replace('Explorar episodios ↗','Explorar los podcasts ↗');fs.writeFileSync(f,s);}
console.log(pais.length+' capítulos nuevos; '+data.episodes.length+' registros totales.');
