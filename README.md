# Véges Test Primitív Elem Számoló

## Használat
- Telepitsd fel a pythont
- Másold a repot vsc-be (vagy más code editor-ba)
- Nyomj f5-öt a futtatáshoz (válaszd ki a python debuggert)
- A terminálban add meg a test rendjét
- A számolás végén "i" (igen) vagy "n" (nem) betük megadásával kiirathatod az ellenőrző hatványokat

# Müködés
1. **A rend felbontása:** 
   Először vesszük a $h = Q - 1$ értéket, és szétkapjuk prímekre és hatványaikra:
   $$h = p_1^{r_1} \cdot p_2^{r_2} \dots$$

2. **Ellenőrző polinomok:** 
   Minden egyes prímfaktornál megnézzük ezt a polinomot: 
   $$f_i(x) = x^{h/p_i} - 1$$
   Olyan számot ($\beta$) keresünk, ami behelyettesítve **nem 0** (vagyis a maradék nem 1 a testben).

3. **Komponensek gyártása ($\alpha_i$):** 
   Ha megvan a jó $\beta$, ebből gyártunk egy "rész-elemet" az adott prímágon:
   $$\alpha_i = \beta_i^{h/p_i^{r_i}} \pmod{Q}$$

4. **A végső összerakás:** 
   A végén nincs más dolgunk, mint ezeket az $\alpha_i$ értékeket összeszorozni:
   $$\alpha = \alpha_1 \cdot \alpha_2 \cdots \alpha_k \pmod{Q}$$


 ---

### Források és képletek
A feladat megoldásához és a matematikai háttér kidolgozásához az alábbi forrást használtam:
* **[Matematikai alapok 2 (PDF)](https://elearning.uni-miskolc.hu/zart/course/view.php?id=5300)** – A képletek és a szisztematikus felépítés algoritmusa ebből a segédletből származik.

### ⚠️ Disclaimer
Ez a program egyetemi segédletnek készült. Bár a kiszámolt eredményeket és a levezetést ellenőriztem (a programba épített hatvány-ellenőrzővel is), mindenki saját felelősségére használja! A kódban előfordulhatnak kerekítési sajátosságok vagy speciális esetek, amikre érdemes figyelni.




<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>
