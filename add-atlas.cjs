const fs=require('fs'),vm=require('vm');
const file='dist/catalog.json',d=JSON.parse(fs.readFileSync(file,'utf8'));
const p={id:'atlas-historico-de-barrios-de-bogota-1884-1954',title:'Atlas histórico de barrios de Bogotá, 1884–1954',year:2019,type:'Libros',publisher:'Instituto Distrital de Patrimonio Cultural / Universidad Nacional de Colombia',role:'Coautor con Luis Carlos Colón Llamas',isbn:'9789587839128',topic:'Bogotá',source:'https://idpc.gov.co/publicaciones/producto/atlas-historico-de-barrios-de-bogota-1884-1954-2/',description:'A través de mapas y documentos históricos, Luis Carlos Colón Llamas y Germán Mejía Pavony estudian la formación de los barrios de Bogotá entre 1884 y 1954. El atlas recorre el crecimiento de la ciudad, la transformación del suelo y la organización de sus espacios residenciales.',cover:'atlas-barrios-bogota-original.jpg',coverSource:'https://portaldelibros.unal.edu.co/gpd-atlas-histy-rico-de-barrios-de-bogotya-1884-1954-9789587839128.html',editions:'',buyLabel:'Comprar en Iberlibro',buyUrl:'https://www.iberlibro.com/Atlas-hist%C3%B3rico-barrios-Bogot%C3%A1-1884-1954-Luis/32467914686/bd'};
d.publications=d.publications.filter(x=>x.id!==p.id);
d.publications.push(p);fs.writeFileSync(file,JSON.stringify(d,null,2)+'\n');fs.writeFileSync('dist/catalog.js','window.ARCHIVE = '+JSON.stringify(d)+';\n');
// Render the existing detail function with a minimal document, keeping the same template.
const main={innerHTML:''},doc={title:'',body:{classList:{add(){}}},querySelector:s=>s==='main'?main:{},querySelectorAll:()=>[]};
let js=fs.readFileSync('dist/archive.js','utf8');js=js.slice(0,js.indexOf('\nfunction catalog'));
// Only the shared helpers and detail renderer are needed.
const end=js.indexOf('\nfunction detail');const next=js.indexOf('\n',end+1);
js=js+'\ndetail(window.ARCHIVE.publications.find(p=>p.id==="'+p.id+'"));})();';
vm.runInNewContext(js,{document:doc,window:{ARCHIVE:d},location:{pathname:'/obra/'+p.id+'/'},navigator:{}});
let html=fs.readFileSync('dist/obra/atlas-historico-de-bogota-cartografia-17912007/index.html','utf8').replace(/<main id="contenido">[\s\S]*?<\/main>/,'<main id="contenido">'+main.innerHTML+'</main>').replace(/<title>.*?<\/title>/,'<title>'+doc.title+'</title>').replace(/<meta name="description" content="[^"]*">/,'<meta name="description" content="'+p.title+' · '+p.role+'.">');
fs.mkdirSync('dist/obra/'+p.id,{recursive:true});fs.writeFileSync('dist/obra/'+p.id+'/index.html',html);
function bump(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const f=dir+'/'+e.name;if(e.isDirectory())bump(f);else if(f.endsWith('.html'))fs.writeFileSync(f,fs.readFileSync(f,'utf8').replaceAll('/catalog.js?v=3','/catalog.js?v=4'));}}bump('dist');
console.log('Added atlas, original cover, static detail and purchase link.');

