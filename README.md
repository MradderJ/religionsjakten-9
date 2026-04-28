# Religionsjakten 9

En fristående gamifierad träningsapp för religionskunskap i årskurs 9.

Appen är byggd som en enda statisk HTML-fil och körs **direkt i webbläsaren** med vanlig JavaScript. Den kräver ingen installation, ingen server och inget Python-runtime. Den fungerar lika bra på iPhone, iPad, Android och dator och kan hostas på GitHub Pages.

## Innehåll

- Frågor om världsreligioner, etik, livsfrågor, sekularisering, religionsfrihet och källkritik.
- Quizlägen: Världsreligioner, Etik och livsfrågor, Religion och samhälle, samt en blandad Prov-sprint.
- XP, nivåer, streaks, märken och dagliga missions.
- Mini-essä med checklista för att träna utvecklade resonemang.
- Ljust och mörkt tema (växlas i toppmenyn).
- Mobilanpassad layout.

## Integritet

- Appen samlar **inte** in personuppgifter och kräver ingen inloggning.
- All logik och spelstatus körs lokalt i din webbläsare. Inget skickas till någon server.
- Sidan laddar typsnitt från ett externt CDN för bästa typografi, men typsnitten är inte nödvändiga – appen fungerar även om de blockeras.

## Viktigt

Detta är inte officiellt material från Skolverket och ska ses som ett fristående träningsstöd.

## Körning

Öppna `index.html` direkt i en webbläsare, eller publicera repot via GitHub Pages och dela länken. Inga byggsteg behövs.

## Teknisk bakgrund

En tidigare version använde PyScript/Pyodide för att köra Python i webbläsaren. Det startade dock inte tillförlitligt på iPhone (lång nedladdning, höga minneskrav, blockerade web workers över vissa nät). För att appen alltid ska starta är spelmotorn nu skriven i vanlig JavaScript med samma frågebank, samma poängsystem och samma UI som tidigare.
