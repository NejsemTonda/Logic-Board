# Zápočtový program Václav Krňák
toto je zápočtový program na progrmování NPRG030-062
jedná se o celulární automat na simulaci elektrických obvodů 
> **Motivace:** Chtěl bych ukázat jak jednoduchá logika tranzistorů a diod dokáže vytvořit komplexní obvod

# Spouštění programu
program se spustí z příkazové řádky příkazem `python main.py` 

> požadavek pro spuštění programu je mít obrazovky s rozlišením aspoň 1800x1000, jinak je třeba změnit řadek self.screen = pygame.display.set_mode((x,y)) v souboru main.py na požadované hodnoty

# Uživatelská dokumentace
## Koncept
Jedná se o diskrétní simulaci světa, tudíž simulace probíhá v krocích.
Svět simulace je rozdělen na čtvercovou mřížku a v každém čtverečku může být nějaká buňka, která ovlivňuje svoje 4 sousedy.
Buňky mohou být buď žívé nebo mrtvé, základní myšlenkou simulace je, že buňka, která je živá, oživí všechny své neživé sousedy. Ty pak v příštím kroku simulace udělají to samé.


## Ovládání
Buňky do jednotlivých políček můžeme vkládat klikáním levého tlačítka myši.
K výběru typu buňky slouží výběrové kolečko, které se otevře stisknutím "**e**" a zavře stiknutím stejného tlačítka nebo vybráním buňky pomocí kliknutí myši.
Logika některých buňek se může měnit na základě jejich orientace, kterou lze změnit stisknutím "**r**".
Jakou buňku a s jakou orientací je vkládáme, slouží rychlý náhled, který je zobrazen pod ukazateleme myši.
Pro lepší orientaci ve světě můžeme kolečekem přibližovat a oddalovat náhled a pravým tlačítkem myši ho zase posouvat.

## Buňky 
### Wire
![wire](/docs/pics/wire.png)

Buňka **wire** neobsahuje žádnou specilání logiku. Pokud je **wire** živý, ožíví své sousedy, pokud je buňka mrtvá déle než čtyři kroky simulace, může být znovu oživena.
Pro vizualizaci toho, kdy může být **wire** zase oživen, slouží barevná indikace: červená znamená, že **wire** je živý, blednutí této barvy inidukuje uplynutý čas, pokud je **wire** opět bílý, může být oživen.

![wire_interaction](/docs/pics/wire.gif)
### Diode
![diode](/docs/pics/diode.png)

Buňka **diode** slouží jako jednosměrný převaděč informace. Může nabývat 4 různých orientací a vždy vede proud pouze ve směru své orientace.
Logika **diode** je zařízená tak, že vede proud rychleji než obyčejný [**wire**](#wire).
Jedna **diode** však nepředává informaci přímo druhé. Kombinaci **diode** a [**wire**](#wire) může dosáhnout větší rychlosti, pokud je to potřeba.

![diode_fast](/docs/pics/diodespeed.gif)

### Tranzistor
![tranzistor](/docs/pics/tranzistor.png)

Buňka **Tranzistor** je hlavní logickou buňkou této simulace. Může nabývat 2 orientací a 2 stavů. 
Stav *blocked* kdy je **tranistor** na přístích 8 kroků simulace zablokovaný a nevede proud a stav *non blocked* kdy se tranzistor chová jako třída [**wire**](#wire)
Při svislé orientaci a se **tranzistor** zablokuje, pokud byl oživen buňkou shora nebo zdola.
Při vodorovné orientaci tomu je obráceně.
Zda je **tranzistor** zablokovaný nebo ne, indikuje jeho zabarvení: šedá znamená *blocked* a bíla *non blocked*

![tranzistor_not_blocked](/docs/pics/tranzistor.gif)
![trazistor_blocked](docs/pics/tranzistorblocked.gif)

## Nástroje
### Remove
![Remove](/docs/pics/remove.png)

Tento nástroj nalezneme ve [výběrovém kolečku](#ovl%C3%A1d%C3%A1n%C3%AD).

Slouží k odstranění buňky 

### Revive
![Revive](/docs/pics/alive.png)

Tento nástroj nalezneme ve [výběrovém kolečku](#ovl%C3%A1d%C3%A1n%C3%AD).

Slouží k oživení buňky 

### Copy
Pomocí tohoto nástroje můžeme kopírovat více buněk najedou. Pro jeho použítí stikněte klávesy `ctrl+c` a výběrovým čtvercem označte buňky, které chcete kopírovat.
Následně je můžete vložit pomocí nástroje [**Paste**](#paste)

### Paste
Slouží pro vkládání více buňek najednou, pro použití stikněte `ctrl+v`. Objeví se náhled pro vložení buňky, levým tlačítkem myši buňky vložíte

### Store
Tímto nástrojem lze uložit zkopírované buňky do textového souboru, ze kterého je lze později načíst pomocí nástroje [**Load**](#load).
Po stisknutí kláves `ctrl+s` je třeba do příkazového řádku napsat název souboru, do kterého si přejete buňky uložit

### Load 
Tento nástroj slouží k načítaní dříve uložených souborů. Po stisknutí kláves `ctrl+l` se do příkazového řádku vypíší dostupné soubory a jejich pořadová čísla. 
Po zvolení pořadového čísla se buňky ze souboru načtou jako při používání nástroje [**Paste**](#paste)

## [Programátorská dokumentace](https://github.com/NejsemTonda/Logic-Board/blob/main/docs/prgDocumentation.md)
