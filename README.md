# 📝 Izluščanje vprašanj in odgovorov iz HTML datoteke

To je enostavna Python aplikacija, ki iz ARNES KVIZ HTML datoteke izlušči vsa vprašanja in pravilne odgovore ter jih shrani v `.txt` datoteko.
Dodatna vprašanja in predlogi posodobitve: https://github.com/ticbudjalol/Izvoz_Vprasanj_arnes/issues

---

## ⚙️ Namestitev

Pred uporabo se prepričajte, da imate nameščen **Python 3**. Prav tako potrebujete knjižnico **BeautifulSoup** (`bs4`) za obdelavo HTML.

1. **Namestite Python knjižnice**:
   ```bash
   pip install beautifulsoup4 lxml
   ```

2. **Prenesite kodo v svojo mapo** ali klonirajte GitHub repozitorij:
   ```bash
   git clone https://github.com/UPORABNISKOIME/Izvoz_Vprasanj_arnes.git
   cd ime-repozitorija
   ```

---

## 📌 Kako uporabiti?

1. **Odpri kviz na učnilnici arnes.
2. **Na koncu povezave v kvizu dodaj `&showall=1` (https://ucilnice.arnes.si/mod/quiz/review.php?attempt=000000&cmid=000000&showall=1)
3. **Shanite HTML datoteko celotnega** (npr. `index.html`) v isto mapo kot skripto.
4. **Zaženite Python skripto**:
   ```bash
   python app.py
   ```
5. Skripta bo poiskala vsa vprašanja in pravilne odgovore ter jih zapisala v datoteko **`izvoz_vprasanja.txt`**.

---

## 📝 Primer izpisa (`izvoz_vprasanja.txt`)

```
Vprašanje 1: Katera vrsta datotečnega sistema je primarna na MS Windows operacijskih sistemih?
Odgovor: FAT32, NTFS

Vprašanje 2: Katera tehnologija se uporablja za brezžično povezavo med napravami na kratkih razdaljah?
Odgovor: Bluetooth
```

---

DELUJE SAMO ZA REŠENE KVIZE KJER SO PRIKAZANI ODGOVORI NA VPRAŠANJA
Primer ustrezne povezave:
(https://ucilnice.arnes.si/mod/quiz/review.php?attempt=000000&cmid=000000&showall=1)


