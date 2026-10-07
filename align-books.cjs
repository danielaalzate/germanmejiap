const fs=require('fs');fs.appendFileSync('dist/style.css',`
/* A single, shared angle keeps the three volumes visually coherent. */
.book-gallery .book-object{transform:perspective(1100px) rotateY(13deg) rotateZ(-2deg)}
.book-object:before{left:-12px;right:auto;transform:skewY(15deg);transform-origin:right;border-left:1px solid #bcb09a;border-right:0}
@media(max-width:720px){.book-object:before{left:-8px;right:auto}}
`);let h=fs.readFileSync('dist/index.html','utf8').replace('style.css?v=9','style.css?v=10');fs.writeFileSync('dist/index.html',h);
