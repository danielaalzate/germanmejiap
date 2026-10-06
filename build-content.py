import json,re,html,unicodedata
from pathlib import Path
root=Path(__file__).parent
dist=root/'dist'
CV='https://javeriana.academia.edu/Germ%C3%A1nMej%C3%ADa/CurriculumVitae'
def slug(s):
 return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip('-')
records=[]
def add(title,year,kind,publisher,role='Autor',isbn='',topic='Historia e historiografía',source=CV,description='',cover='',editions=''):
 records.append(dict(id=slug(title),title=title,year=year,type=kind,publisher=publisher,role=role,isbn=isbn,topic=topic,source=source,description=description,cover=cover,editions=editions))
add('Los años del cambio. Historia urbana de Bogotá, 1820–1910',1999,'Libros','CEJA / Instituto Colombiano de Cultura Hispánica',isbn='9586831108',topic='Bogotá',description='Bogotá entre 1820 y 1910: una investigación sobre la transformación de la ciudad durante el siglo XIX. Un punto de entrada a la historia urbana de la capital.',cover='los-anos-del-cambio-original.webp',editions='Primera edición: 1999. Segunda edición: CEJA / ICANH, 2000; ISBN 9586833089.')
add('La ciudad de los conquistadores. Historia de Bogotá, 1536–1604',2012,'Libros','Editorial Pontificia Universidad Javeriana',isbn='9789587165302',topic='Bogotá',description='Los primeros años de Santafé constituyen el marco de esta historia de Bogotá. La ficha reúne la referencia de la edición que estudia el período comprendido entre 1536 y 1604.',cover='la-ciudad-de-los-conquistadores-original.webp')
add('La aventura urbana de América Latina',2013,'Libros','Fundación Mapfre / Taurus',topic='América Latina',description='Una mirada a la historia de las ciudades latinoamericanas. Forma parte de la colección América Latina en la Historia Contemporánea, serie Recorridos.',cover='la-aventura-urbana-original.webp')
add('Historia concisa de Colombia',2013,'Libros','Editorial Pontificia Universidad Javeriana / Universidad del Rosario','Coautor con Michael J. LaRosa','9789587166804','Colombia',source='https://www.javeriana.edu.co/editorial/w/historia-concisa-colombia',description='Una historia de Colombia escrita junto con Michael J. LaRosa. El catálogo reúne sus ediciones bajo una misma obra para facilitar la consulta.',editions='Edición de 2013: Historia concisa de Colombia (1810–2013), traducción de Matías Godoy. Edición de Debate: 2023. Cada edición puede presentar actualizaciones y una paginación diferente.')
add('Del canon a la memoria. El pasado como historia de Colombia',2020,'Libros','Editorial Pontificia Universidad Javeriana',isbn='9789587815474',topic='Colombia',source='https://perfilesycapacidades.javeriana.edu.co/en/publications/del-canon-a-la-memoria-el-pasado-como-historia-de-colombia/',description='Una obra dedicada a la escritura del pasado colombiano y a su relación con la memoria. Se integra aquí en el recorrido por las preguntas historiográficas del autor.')
add('Después de la heroica fase de exploración. La historiografía urbana en América Latina',2021,'Libros','Universidad de Guanajuato / Editorial Pontificia Universidad Javeriana','Coordinación con Gerardo Martínez Delgado',topic='América Latina',source='https://repositorio.flacsoandes.edu.ec/bitstream/10469/20278/2/LFLACSO-Martinez-COOR-152336-PUBCOM.pdf',description='Volumen colectivo coordinado con Gerardo Martínez Delgado sobre la historiografía urbana latinoamericana. Reúne el trabajo de distintos investigadores; la participación de Germán corresponde a la coordinación de la obra.')
add('Entre la libertad y el orden. Una historia de la derecha en Colombia',2025,'Libros','Debate',isbn='9786287669727',topic='Colombia',source='https://www.penguinlibros.com/co/tematicas/371834-libro-entre-la-libertad-y-el-orden-9786287669727',description='Una investigación sobre la historia de la derecha en Colombia a través de quince momentos, desde el siglo XIX hasta el XXI. Publicado por Debate en abril de 2025.')
for t,y,p,r,i,theme in [
 ('Proceso seguido al General Santander por consecuencia del acontecimiento de la noche del 25 de septiembre de 1828 en Bogotá',1988,'Fundación Francisco de Paula Santander','Colaboración en compilación y crítica documental','9586430359','Colombia'),
 ('Causas y Memorias de los Conjurados del 25 de septiembre de 1828',1990,'Fundación Francisco de Paula Santander · 3 volúmenes','Colaboración','9586430960','Colombia'),
 ('Colombia en el siglo XIX',1999,'Planeta','Coeditor','9586147797','Colombia'),
 ('La ciudad y las ciencias sociales. Ensayos y aproximaciones',2000,'CEJA / Instituto Distrital de Cultura y Turismo','Coeditor con Fabio Zambrano','9586832163','Historia urbana'),
 ('The United States Discovers Panama. The Writings of Soldiers, Scholars, Scientists, and Scoundrels, 1850–1905',2003,'Rowman & Littlefield','Coeditor','0742527212','América Latina'),
 ('La Nueva Granada Colonial. Selección de textos históricos',2005,'Universidad de los Andes / CESO','Coeditor','9586951960','Colombia'),
 ('An Atlas and Survey of Latin American History',2006,'M. E. Sharpe','Colaboración','0765615975','América Latina'),
 ('Atlas histórico de Bogotá. Cartografía 1791–2007',2007,'Archivo de Bogotá / IDPC / Planeta','Colaboración','9789584215536','Bogotá'),
 ('Colombia: A Concise Contemporary History',2012,'Rowman & Littlefield','Coautor con Michael J. LaRosa','9781442200935','Colombia'),
 ('Santa Fe. Iglesias coloniales, conventos y ermitas',2013,'Arquidiócesis de Bogotá / Consuelo Mendoza Ediciones','Coeditor académico','9789589875681','Bogotá')]: add(t,y,'Libros',p,r,i,theme)
academic='''1981|Artículos|Algunas consideraciones en torno a Qué es la Historia|Mente, 1|Historia e historiografía
1982|Artículos|Análisis de la instancia ideológica en la obra de Venancio Ortiz|Revista Javeriana, 483, pp. 265–271|Historia e historiografía
1982|Artículos|Las Sociedades Democráticas, 1848–1854. Problemas historiográficos|Universitas Humanística, 11 (17), pp. 145–176|Colombia
1986|Artículos|El sujeto social y la historia oral: una propuesta metodológica|Universitas Humanística, 14 (26), pp. 141–148|Historia e historiografía
1986|Artículos|Rebeliones indígenas en México y el Alto Perú durante el período colonial: tendencias investigativas|Boletín de Historia, 3 (5–6), pp. 20–33|América Latina
1987|Artículos|Muerte y vida cotidiana. La historia ante una proscripción|Trocadero, 3 (4), pp. 3–7|Historia e historiografía
1988|Artículos|Bogotá, condiciones de vida y dominación a finales del siglo XIX|Boletín de Historia, 5 (9–10), pp. 26–40|Bogotá
1988|Artículos|El Dios de los santafereños. Espacio y tiempo en una sociedad urbana precapitalista|Trocadero, 4 (5), pp. 5–12|Bogotá
1990|Artículos|La Historia y el Tiempo|Universitas Humanística, 19 (32), pp. 54–62|Historia e historiografía
1997|Artículos|Los itinerarios de la transformación urbana. Bogotá, 1820–1910|Anuario Colombiano de Historia Social y de la Cultura, 24, pp. 101–137|Bogotá
1999|Artículos|La pregunta por la existencia de la historia urbana|Historia Crítica, 18, pp. 23–35|Historia urbana
2000|Artículos|La historia urbana y la valoración del patrimonio urbano|Revista Javeriana, 134 (664), pp. 281–285|Historia urbana
2000|Artículos|La ciudad y el ciudadano|Arquitectura +A, 1, pp. 9–12|Historia urbana
2000|Capítulos|Pensando la Historia Urbana|En La ciudad y las ciencias sociales. CEJA / IDCT|Historia urbana
2000|Capítulos|De pueblo de indios a ciudad. Notas sobre el desarrollo urbano de Soacha|En Soacha, 400 años. Alcaldía de Soacha|Historia urbana
2003|Capítulos|La ciudad observada. Agustín Codazzi en Bogotá, 1849–1858|En Geografía física y política de la Confederación Granadina, vol. II, pp. 63–82|Bogotá
2003|Artículos|La parroquia y el barrio en la historia de Bogotá|Textos. Documentos de Historia y Teoría, 9, pp. 47–85. Universidad Nacional de Colombia|Bogotá
2005|Artículos|Qué tan vieja es Bogotá|La Rueda, 3, pp. 16–23|Bogotá
2006|Capítulos|Ciudad y Territorio|En Historia y sociedad en Cundinamarca. ESAP, pp. 37–45|Colombia
2006|Artículos|Bogotá 1810–1819. Urbs y Civitas en una época de crisis|Boletín de Historia y Antigüedades, 93 (835), pp. 885–912|Bogotá
2007|Capítulos|Cuando La Candelaria era Bogotá: un recorrido por el sector en el siglo XVIII|Cátedra abierta de localidades: La Candelaria. Cámara de Comercio de Bogotá, pp. 9–32|Bogotá
2008|Capítulos|Santafé. De ciudad fundada a ciudad construida|En Urbanismo y vida urbana en Iberoamérica colonial. Archivo de Bogotá, pp. 193–226|Bogotá
2008|Capítulos|Miguel Samper Agudelo (1825–1899)|En Pensamiento colombiano del siglo XX, vol. 2. Javeriana, pp. 299–321|Colombia
2009|Capítulos|La ciudad barroca y el reformismo ilustrado. Bogotá, 1774–1816|En Ilustración en el mundo hispánico. Tlaxcala / Universidad Iberoamericana, pp. 431–452|Bogotá
2009|Capítulos|El árbol de la plaza|En Te cuento la Independencia. Ministerio de Educación, pp. 75–81|Colombia
2010|Capítulos|1810: el umbral a la República|En Colombias, 200 años. Museo de Antioquia, pp. 27–34|Colombia
2010|Artículos|El idioma de la nación. La experiencia decimonónica colombiana|Ínsula, 65 (762), pp. 16–20|Colombia
2010|Capítulos|El nacimiento de un orden territorial. Poblamiento y territorio en Colombia, 1810–1910|En Colombia. Preguntas y respuestas sobre su pasado y su presente. Universidad de los Andes, pp. 171–190|Colombia
2010|Capítulos|Las guerras civiles en Bogotá|En Bogotá y el Ejército Nacional en el Bicentenario. Fotomuseo, pp. 208–223|Bogotá
2010|Capítulos|Pontificia Universidad Javeriana. Una historia, 1924–1978|En Pontificia Universidad Javeriana, 80 años, pp. 67–154|Colombia
2010|Capítulos|La ciudad capital, espacio urbano, nomenclatura y monumentalidad. Bogotá, 1810–1910|En Del mundo hispánico a la consolidación de las naciones. Tlaxcala, pp. 461–492|Bogotá
2011|Capítulos|En busca de la intimidad (Bogotá, 1880–1910)|En Historia de la vida privada en Colombia, tomo II. Taurus, pp. 1–45|Bogotá
2012|Capítulos|Santafé en el siglo XVIII. Aires de transformación|En Fray Domingo de Petrés. IDPC, pp. 29–37|Bogotá
2012|Artículos|La creación del Virreinato de la Nueva Granada y su capital, Santafé de Bogotá|De Memoria, 1, pp. 10–13|Bogotá
2012|Capítulos|Los tiempos de la ciudad|En Memorias del patrimonio. Universidad de Boyacá, pp. 118–121|Historia urbana
2013|Artículos|Febrero de 1933|Revista Javeriana, 149 (794), pp. 14–22|Colombia
2013|Artículos|La ciudad recordada. Notas de Josefa Acevedo y Gómez sobre Santafé en 1810|De Memoria, 3, pp. 45–48|Bogotá
2013|Artículos|El histórico archivo Javeriano|De Memoria, 5, pp. 39–43|Historia e historiografía
2015|Capítulos|España en Colombia. Rastros de una añeja amistad|En Colombia: un país en transformación acelerada. Nebrija / McGraw-Hill, pp. 179–183|Colombia
2015|Capítulos|La prisión historiográfica. Un concepto relevante de Germán Colmenares|En Una obra para la historia: homenaje a Germán Colmenares. Universidad del Rosario, pp. 1–13|Historia e historiografía
2015|Capítulos|Bogotá, 1966|En Si las paredes hablaran: 50 años de música en la Biblioteca Luis Ángel Arango. Banco de la República|Bogotá
2016|Capítulos|Bogotá 1948. De la hipérbole al mito|En Ciudades sudamericanas como arenas culturales. Siglo XXI|Bogotá
1989|Reseñas|Entre celebración y celebración|Boletín Cultural y Bibliográfico, 24 (20), pp. 75–77|Bogotá
2010|Reseñas|Un nuevo enfoque de las independencias|Revista de Occidente, 354, pp. 150–155|América Latina
1979|Material educativo|El Hombre y su huella. Historia de Colombia II|Voluntad|Colombia
1988|Material educativo|Educación para la Democracia. Módulo de Bachillerato por Radio|Inravisión / Universidad Javeriana|Colombia
1991|Material educativo|Civilización 8|Norma. Unidades 1, 4 y 5; revisión de 1994|Historia e historiografía
1991|Material educativo|Civilización 9|Norma. Unidades 1, 3 y 5; revisión de 1994|Historia e historiografía'''
for line in academic.splitlines():
 y,k,t,p,theme=line.split('|'); add(t,int(y),k,p,role='Colaboración' if k=='Material educativo' or t.startswith('La parroquia') else 'Autor',topic=theme)
add('De ciudades, villas, pueblos y parroquias',2017,'Reseñas','Boletín Cultural y Bibliográfico, 51 (92), pp. 177–178',topic='Colombia',source='https://publicaciones.banrepcultural.org/index.php/boletin_cultural/article/view/7980',description='Reseña del libro Poblamiento y economía, de Guerrero, Pabón y Ferreira. Se cataloga como reseña bibliográfica, no como un libro de autoría de Germán Mejía Pavony.')
episodes=[]
source_path=root/'review/radio-source.html'
source=source_path.read_text(encoding='utf-8-sig') if source_path.exists() else ''
if not source and (dist/'catalog.json').exists():
 episodes=json.loads((dist/'catalog.json').read_text(encoding='utf-8'))['episodes']
for m in re.finditer(r'<h4[^>]*>(.*?)</h4>',source,re.S):
 title=html.unescape(re.sub('<[^>]+>','',m.group(1))).strip()
 if not re.match(r'Episodio\s+\d+',title,re.I): continue
 ids=re.findall(r'youtube.com/embed/([\w-]{11})',source[:m.start()])
 if ids and not any(e['video']==ids[-1] for e in episodes): episodes.append(dict(id=ids[-1],video=ids[-1],title=title,source='https://javerianaestereo.com/tiempos-del-ruido'))
data={'publications':records,'episodes':episodes}
(dist/'catalog.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(dist/'catalog.js').write_text('window.ARCHIVE='+json.dumps(data,ensure_ascii=False)+';',encoding='utf-8')
print(f'{len(records)} publicaciones, {len(episodes)} episodios')
