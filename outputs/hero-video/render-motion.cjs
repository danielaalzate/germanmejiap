const fs=require('fs'),{spawnSync}=require('child_process');
const ff='C:/Users/retro/Documents/ChatGPT/Paginas web otros/_video_tools/ffmpeg-9.0.1-essentials_build/bin/ffmpeg.exe';
const sources=['outputs/hero-video/clips/01.mp4',...['03','04'].map(n=>`outputs/hero-video/clips-timelapse/${n}.mp4`)];
const args=['-hide_banner','-loglevel','error','-y'];for(const source of sources)args.push('-i',source);
const filters=sources.map((_,i)=>`[${i}:v]scale=1366:768:force_original_aspect_ratio=increase,crop=1366:768,setpts=0.65*(PTS-STARTPTS),fps=24,trim=duration=3.9,setpts=PTS-STARTPTS,format=yuv420p,settb=AVTB[v${i}]`);
filters.push('[v0][v1]xfade=transition=fade:duration=0.3:offset=3.6[x1]','[x1][v2]xfade=transition=fade:duration=0.3:offset=7.2[out]');
const base=[...args,'-filter_complex',filters.join(';'),'-map','[out]','-t','11.1','-an','-c:v','libx264','-preset','slow','-b:v','590k','-pix_fmt','yuv420p','-passlogfile','outputs/hero-video/timelapse-pass'];
for(const pass of [1,2]){const a=[...base,'-pass',String(pass),...(pass===1?['-f','null','NUL']:['-movflags','+faststart','dist/assets/bogota-hero-motion-768p.mp4'])];const r=spawnSync(ff,a,{stdio:'inherit'});if(r.status)process.exit(r.status);}
const size=fs.statSync('dist/assets/bogota-hero-motion-768p.mp4').size;if(size>=1000000)throw Error('El video excede 1 MB: '+size);
fs.writeFileSync('outputs/hero-video/edit-motion.json',JSON.stringify({sources,duration:11.1,resolution:'1366x768',bitrate:590000,size,filters},null,2));console.log('Video final: '+size+' bytes');

