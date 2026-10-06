const fs=require('fs'),path=require('path');
const sharp=require('C:/Users/retro/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
(async()=>{
const assets='dist/assets';
const covers=['los-anos-del-cambio.webp','la-ciudad-de-los-conquistadores.jpg','la-aventura-urbana.jpg'];
for(const cover of covers){const dest=cover.replace(/\.(jpg|webp)$/, '-original.webp');await sharp(path.join(assets,cover)).sharpen({sigma:.6,m1:.5,m2:1.2}).webp({lossless:true}).toFile(path.join(assets,dest));}
let home=fs.readFileSync('dist/index.html','utf8');
['one','two','three'].forEach((key,i)=>{home=home.replace(new RegExp('<span class="dummy dummy-'+key+'"[^>]*></span>'),'<img src="/assets/'+covers[i].replace(/\.(jpg|webp)$/,'-original.webp')+'" alt="Carátula original de '+['Los años del cambio','La ciudad de los conquistadores','La aventura urbana de América Latina'][i]+'" loading="lazy">')});
home=home.replace(/<p class="cover-note">.*?<\/p>/,'').replace('/style.css?v=6','/style.css?v=7');fs.writeFileSync('dist/index.html',home);
for(const file of ['dist/catalog.json','dist/catalog.js','build-content.py','dist/app.js']){let text=fs.readFileSync(file,'utf8');for(const cover of covers)text=text.replaceAll(cover,cover.replace(/\.(jpg|webp)$/,'-original.webp'));text=text.replace('Dummies: cubiertas conceptuales provisionales; las fichas muestran las ediciones originales.','Carátulas originales con un ajuste conservador de nitidez, sin rediseño.');fs.writeFileSync(file,text)}
for(const dir of fs.readdirSync('dist/obra',{withFileTypes:true}).filter(x=>x.isDirectory())){const file=path.join('dist/obra',dir.name,'index.html');let text=fs.readFileSync(file,'utf8');for(const cover of covers)text=text.replaceAll(cover,cover.replace(/\.(jpg|webp)$/,'-original.webp'));fs.writeFileSync(file,text)}
console.log('Tres carátulas originales incorporadas. Conservadas las imágenes fuente.');
})();
