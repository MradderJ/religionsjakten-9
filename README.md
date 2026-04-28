# Religionsjakten 9

En fristående gamifierad träningsapp för religionskunskap i årskurs 9.

## Två versioner

- **`index.html` (snabbstart, standard på GitHub Pages):** En lättviktig mobilanpassad version utan **några** externa resurser. Inga typsnitt, ingen CDN, ingen PyScript/Pyodide. Använder systemets typsnitt och startar omedelbart även på iPhone över långsamma nät. Visar ett synligt statusmeddelande när quizmotorn är redo.
- **`full.html` (full version):** Den ursprungliga, mer polerade versionen med Fontshare-typsnitt och utökad design. Länkad från snabbstartens sidfot.

## Innehåll (båda versionerna)

- Frågor om världsreligioner, etik, livsfrågor, sekularisering, religionsfrihet och källkritik.
- Quizlägen: Världsreligioner, Etik och livsfrågor, Religion och samhälle, samt en blandad Prov-sprint.
- XP, nivåer, streaks, märken och dagliga uppdrag.
- Mini-essä med checklista för att träna utvecklade resonemang.
- Mobilanpassad layout.

## Integritet

- Inga personuppgifter, ingen inloggning, ingen serverkommunikation.
- All spelstatus körs lokalt i din webbläsare.
- Snabbversionen laddar **inga** externa resurser alls.

## Körning

Öppna `index.html` direkt i en webbläsare, eller publicera repot via GitHub Pages och dela länken. Inga byggsteg behövs.

## Teknisk bakgrund

En tidigare prototyp använde PyScript/Pyodide för att köra Python i webbläsaren. Det startade inte tillförlitligt på iPhone (lång nedladdning, höga minneskrav, blockerade web workers över vissa nät). Snabbstarten är därför skriven som ren vanilla JavaScript inline i HTML-filen — samma frågebank, samma poängsystem, samma kärnfunktioner.

## Viktigt

Detta är inte officiellt material från Skolverket och ska ses som ett fristående träningsstöd.
