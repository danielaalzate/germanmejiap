const fs=require('fs'),vm=require('vm');
let js=fs.readFileSync('dist/archive.js','utf8');
const match=js.match(/const press=(\[[\s\S]*?\]);\r?\nif\(!route.length\)/);
const old=vm.runInNewContext('('+match[1]+')');
const research=JSON.parse(fs.readFileSync('press-research.json','utf8'));
const press=[...research.newItems,...old];
fs.writeFileSync('dist/press.json',JSON.stringify(press,null,2));
js=js.replace(match[1],JSON.stringify(press));
const start=js.indexOf("const p=press.find",js.indexOf("else if(route[0]==='prensa')"));
const end=js.indexOf("}else if(route[0]==='contacto')",start);
js=js.slice(0,start)+`const p=press.find(p=>p.id===route[1]);const category=new URLSearchParams(location.search).get('tipo');const selected=category?press.filter(p=>p.kind===category):press;title(p?p.title:'Germán y la prensa');
const meta=p=>esc([p.kind,p.medium,p.date].filter(Boolean).join(' · '));
page(p?\`\${bread('Prensa')}\${heading(esc(p.title))}<p class="record-meta">\${meta(p)}</p>\${p.author?'<p>Por '+esc(p.author)+'</p>':''}<article class="reading"><h2>Sobre esta pieza</h2><p>\${esc(p.text)}</p><p class="catalog-footnote">Presentación editorial. El artículo íntegro se consulta en el medio original.</p>\${sourceLink(p.source,'Leer en '+p.medium)}</article><div class="actions">\${link('prensa','Volver a Germán y la prensa','text-link')}</div>\`:\`\${bread('Prensa')}\${heading('Homenajes y perfiles')}<p class="lead">Su obra y su voz en los medios.</p><nav class="press-filters" aria-label="Categorías de prensa"><a href="/prensa/" \${!category?'aria-current="page"':''}>Todas</a>\${[...new Set(press.map(p=>p.kind))].map(k=>'<a href="/prensa/?tipo='+encodeURIComponent(k)+'" '+(category===k?'aria-current="page"':'')+'>'+esc(k)+'</a>').join('')}</nav><p class="record-meta">\${selected.length} piezas</p><div class="press-references">\${selected.map(p=>\`<article><p class="record-meta">\${meta(p)}</p><h2>\${link('prensa/'+p.id,esc(p.title))}</h2><p>\${esc(p.text)}</p>\${link('prensa/'+p.id,'Ver la pieza','text-link')}</article>\`).join('')}</div>\`)
`+js.slice(end);
fs.writeFileSync('dist/archive.js',js);
fs.appendFileSync('dist/archive.css','\n.press-filters{position:static;display:flex;flex-wrap:wrap;gap:12px 22px;padding:24px 0;border-block:1px solid #ded2bf;background:none;box-shadow:none}.press-filters a{font-size:14px;padding:6px 0}.press-filters a[aria-current=page]{color:#97360f;text-decoration:underline;text-underline-offset:6px}.press-references{max-width:920px}.press-references article{padding:30px 0;border-bottom:1px solid #ded2bf}.press-references h2{font-size:36px;max-width:850px}.press-references article>p:not(.record-meta){max-width:75ch}@media(max-width:720px){.press-filters{display:flex!important;flex-direction:row!important}.press-references h2{font-size:29px}}\n');
let home=fs.readFileSync('dist/index.html','utf8');home=home.replace('<h3>San Victorino: pasado y presente de la capital</h3>','<h3>Entre la libertad y el orden: una lectura recomendada</h3>').replace('<small>Radio Nacional de Colombia</small>','<small>La República · 8 de abril de 2025</small>').replace('href="/prensa/san-victorino/"','href="/prensa/la-republica-libertad-orden/"');
home=home.replace('</div></div></section>\n<section class="contact"','</div></div><p><a class="text-link" href="/prensa/">Ver todas las publicaciones en prensa</a></p></section>\n<section class="contact"');
fs.writeFileSync('dist/index.html',home);
for(const p of press){const dir='dist/prensa/'+p.id;fs.mkdirSync(dir,{recursive:true});if(!fs.existsSync(dir+'/index.html'))fs.copyFileSync('dist/prensa/perfil-javeriana/index.html',dir+'/index.html')}
function walk(d){for(const e of fs.readdirSync(d,{withFileTypes:true})){const p=d+'/'+e.name;if(e.isDirectory())walk(p);else if(p.endsWith('.html'))fs.writeFileSync(p,fs.readFileSync(p,'utf8').replace('/archive.js?v=2','/archive.js?v=3').replace('/archive.css?v=2','/archive.css?v=3'))}}walk('dist');
let pre=fs.readFileSync('prerender.cjs','utf8');pre=pre.replace("'prensa/san-victorino','prensa/entrevista-uniciso','prensa/perfil-javeriana'","...JSON.parse(fs.readFileSync('dist/press.json','utf8')).map(p=>'prensa/'+p.id)");fs.writeFileSync('prerender.cjs',pre);
console.log(press.length+' piezas de prensa; '+research.newItems.length+' incorporaciones verificadas.');
