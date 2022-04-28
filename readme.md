# **candyCalc**
## **Tymovy projekt IVS**

Pro vyvoj kalkulacky jsme vybrali jazyk Python. Uzivatelske rozhrani je vytvoreno programem Qt Creator.

Prostredi
---------

Ubuntu 64bit
Windows 64bit

Autori
------

candyCalc
- xstrel03 Matyas Strelec
- xkurci00 Julia Kurcikova 
- xseidl06 Ondrej Seidl 
- xnovym00 Maxmilian Novy 

Zavislosti
----------

Nasledujici prikazy jsou pro Ubuntu Linux. Na Windows lze pouzit obdobne prikazy.
Pro uspesne rucni spusteni je potreba zavislosti `python3` a `PyQt5`. Pro nainstalovani je potreba i `pip3`.
Zavilosti se nainstaluji provedenim prikazu v adresari `src`:

    make dependencies

Nebo rucne pomoci nasledujicich prikazu:

    apt install python3
    apt install pip3
    pip3 install PyQt5


Rucni spusteni
--------------

Nasledujici prikazy jsou pro Ubuntu Linux. Na Windows lze pouzit obdobne prikazy.
Program je psany v jazyce Python, tedy neni potreba kompilace.
Po rozbaleni slozky `ivs-calculator` provedte pro spusteni nasledujici prikazy v adresari `src`:

    python3 main.py

Sestaveni spustitelneho programu
--------------------------------

Spustitelne soubor nezavisly na zavislostech lze sestavit programem `PyInstaller`.
Sestaveni spustitelneho provedenim prikazu v adresari `src`:

    make build

Nebo rucne pomoci nasledujicich prikazu:

    python3 -m PyInstaller pyinstaller.spec

Tentoprogram vytvori slozku `dist`, ve ktere se mimo knihoven a datovych souboru bude nachazet
soubor `candycalc` na Ubuntu nebo `candycalc.exe` na Windows.

Instalace
---------

Program lze nainstalovat spustenim souboru `candycalc-install.deb` pro Ubuntu, nebo `candycalc-install.exe` pro Windows.
Blizsi postup instalace je popsan v uzivatelske prirucce.

Licence
-------

Tento program je svobodny software: muzete jej sirit a upravovat podle ustanoveni Obecne verejne licence GNU (GNU General Public Licence), vydavane Free Software Foundation a to bud podle 3. verze teto Licence, nebo (podle vaseho uvazeni) kterekoli pozdejsi verze.

Tento program je rozsirovan v nadeji, ze bude uzitecny, avsak BEZ JAKEKOLIV ZARUKY. Neposkytuji se ani odvozene zaruky PRODEJNOSTI anebo VHODNOSTI PRO URCITY UCEL. Dalsi podrobnosti hledejte v Obecne verejne licenci GNU.

Kopie Obecne verejne licence GNU je v soboru licence.md. Take ji najdete zde: <http://www.gnu.org/licenses/>.