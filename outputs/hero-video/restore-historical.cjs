const sharp=require('C:/Users/retro/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const fs=require('fs');
const dir='outputs/hero-video/frames-restaurados';fs.mkdirSync(dir,{recursive:true});
(async()=>{const files=fs.readdirSync('outputs/hero-video/originales');for(let i=1;i<files.length;i++){await sharp('outputs/hero-video/originales/'+files[i]).greyscale().normalise({lower:1,upper:99}).linear(1.04,-5).resize(1366,768,{fit:'cover',position:'centre',kernel:'lanczos3'}).sharpen({sigma:.7,m1:.55,m2:1.2}).png().toFile(`${dir}/0${i+1}.png`);}console.log('Cuatro fotografías ajustadas: blanco y negro, contraste y enfoque moderados, sin reconstrucción generativa.');})();
