Kāpēc mobilā aplikācija “SOS” ir distributīvā sistēma?
Balstoties uz **A. Tanenbauma** definīciju, distributīvā sistēma ir mijiedarbojošu 
programmatūras komponentu kopums, kas darbojas vienā vai vairākos savienotos datoros 
un no lietotāja viedokļa izskatās kā vienots veselums. Distributīvās sistēmās viena līmeņa 
programmas funkcijas var izplatīties starp vairākiem datoriem. 

Lietotnes “SOS” kvalitatīvai funkcionēšanai ir jāstrādā kopā 4 tas daļas – serveris, 
kurš saņem informāciju no lietotāja, datu bāze, kura glabā visu informāciju par 
lietotājiem, administratora interfeiss, ar kuru viņš pārvalda informāciju un izsaukumus un, 
protams, klienta interfeiss ar izsaukuma taustiņiem un atbalsta logu; tomēr, 
pēc klienta viedokļa programma strādā kā vienots veselums.

Pamatojoties uz divu vienību mijiedarbības aprakstu, mēs uzskatām vispārēju klienta-servera 
mijiedarbības modeli, kurā viena no pusēm (klients) uzsāk datu apmaiņu, nosūtot 
pieprasījumu otrai pusei (serverim). Serveris apstrādā pieprasījumu un, ja nepieciešams, 
nosūta atbildi klientam.

Lietotne “SOS” balstās uz Python Socket server un client.

![Image one](https://raw.githubusercontent.com/sos-ds/DS/master/Presentations/1.jpg)

Mijiedarbība klienta-servera modelī var būt sinhrona, ja klients gaida, lai serveris apstrādātu 
pieprasījumu, vai asinhronais, kurā klients nosūta pieprasījumu serverim un turpina izpildi, 
negaidot servera atbildi. Klientu un servera modeli var izmantot kā pamatu dažādu mijiedarbību aprakstīšanai.

![Image two](https://raw.githubusercontent.com/sos-ds/DS/master/Presentations/2.jpg)

Apsveriet tipisku lietojumprogrammu, kas saskaņā ar mūsdienu koncepcijām var iedalīt 
šādos loģiskos līmeņos: lietotāja interfeiss (LI), lietojumprogrammu loģika (LP) un piekļuve 
datiem (PD), strādājot ar datu bāzi (DB). Sistēmas lietotājs mijiedarbojas ar to, izmantojot 
lietotāja interfeisu, datu bāze glabā datus, kas apraksta lietojumprogrammas domēnu, un 
lietojuma loģikas līmenis īsteno visus algoritmus, kas saistīti ar tematu.

Mobilā aplikācija “SOS” sastāv no servera ar datubazi un klienta intefeisu ar izsaukuma taustiņiem un atbalsta logu.

Tā kā praksē dažādi sistēmas lietotāji parasti ir ieinteresēti piekļūt vieniem un tiem pašiem 
datiem, šīs sistēmas funkciju vienkāršākā nošķiršana starp vairākiem datoriem būs 
lietojumprogrammas loģisko līmeņu nošķiršana no vienas lietojumprogrammas servera 
daļas, kas atbild par piekļuvi datiem un klientu daļām, kas atrodas vairākos datoros. 

![Image three](https://raw.githubusercontent.com/sos-ds/DS/master/Presentations/3.jpg)

Uz šo principu balstīto lietojumprogrammu arhitektūru sauc par klienta-serveri vai 
divvirzienu. Praksē šādas sistēmas bieži netiek klasificētas kā distributīvās, bet oficiāli tās var 
uzskatīt par vienkāršāko distributīvās sistēmu pārstāvju.

Lai sasniegtu mērķi - lai uzlabotu lietotāju pieprasījumu izpildi, distributīvai sistēmai jāatbilst 
noteiktām nepieciešamajām prasībām.

**Atklātība.** Visiem komponenta mijiedarbības protokoliem izkliedētā sistēmā ideālā gadījumā 
būtu jābalstās uz publiski pieejamiem standartiem. Katram komponentam ir jābūt precīzai 
un pilnīgai tās pakalpojumu specifikācijai. Šādā gadījumā sadalītās sistēmas komponentus 
var izveidot neatkarīgi izstrādātāji. Ja šī prasība tiek pārkāpta, var izzust iespēju izveidot 
sadalītu sistēmu, kas aptver vairākas neatkarīgas organizācijas.

Lietotne “SOS” tika izveidota saskaņā ar Python 3 specifikācijām, un to var uzskatīt par atklātu.

**Mērogojams.** Iespēja pievienot distributīvai sistēmai jaunus datorus, lai palielinātu sistēmas 
veiktspēju, kas ir saistīta ar slodzes līdzsvarošanas sistēmu  (load balancing)  serveros. 
Mērogošana ietver arī jautājumus, kas saistīti ar servera resursu efektīvu sadali, kas apkalpo 
klientu pieprasījumus.

Lietotnes “SOS” datubāzi laika gaitā var paplašināt, reģistrējot reģistrējot jaunus klientus no 
visiem Latvijas reģioniem.

**Saglabāt loģisko datu integritāti.** Izmantotajam pieprasījumam sadalītajā sistēmā ir vai nu 
pareizi, vai arī pilnībā jāpilda. Sliktākā ir situācija, kad daļa no sistēmas sastāvdaļām pareizi 
apstrādā ienākošo pieprasījumu un daļu.

Ja “SOS” programma nedarbojas, klienta daļa rada kļūdu.

Ilgtspējība. Stabilitāte attiecas uz iespēju, ka vairāki datori var dublēt vairākas tās pašas 
funkcijas, vai iespēju automātiskai funkciju sadalei sistēmā, ja kāds no datoriem neizdodas. 
Ideālā gadījumā tas nozīmē, ka nav pilnīgi unikāla neveiksmes punkta, proti, jebkura datora 
kļūme neļauj neiesniegt lietotāja pieprasījumu.

Reālajā dzīvē šāda programma kā "SOS" būtu oficiālā Latvijas Republikas veselības sistēma, 
piemēram, kā " E-veselība", un būtu milzīgs tehniskais atbalsts.

**Drošība.** Dati, kas tiek pārsūtīti starp komponentiem, ir jāaizsargā no trešām personām 
gan no izkropļojumiem, gan no trešās puses pārlūkošanu.

**Efektivitāte.** Šaurā izpratnē, kā tas attiecas uz sadalītajām sistēmām, efektivitāte tiks 
saprasta kā minimālās izmaksas, kas saistītas ar sistēmas sadalīto raksturu. Tā kā efektivitāte 
šajā šaurajā nozīmē var būt pretrunā ar sistēmas drošību, atvērtību un uzticamību, jāatzīmē, 
ka efektivitātes prasība šajā kontekstā ir vismazākā prioritāte. 




