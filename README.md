# Religionsjakten 9

En fristående träningsapp för religionskunskap i årskurs 9 och inför nationella provet. **200 unika flervalsfrågor** på svenska – inget annat. Helt mobilanpassad och körs direkt på iPhone utan installation.

## Innehåll

- **200 frågor** om världsreligioner (judendom, kristendom, islam, hinduism, buddhism, sikhism, shinto m.fl.), etik och livsfrågor, religion och samhälle, sekularisering, religionsfrihet i Sverige, källkritik, begrepp, ritualer, urkunder, jämförelse, identitet, samt konflikt och fred.
- Fyra svarsalternativ per fråga, ett rätt svar.
- Direkt feedback med förklaring efter varje svar.
- Kategorier: alla, världsreligioner, etik & livsfrågor, religion & samhälle, begrepp & källkritik.

## Belöningar

Allt drivs uteslutande av att svara på frågor – inga essäer, uppdrag eller storyworlds.

- **Poäng** per rätt svar med streak-bonus (3, 5, 10).
- **Streak**-räknare med rekord och små animerade gnistor när du svarar rätt.
- **Märken/achievements** som låses upp efter hand: första svaret, streak 3/5/10, 10/50/100 rätt, poängmilstolpar 500 och 1500, hela rundan, samt felfri runda.
- **Slutsummering** med antal rätt, träffsäkerhet, bästa streak och total poäng.
- Motiverande mikrokopia ("Snyggt!", "Du brinner!") och toast-meddelanden.

## UI

- Frågans nummer av totalen, framstegsmätare, kategori-väljare.
- Svarsknappar med tydlig markering rätt/fel.
- Knappar för **nästa fråga**, **blanda om**, **starta om**.
- Slutkort med möjlighet att spela igen.

## Snabb och iPhone-vänlig

- Ingen PyScript, ingen Pyodide, inga CDN, inga Google Fonts eller Fontshare.
- Inline vanilla JavaScript och CSS i `index.html`. Använder systemets typsnitt.
- Startar omedelbart även på långsamma mobilnät.

## Integritet

- Inga personuppgifter, ingen inloggning, inga cookies, ingen serverkommunikation.
- All spelstatus körs lokalt i webbläsaren och försvinner när du laddar om.
- Inga externa resurser laddas alls.

## Körning

Öppna `index.html` direkt i en webbläsare, eller publicera repot via GitHub Pages och dela länken. Inga byggsteg, ingen installation, ingen konfiguration behövs.

## Tester

Kör `python3 test_quiz.py` för att verifiera att frågebanken är intakt:

- exakt 200 frågor
- alla frågetexter unika
- fyra alternativ per fråga
- giltiga svarsindex
- inga rester av mini-essä, story-world, uppdrag eller externa beroenden

## Tidigare version

Den ursprungliga, mer omfattande versionen med XP, mini-essä och uppdrag finns kvar i `full.html` för referens. Den är **inte** den huvudsakliga, snabba GitHub Pages-startsidan.

## Viktigt

Detta är inte officiellt material från Skolverket utan ett fristående träningsstöd.
