from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from fontTools.ttLib import TTFont as FT
from fontTools.varLib.instancer import instantiateVariableFont
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import RectangleObject
import shutil
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
OUT=ROOT/'public/assets'; OUT.mkdir(exist_ok=True)
for name,weight in [('Regular',400),('Bold',700),('ExtraBold',800)]:
 p=HERE/f'Inter-{name}.ttf'
 if not p.exists():
  f=FT(HERE/'Inter-variable.ttf'); instantiateVariableFont(f,{'wght':weight,'opsz':14},inplace=True)
  for nid,value in [(1,'Inter '+name),(2,'Regular'),(4,'Inter '+name),(6,'Inter-'+name)]:
   f['name'].setName(value,nid,3,1,0x409)
  f.save(p)
 pdfmetrics.registerFont(TTFont(name,str(p)))
pdfmetrics.registerFontFamily('Regular',normal='Regular',bold='Bold')
W,H=95*mm,145*mm
INK='#111714'; MUTED='#5e625e'; GREEN='#334c44'; AQUA='#16a7bd'; LIME='#aac833'; GOLD='#f2bd18'; PAPER='#f5f3ed'; LINE='#dcded9'
URL='https://comunita-sassifraga.github.io/ViviSoana-Web/'
DIGITAL=OUT/'passaporto-della-valle-digitale.pdf'
c=canvas.Canvas(str(DIGITAL),pagesize=(W,H),pageCompression=1)
c.setTitle('Passaporto della Valle | Valle Soana');c.setAuthor('Valle Soana');c.setSubject('Sei missioni, sei riconoscimenti e un legame con la Valle Soana')
def rect(x,y,w,h,color,stroke=None,r=0):
 c.setFillColor(HexColor(color)); c.setStrokeColor(HexColor(stroke or color));c.setLineWidth(.55)
 if r:c.roundRect(x*mm,H-(y+h)*mm,w*mm,h*mm,r*mm,fill=1,stroke=bool(stroke))
 else:c.rect(x*mm,H-(y+h)*mm,w*mm,h*mm,fill=1,stroke=bool(stroke))
def text(t,x,y,size=9,font='Regular',color=INK):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x*mm,H-y*mm,t)
def para(t,x,y,w=81,size=9,leading=12,color=INK,font='Regular'):
 s=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading,textColor=HexColor(color))
 p=Paragraph(t,s);pw,ph=p.wrap(w*mm,1000);p.drawOn(c,x*mm,H-y*mm-ph);return y+ph/mm

def base(n,label,accent=AQUA):
 rect(0,0,95,145,'#ffffff');rect(7,8,12,1.5,accent)
 text(label.upper(),7,15,7,'Bold',GREEN)
 c.setStrokeColor(HexColor(LINE));c.setLineWidth(.5);c.line(7*mm,10*mm,88*mm,10*mm)
 text('VALLE SOANA',7,140,6.6,'Bold',MUTED);text(f'{n:02d} / 12',77,140,6.6,'Regular',MUTED)
 c.bookmarkPage(f'p{n}');c.addOutlineEntry(label,f'p{n}',level=0)
def title(t,y=20,size=20):return para(t,7,y,size=size,leading=size*1.05,font='ExtraBold')
def line(label,y):
 text(label,7,y,7,'Bold',MUTED);c.setStrokeColor(HexColor(LINE));c.line(7*mm,H-(y+9)*mm,88*mm,H-(y+9)*mm)
def stamp(x,y,w,h,label,sub='Data:'):
 rect(x,y,w,h,'#ffffff',LINE,1.5);text(label,x+2,y+4.3,6.6,'Bold',MUTED)
 if sub:text(sub,x+2,y+h-2.6,6.2,'Regular',MUTED)
def qrbox(url,x,y,size):
 q=qr.QrCodeWidget(url);b=q.getBounds();d=Drawing(size*mm,size*mm,transform=[size*mm/(b[2]-b[0]),0,0,size*mm/(b[3]-b[1]),0,0]);d.add(q);renderPDF.draw(d,c,x*mm,H-(y+size)*mm)
 c.linkURL(url,(x*mm,H-(y+size)*mm,(x+size)*mm,H-y*mm),relative=0)
def finish():c.showPage()
# Cover: the original, unmodified official lockup includes all three crests.
base(1,'Il tuo viaggio comincia qui')
c.drawImage(str(OUT/'valle-soana-logo.png'),7*mm,H-38*mm,width=81*mm,height=17.26*mm,mask='auto')
rect(0,45,95,70,GREEN)
para('PASSAPORTO<br/>DELLA<br/>VALLE',7,53,81,28,29,'#ffffff','ExtraBold')
text('SCOPRI. TORNA. PARTECIPA.',7,104,8,'Bold','#ffffff')
for i,col in enumerate([AQUA,LIME,GOLD]):rect(i*95/3,115,95/3,2,col)
para('Ronco Canavese · Valprato Soana · Ingria',7,122,size=8,leading=11)
finish()
base(2,'Come funziona',LIME);title('Una valle da<br/>sentire tua.')
para('Scegli da dove cominciare. Completa le sei missioni nel tempo e raccogli i timbri delle tue esperienze.',7,39,size=9.2,leading=12.5)
for y,num,t in [(61,'1','Chiedi al referente dove ottenere i timbri e quali attività sono valide.'),(78,'2','Porta il Passaporto con te. Fai registrare le esperienze nelle facciate 3-8.'),(95,'3','Fai convalidare le missioni nelle facciate 9-10. Tutte e sei aprono il traguardo finale.')]:
 text(num,7,y+4,15,'ExtraBold',GREEN);para(t,16,y,72,8.6,11.3)
line('QUESTO PASSAPORTO APPARTIENE A',120);finish()
missions=[
 ('Scopri i<br/>tre comuni','Visita <b>Ronco Canavese, Valprato Soana e Ingria</b>. Raccogli le convalide previste nei tre comuni.','Esploratore della Soana',AQUA),
 ('Torna in<br/>stagioni diverse','Riscopri la valle in <b>primavera, estate, autunno e inverno</b>. Raccogli un timbro per ogni stagione.','Fedele alla Valle',LIME),
 ('Sostieni le<br/>attività locali','Raccogli un timbro in <b>quattro esercizi aderenti diversi</b>, raggiungendo in ciascuno la <b>soglia minima di spesa prevista</b>. Chiedila prima dell’acquisto.','Alleato della Comunità',GOLD),
 ('Invita chi ancora<br/>non la conosce','Porta con te <b>persone nuove</b> e fai registrare i loro arrivi. Chiedi al referente le modalità di completamento della missione.','Ambasciatore della Soana',AQUA),
 ('Partecipa alla vita<br/>del territorio','Prendi parte a <b>iniziative dedicate all’ambiente, al paesaggio e alla conoscenza della valle</b>. Chiedi al referente quali partecipazioni convalidare.','Sentinella del Paesaggio',LIME),
 ('Arricchisci il<br/>Digital Twin','Proponi <b>luoghi, storie, informazioni o riprese da smartphone</b>, anche per contenuti 3D. I contributi sono valutati prima dell’eventuale integrazione.','Custode della Memoria',GOLD)]
for i,(tit,desc,award,col) in enumerate(missions):
 n=i+3;base(n,f'Missione {i+1:02d}',col);title(tit,size=19)
 end=para(desc,7,37,size=8.5,leading=11.1)
 assert end<65,(i,end)
 if i==0:
  for y,l in zip([55,81,107],['Ronco Canavese','Valprato Soana','Ingria']):stamp(7,y,81,24,l)
 elif i in [1,2,3]:
  labels= [['Primavera','Estate','Autunno','Inverno'],['Esercizio 1','Esercizio 2','Esercizio 3','Esercizio 4'],['Nuovo arrivo','Nuovo arrivo','Nuovo arrivo','Nuovo arrivo']][i-1]
  for k,l in enumerate(labels):stamp(7+(k%2)*42,67+(k//2)*33,39,30,l, 'Data / riferimento:' if i==3 else 'Data:')
  if i==3: text('Spazi di registrazione; requisiti dal referente.',7,133,6.7,'Regular',MUTED)
 else:
  line('INIZIATIVA / CONTRIBUTO',70);line('DATA E REFERENTE / CODICE DI INVIO',89)
  stamp(7,106,81,25,'Registrazione / timbro del referente',None)
 finish()
for n,start in [(9,0),(10,3)]:
 base(n,'Convalide delle missioni',LIME);title('Ogni missione,<br/>un riconoscimento.',size=18)
 para('Convalida a cura del Comune, del Sindaco o di un referente autorizzato.',7,37,size=8,leading=10.5)
 for j in range(3):
  k=start+j;y=48+j*29
  text(f'{k+1:02d}',7,y+4,8,'ExtraBold',GREEN)
  para(missions[k][2],16,y,72,8.6,10,'#111714','Bold')
  stamp(7,y+7,81,20,'Timbro / firma del referente', 'Data:')
 finish()
base(11,'Il traguardo finale',GOLD);title('Cittadino<br/>della Valle',size=24)
para('Completa <b>tutte e sei le missioni</b> e fai convalidare il percorso. Riceverai un <b>titolo simbolico di appartenenza</b> alla comunità della Valle Soana.',7,43,size=9,leading=12)
rect(7,70,81,27,PAPER,r=2)
para('Il titolo viene conferito pubblicamente durante la <b>Festa annuale degli Amici della Valle</b>: una giornata per incontrarsi e festeggiare insieme.',10,74,75,8.4,11)
stamp(7,102,81,29,'Convalida del percorso completo', 'Data / firma del referente:');finish()
base(12,'Per continuare il viaggio',AQUA);title('Un motivo in più<br/>per tornare.',size=19)
para('<b>Vantaggi nelle attività aderenti, inviti a iniziative dedicate, occasioni riservate per tornare e riconoscimenti della comunità.</b> Chiedi agli aderenti le condizioni disponibili.',7,38,size=8.5,leading=11.2)
qrbox('https://visitvallesoana.it/',5,66,23)
text('VISIT VALLE SOANA',31,72,8,'Bold',GREEN)
para('Ospitalità, eventi, sentieri<br/>e contatti del territorio.',31,75,57,8,10.5)
text('visitvallesoana.it',31,90,7,'Regular',MUTED);c.linkURL('https://visitvallesoana.it/',(31*mm,H-92*mm,88*mm,H-67*mm))
qrbox('https://soana-portale.vercel.app/',5,96,23)
text('DIGITAL TWIN',31,102,8,'Bold',GREEN)
para('Esplora la valle digitale.<br/>Per proporre un contributo,<br/>usa i contatti del progetto.',31,105,57,8,10)
text('soana-portale.vercel.app',31,120,7,'Regular',MUTED)
c.linkURL('https://soana-portale.vercel.app/',(31*mm,H-122*mm,88*mm,H-97*mm))
para('<link href="'+URL+'#contatti" color="'+GREEN+'"><u>Passaporto: informazioni e contatti del progetto</u></link>',7,128,81,7,9)
finish();c.save()
# Printer spreads, two sides, 3 mm bleed and trim/fold marks outside bleed.
r=PdfReader(DIGITAL);writer=PdfWriter();SW,SH=590*mm,165*mm
for side in range(2):
 page=writer.add_blank_page(width=SW,height=SH)
 for j in range(6):
  src=r.pages[([0,1,2,3,4,11] if side==0 else [10,9,8,7,6,5])[j]];page.merge_transformed_page(src,Transformation().translate((10+j*95)*mm,10*mm))
 marks=HERE/'marks.pdf';m=canvas.Canvas(str(marks),pagesize=(SW,SH))
 if side==0:
  m.setFillColor(HexColor(GREEN));m.rect(7*mm,40*mm,3*mm,70*mm,fill=1,stroke=0)
  m.setFillColor(HexColor(AQUA));m.rect(7*mm,38*mm,3*mm,2*mm,fill=1,stroke=0)
 m.setLineWidth(.3);m.setStrokeColor(HexColor('#555555'))
 for x in [10,580]:
  for y in [10,155]:
   m.line((x-7 if x==10 else x+4)*mm,y*mm,(x-4 if x==10 else x+7)*mm,y*mm)
   m.line(x*mm,(y-7 if y==10 else y+4)*mm,x*mm,(y-4 if y==10 else y+7)*mm)
 for x in [105,200,295,390,485]:
  m.setDash(1.5,1.5);m.line(x*mm,3*mm,x*mm,6*mm);m.line(x*mm,159*mm,x*mm,162*mm)
 m.setDash();m.setFillColor(HexColor('#555555'));m.setFont('Regular',6);m.drawString(10*mm,2*mm,('FRONTE  01 02 03 04 05 12' if side==0 else 'RETRO  11 10 09 08 07 06')+'   |   570 x 145 mm   |   6 ante 95 mm   |   100%');m.save()
 page.merge_page(PdfReader(marks).pages[0]);page.trimbox=RectangleObject([10*mm,10*mm,580*mm,155*mm]);page.bleedbox=RectangleObject([7*mm,7*mm,583*mm,158*mm])
writer.add_metadata({'/Title':'Passaporto della Valle | Stampa fronte e retro','/Author':'Valle Soana'})
with open(OUT/'passaporto-della-valle.pdf','wb') as f:writer.write(f)
# A separate printer instruction sheet keeps production notes out of the tourist document.
c=canvas.Canvas(str(OUT/'passaporto-della-valle-istruzioni-stampa.pdf'),pagesize=(210*mm,297*mm))
W,H=210*mm,297*mm
text('PASSAPORTO DELLA VALLE',18,23,22,'ExtraBold',GREEN)
text('Scheda di produzione · 26 ottobre 2026',18,32,10,'Regular',MUTED)
y=46
for h,t in [
 ('Formato e supporto','Formato chiuso 95 × 145 mm. Aperto rifilato 570 × 145 mm. Sei ante uguali, cinque pieghe alternate a fisarmonica; dodici facciate. Carta naturale non patinata, bianca, 140-160 g/m², adatta a scrittura e timbri. Nessuna plastificazione. Fibra parallela alle pieghe; cordonatura consigliata.'),
 ('File di stampa','Due pagine PDF di 590 × 165 mm. TrimBox 570 × 145 mm, BleedBox con 3 mm di abbondanza; crocini esterni al taglio e tacche di piega. Stampa in scala 100%, senza adattamento, senza inversione speculare. Testi e QR vettoriali, font Inter incorporati, composizione originale dei loghi conservata. Colori RGB: conversione nel profilo della macchina a cura della tipografia. Non è un file certificato PDF/X.'),
 ('Imposizione fronte / retro','Fronte, da sinistra: 01 · 02 · 03 · 04 · 05 · 12. Retro, visto diritto, da sinistra: 11 · 10 · 09 · 08 · 07 · 06. Le coppie fisiche sono 01/06, 02/07, 03/08, 04/09, 05/10, 12/11. Voltare sul lato corto, mantenendo la testa in alto. Non riordinare le facciate.'),
 ('Piegatura e lettura','Con il fronte diritto, richiudere a fisarmonica le ante dietro la copertina 01, lasciandola esterna; 12 è il retro di copertina. Alternare il verso delle pieghe a 95, 190, 285, 380 e 475 mm dal taglio sinistro. Lettura: seguire i numeri 01-05 sul fronte; voltare e proseguire sul retro da 06 a 11, da destra verso sinistra. La facciata 12 chiude il percorso. Fare un campione fronte/retro prima della tiratura.'),
 ('Spazi e controlli di utilizzo','Timbri stagionali, esercizi e arrivi: riquadri 39 × 30 mm. Tre comuni: 81 × 24 mm. Convalide: 81 × 20 mm, con alternativa firma del referente. Tenere la timbratura entro i riquadri e lontano dalle pieghe. Se i timbri in uso sono più grandi, concordare un timbro compatibile o usare la convalida firmata.'),
 ('Contenuti e versione digitale','Contenuti ricavati da public/index.html del repository ViviSoana-Web, revisione 21aeb7f. Le soglie non specificate dal sito per inviti, iniziative e contributi restano affidate al referente autorizzato. I quattro spazi per gli arrivi non stabiliscono un requisito di quattro inviti. Il PDF digitale contiene le dodici facciate in ordine, segnalibri e collegamenti attivi.')]:
 y=para(h,18,y,174,12,15,GREEN,'Bold')+2;y=para(t,18,y,174,9,12)+7
c.save()
for filename in ['passaporto-della-valle.pdf','passaporto-della-valle-digitale.pdf','passaporto-della-valle-istruzioni-stampa.pdf']:
 shutil.copy2(OUT/filename,ROOT/'source-sites/site/assets'/filename)
print('Generated 3 PDFs')
