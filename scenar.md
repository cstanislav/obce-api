PREP: nastaviť Vivaldi ako default browser

# Webinár: Vytvorenie a nasadenie jednoduchého API
13.11. 2024 18:00 – 20:00

Táto prednáška vám poskytne praktické zručnosti a znalosti, ktoré sú nevyhnutné na vývoj a nasadenie moderných webových aplikácií a API. Naučíte sa používať technológie a postupy, ktoré sú cenené na trhu práce.

Dovoľte mi aby som vás aj ja privítal na dnešnom webinári.

Dnes si ukážeme vývoj aplikácie od návrhu až po nasadenie na server. Samotná aplikácia bude veľmi jednoduchá a v podstate bez využitia v reálnom svete, skôr sa budeme zameriavať na samotný postup vytvorenia aplikácie – návrh, založenie projektu, ako spravovať zdrojový kód, ako vytvoriť jednoduché API, ako vytvoriť databázu, ako do nej načítať dáta, ako používať Docker, nasadenie aplikácie na server a podobne. Neprekvapí ma, ak ste sa už niektorí stretli s vecami o ktorých budem hovoriť, ale dúfam, že si každý odtiaľto odnesie aspoň niečo nové, čo sa mu bude hodiť v praxi.

Seminár bude rozdelený na 3 časti – v prvej vytvoríme API, v druhej ju zabalíme do Docker kontajnera a nasadíme, a v tretej budete mať možnosť sa opýtať na čokoľvek, čo vás zaujíma, prípadne sa môžeme venovať niektorým konkrétnym témam podrobnejšie. Keďže toho musíme dnes veľa prebrať, poďme rovno na vec. U seba nemusíte robiť nič, stačí sledovať, dávať pozor a prípadne si písať poznámky a otázky.

Chceme vytvoriť projekt – môžeme začať tým, že si nájdeme nejaký zdroj otvorených dát, ktorý budeme spracovávať.

## Nájdenie zdroja otvorených dát

### Čo sú otvorené dáta a kde ich nájsť
> - Široký pojem – informácie a dáta zverejnené na internete, ľahko dostupné, strojovo čitateľné, používajúce štandardy s voľne dostupnou špecifikáciou, sprístupnené za jasne definovaných podmienok použitia dát s minimom obmedzení a dostupné užívateľom pri vynaložení minima možných nákladov.
> - Pochádzajú z univerzít, mimovládnych organizácií, súkromných firiem alebo verejnej správy
> - Cestovné poriadky, príjmy štátov, rozpočty, databázy, zoznam poskytovateľov sociálnych služieb, kalendár ministra alebo meranie čistoty ovzdušia
> - [Otevřená data - Wikipedie](https://cs.wikipedia.org/wiki/Otev%C5%99en%C3%A1_data)

#### Príklady populárnych zdrojov
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [data.gov.cz – ČR](https://data.gov.cz/)
- [data.jmk.cz – Jihomoravský kraj](https://data.jmk.cz/)
- [data.brno.cz – Brno](https://data.brno.cz/)
- ...

## Analýza dát
- Budeme sa zaoberať datasetom [Adresář obcí – Královéhradecký kraj](https://data.gov.cz/datov%C3%A1-sada?iri=https%3A%2F%2Fdata.gov.cz%2Fzdroj%2Fdatov%C3%A9-sady%2F70889546%2F9f2295911102f469bebb82ede1b3691a)
    - Královehradecký Kraj – Adresár obcí
    - formát: CSV (Comma Separated Values – hodnoty oddelené čiarkou)

- Stiahnuť dataset (manuálne) a otvoriť vo VS Code
    - ukázať, že je to obyčajný textový súbor
    - povedať, že sa dá otvoriť aj napr. v Exceli

- Pozrieť na dáta a rozhodnúť sa, že ideme vytvoriť API, ktoré má následujúce endpointy (**Excalidraw**):
    - `GET /obce` – vráti zoznam obcí podľa parametrov (okres - district, PSČ - zip_code)
- JSON objekt obce:
    - `id` – ID obce
    - `name` – názov obce
    - `district` – okres, v ktorom sa obec nachádza
    - `zip_code` – PSČ obce
    - `web` – webová stránka obce

## Založenie projektu

## Vytvorenie aplikácie s pomocou FastAPI
- Praktický príklad vytvorenia jednoduchého API
- na vytvorenie API v Pythone existuje viacero knižníc, my použijeme FastAPI
- upraviť main.py

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return "Hello World"
```

- fastapi je podčiarknuté, pretože túto knižnicu je potrebné nainštalovať
- dá sa nainštalovať cez ```pip install fastapi```, ale lepšie je zoznam potrebných knižníc uložiť do súboru `requirements.txt` a inštalovať ich naraz
- okrem fastapi potrebujeme aj knižnicu uvicorn
- vytvoriť súbor `requirements.txt` a pridať do neho `fastapi` a `uvicorn`

```
pip install -r requirements.txt
```
- pip nám vynadá, že máme použiť virtuálne prostredie
    - virtuálne prostredie je izolované prostredie, ktoré obsahuje všetky potrebné knižnice pre daný projekt, aby sa nestalo, že by sme si zmenili verziu knižnice pre jeden projekt a zmenili by sme ju aj pre iný projekt
- príkazy na jeho vytvorenie a aktiváciu máme v konzole 
- po vytvorení vidíme (venv) pred promptom
- znova nainštalovať requirements
- už funguje
- ale vo VS Code je možno stále podčiarknuté, lebo treba zreštartovať Python language server (reštart Code alebo F1 a Python: Restart Language Server)
- spustíme api príkazom `uvicorn obec-api.main:app --reload`
- otvoriť link v prehliadači, vidíme Hello World
- teraz keď už máme niečo vytvorené, môžeme to uložiť do Git repozitára

### Čo je Git?
- Systém na správu zdrojových kódov, ktorý umožňuje sledovať zmeny v kóde, spolupracovať s inými programátormi a udržiavať históriu zmien
- [Git – Wikipedie](https://cs.wikipedia.org/wiki/Git)
- [Git explained in 100 seconds](https://www.youtube.com/watch?v=hwP7WQkmECE)

### Vytvorenie Git repozitára
- Vytvoriť nový adresár pre projekt
- Otvoriť terminál v adresári
- Spustiť príkaz `git init`
- Ukázať vo VS Code Git Graph
- Ukázať, čo robí `git commit`
- Ísť na GitHub a vytvoriť nový repozitár (názov: `obce-hk-api`)
- Vytvoriť hello world (main.py, print "Hello, world!")
- stage, commit, push, ukázať v Git Graph
- ukázať na GitHube

- poďme sa teraz pozrieť na to, ako vytvoriť endpoint `GET /obce`
- najprv musíme načítať dáta z CSV súboru a uložiť ich do databázy. Najjednoduchšia moźnosť je použiť SQLite databázu

## Import dat do databáze (SQLite, PostgreSQL)
- SQLite je jednoduchá relačná databáza, ktorá je uložená v jednom súbore
- nie je vhodné otvorené dáta ukladať priamo do repozitára, pretože môžu byť aktualizované, alebo sa rozhodneme použiť iný zdroj, takže najprogramujeme aj samotné stiahnutie dát
- začať písať kód
- na stiahnutie dát môžeme použiť knižnicu `requests`, ktorú treba doinštalovať cez requirements.txt – pridáme, vypneme API (Ctrl+C), znova nainštalujeme requirements, spustíme API
- vidíme, že po uložení súboru sa API automaticky reštartuje
- dáta nebudeme sťahovať do .csv súboru, ale rovno ich uložíme do databázy, v súbore data.sqlite
    - naša tabuľka bude mať stĺpce:
        - `id` – ID obce (integer)
        - `name` – názov obce (text)
        - `district` – okres, v ktorom sa obec nachádza (text)
        - `zip_code` – PSČ obce (integer)
        - `web` – webová stránka obce (text)

```python
from fastapi import FastAPI
import requests
import sqlite3
import csv

DATA_URL = "https://www.datakhk.cz/api/download/v1/items/3ec5df3a89d7470ea40330baadca74f4/csv?layers=0"

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World"

def import_data():
    print("Importing data...")
    # Download data from DATA_URL and save to sqlite database
    response = requests.get(DATA_URL)

    # Create sqlite database
    conn = sqlite3.connect("data.sqlite")
    cursor = conn.cursor()

    # Create table
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT, district TEXT, zip_code TEXT, web TEXT)")

    # Insert data
    csv_file = response.text.splitlines()
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cursor.execute("INSERT INTO data (name, district, zip_code, web) VALUES (?, ?, ?, ?)", (row["Název obce"], row["Název okresu"], row["PSČ"], row["Webové stránky"]))
    conn.commit()
    conn.close()
    
    print("Data imported.")

import_data()
```

- po spustení vidíme, že sa vytvoril súbor data.sqlite
- aby sme sa mohli do databázy pozrieť, vieme vo VS Code použiť rozšírenie SQLite
    - keď je nainštalované, pomocou F1 otvoríme príkazovú paletu a použijeme príkaz SQLite: Open Database
    - potom ju vidíme v Exploreri dole v SQLite Explorer
    - dáta máme krásne načítané, môžeme sa pustiť do vytvorenia endpointu
- **predtým ale ešte commitneme zmeny do Gitu**
    - vidíme, že v tabe source control je veľa zmien, ktoré do repozitára nepatria (venv, data.sqlite), tak ich ignorujeme vytvorením súboru `.gitignore` a pridaním týchto riadkov:
    ```
    venv
    data.sqlite
    .DS_Store
    *.pyc
    ```
    - vytvoríme commit ("Implemented data ingestion"), commit+push
- nový endpoint:

```python
def map_data(row):
    return {
        "id": row[0],
        "name": row[1],
        "district": row[2],
        "zip_code": row[3],
        "web": row[4]
    }

@app.get("/obce")
def get_obce(district: str, zip_code: str):
    conn = sqlite3.connect("data.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, district, zip_code, web FROM data WHERE district = ? AND zip_code = ?", (district, zip_code))
    data = cursor.fetchall()
    conn.close()

    return list(map(map_data,data))
```
- poďme endpoint vyskúšať
- FastAPI automaticky generuje dokumentáciu api, dostupnú na adrese /docs
- kliknúť na endpoint /obce, Try it out, zadať parametre, Execute

## Prechod na PostgreSQL
- SQLite je vhodná pre jednoduché aplikácie a prototypy, ale pre produkčné aplikácie je lepšie použiť databázu ako PostgreSQL
    - je robustnejšia, podporuje viac súčasne pripojených klientov, má lepšie možnosti zálohovania a obnovy, lepšie možnosti zabezpečenia, lepšie možnosti optimalizácie, lepšie možnosti replikácie...
    - v tomto prípade by nebolo treba použiť vôbec žiadnu databázu, ale ide o demonštráciu
- **začnime tým, že si povieme niečo o Dockeri**
    - Docker je platforma na vývoj, doručovanie a spustenie aplikácií pomocou kontajnerizácie
    - kontajner je štandardizovaný spôsob balenia aplikácie a všetkých jej závislostí do jedného balíka, ktorý je možné spustiť na akomkoľvek systéme, ktorý podporuje Docker
    - kontajnery sú izolované, na rôznych systémoch sa správajú rovnako
        - takže v podstate eliminuje problémy typu "u mňa to funguje"
        - na produkčnom serveri môže bežať presne rovnaká aplikácia ako na našom počítači, s rovnakými závislosťami
    - Docker umožňuje spustiť kontajner na akomkoľvek systéme, ktorý podporuje Docker
    - výhoda je, že nemusíme inštalovať databázu na našom počítači, ale môžeme ju spustiť v kontajneri
    - existuje veľké množstvo aplikácií, ktoré je možné používať ako Docker kontajner, ako napríklad PostgreSQL, čím sa vyhneme zložitej inštalácií
- Docker sa dá jednoducho stiahnuť a nainštalovať z [Docker.com](https://www.docker.com)
- kontajnery môžeme spravovať buď cez aplikáciu Docker Desktop, alebo cez rozšírenie VS Code
- otvoriť rozšírenie
- po inštalácií môžeme jednoducho vytvoriť postgres kontajner jedným príkazom:
```
docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres
```
- databáza beží, poďme prepísať kód aplikácie
- requirements.txt: pridať psycopg2-binary
```python
import psycopg2
```

```python
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASS = "postgres"

def get_database_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        dbname="data"
    )
```
- nie je dobré mať prihlasovacie údaje a API kľúče priamo v kóde, ale pre jednoduchosť to tak zatiaľ necháme a prípadne sa k tomu môžeme vrátiť na konci

```python
@app.get("/obce")
def get_obce(district: str, zip_code: str):
    conn = get_database_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, district, zip_code, web FROM data WHERE district = %s AND zip_code = %s", (district, zip_code))
    data = cursor.fetchall()
    conn.close()
```

```python
    # Create PostgreSQL database
    conn = get_database_connection()
    cursor = conn.cursor()

    # Create table
    cursor.execute("CREATE TABLE IF NOT EXISTS data (id SERIAL PRIMARY KEY, name TEXT, district TEXT, zip_code TEXT, web TEXT)")

    # Insert data
    csv_file = response.text.splitlines()
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cursor.execute("INSERT INTO data (name, district, zip_code, web) VALUES (%s, %s, %s, %s)", (row["Název obce"], row["Název okresu"], row["PSČ"], row["Webové stránky"]))
    conn.commit()
    conn.close()
```
- spustíme aplikáciu
- ako vieme, že import prebehol správne? pozrieme sa do databázy, avšak teraz už nebudeme používať SQLite rozšírenie vo VS Code, ale Adminer
    - ten vieme tiež použiť ako Docker kontajner
    - príkaz na spustenie Adminera:
    ```
    docker run --name adminer -p 8081:8080 adminer
    ```
- v Admineri zadáme:
- host: host.docker.internal:5432
- postgres/postgres
- vidíme, že tabuľka s dátami existuje, ale obsahuje príliš veľa riadkov, viac riadkov než je vo vstupnom CSV súbore
    - napadá niekoho, prečo?
    - je to tým, že vždy po reštarte aplikácie sa dáta znova načítajú, avšak predtým databázu nevymažeme
```python
# Drop table if exists
cursor.execute("DROP TABLE IF EXISTS data")

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS data (id SERIAL PRIMARY KEY, name TEXT, district TEXT, zip_code TEXT, web TEXT)")
```
- uložíme, počkáme kým prebehne import, obnovíme stránku, a počet už sedí
- prejdeme si zmeny v Source Control tabe a commitneme ich + pushneme
- zatiaľ sa nám teda podarilo vytvoriť jednoduchú aplikáciu, ktorá načíta dáta do databázy a poskytuje jednoduchý endpoint na ich získanie
- teraz si dajme prestávku 10 minút a po nej sa pozrieme na to, ako vytvoriť aj zo samotnej aplikácie Docker kontajner a ako spúšťať viacero kontajnerov naraz
- a keď sa nám podarí spustiť viac kontajnerov naraz lokálne, pripojíme sa na server a aplikáciu nasadíme, aby bola dostupná na internete

## PRESTÁVKA 10 minút

## Kontejnerizácia aplikácie (Docker, Docker Compose)
- 10 minút uplynulo, tak pevne verím, že ste všetci pripravení pokračovať. Poďme sa teda pozrieť na to, ako môžeme našu aplikáciu zabalit do Docker kontajnera
- najprv si musíme vysvetliť pojmy:
    - Docker image (obraz) – šablóna, ktorá obsahuje všetko, čo je potrebné na spustenie kontajnera, vrátane operačného systému, aplikácie a jej závislostí
    - Docker container (kontajner) – inštancia Docker image, ktorá beží na hostiteľskom systéme
    - takže môžete mať jeden obraz (napr. databáza) a spustiť 4 rôzne kontajnery s touto databázou, každá napr. na inom porte
- My teraz ideme zadefinovať docker image, čo sa robí pomocou súboru Dockerfile
    - v Dockerfile sa definuje postup vytvorenia imageu
    - na začiatku je vždy za kľúčovým slovom FROM uvedený image, z ktorého náš image bude odvodený
        - image môže byť napríklad debian alebo ubuntu, alebo aj postgresql a adminer, ktoré sme už použili
        - dostupné imagey môžeme hľadať na [Docker Hub](https://hub.docker.com)
        - špecifickejšie imidže, napríklad adminer, zvyčajne vychádzajú z nejakého základného imidžu, napr. debian
            - [viď Adminer na Docker Hube](https://hub.docker.com/layers/library/adminer/latest/images/sha256-7b346bacc32a9fc9f0d434d0e14c875b9ec54c82b3ea47a87c925389291e67d1?context=explore)
        - my budeme vychádzať z Python imageu, ktorý je založený na Debiane
            - overíme cez
            ```bash
            docker run --entrypoint bash -it python:latest
            cat /etc/*-release
            ```
- Predstavte si, že máme počítač s čerstvo nainštalovaným Debianom a chceme na ňom spustiť naše API. Aký je postup? Nakopírujeme doň náš kód, nainštalujeme potrebné knižnice, a spustíme aplikáciu. A presne to isté musíme urobiť aj v Dockerfile
```Dockerfile
FROM python:latest

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Run uvicorn
CMD ["uvicorn", "obec-api.main:app", "--host", "0.0.0.0"]
```
- drobnosť – Docker vie identifikovať, ktoré súbory sa zmenili a ktoré nie, a tak pri každom buildovaní imageu buduje iba od miesta, kde sa zmena stala. Preto sa veľmi oplatí najprv kopírovať requirements.txt a inštalovať závislosti, a až potom kopírovať zvyšok kódu, pretože závislosti sa menia menej často a ich inštalácia môźe zaberať veľa času, obzvlášť ak ste na pomalšom internete
- teraz môžeme vytvoriť image
```
docker build -t obec-api .
```
- a spustiť kontajner
```
docker run -p 8000:8000 obec-api
```
- uistime sa, že databáza je spustená
- stále sa nedá pripojiť k databáze, pretože v containeri localhost už neznamená hostiteľský počítač, ale container samotný – zmenil sa kontext
    - zameníme za `host.docker.internal` (názov kontajnera)
- nesmieme zabudnúť, že nestačí len znova spustiť kontajner, ale treba aj znova vytvoriť image, inak by sme spúšťali starý kód
- po úspešnom spustení môžeme otvoriť prehliadač, zadať `localhost:8000/docs` a vyskúšať endpoint
- **nezabudnúť spraviť commit!!!**
    - podívať sa na Git Graph
- teraz ideme vyriešiť problém, že musíme spúšťať dve aplikácie naraz – našu aplikáciu a databázu
    - na to je ideálny Docker Compose – nástroj na definovanie a spúšťanie viackontajnerových aplikácií
    - definícia sa umiestňuje do súboru `docker-compose.yml`
```yaml
services:
  obec-api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 8000:8000
  postgres:
    image: postgres:latest
    environment:
      POSTGRES_PASSWORD: postgres
```
- spustíme
```
docker-compose up
```
- nedá sa pripojiť do databázy
    - zmeníme host na `hackathon-postgres-1` (názov kontajnera, vytvorený automaticky docker compose)
    - alebo na `postgres` a pridáme do docker-compose atribút `container_name: postgres`
- spustíme znova
```
docker-compose up --build
```
- vyskúšame na /docs, všetko funguje
- do compose si prípadne vieme hodiť aj Adminera
```yaml
  adminer:
    image: adminer
    ports:
      - 8081:8080
```
- **commit!!!**

## BONUS: ako pripojiť pekný frontend
- vytvoríme si zložku client, index.html
```html
<!DOCTYPE html>
<html>
  <head>
    <title>My App</title>
  </head>
  <body>
    <div id="app">
      <h1>My App</h1>
      <p>My app is running!</p>
    </div>
  </body>
</html>
```
- záleží na poradí definícií, definovať až za get /obce
```python
# Serve static files from /client
app.mount("/", StaticFiles(directory="client", html=True), name="client")
```
- reštart, kontrola či funguje, commit
- v zložke client môžete mať napr. React aplikáciu, ktorej build sa nachádza v /client/dist, a túto zložku môžete servovať cez FastAPI tak ako sme si ukázali
- vzor ako vytvoriť mini frontend (form, button, fetch) a zavolať endpoint
```html
<!DOCTYPE html>
<html>
  <head>
    <title>My App</title>
  </head>
  <body>
    <div id="app">
      <h1>My App</h1>
      <form id="form">
        <label for="district">District:</label>
        <input type="text" id="district" name="district">
        <label for="zip_code">ZIP code:</label>
        <input type="text" id="zip_code" name="zip_code">
        <button type="submit">Submit</button>
      </form>
      <div id="result"></div>
    </div>
    <script>
      document.getElementById("form").addEventListener("submit", async (event) => {
        event.preventDefault();
        const district = document.getElementById("district").value;
        const zip_code = document.getElementById("zip_code").value;
        const response = await fetch(`/obce?district=${district}&zip_code=${zip_code}`);
        const data = await response.json();
        document.getElementById("result").innerText = JSON.stringify(data, null, 2);
      });
    </script>
  </body>
</html>
```
- CORS? pozor na akej URL som v prehliadači (mala by byť localhost)
- **COMMIT!!!**

## Nasazení aplikace na VPS
- Čo je virtuálny privátny server (VPS) a ako funguje
    - VPS je virtuálny server, ktorý beží na fyzickom serveri, ale je izolovaný od ostatných VPS na tom istom fyzickom serveri
    - VPS je možné spravovať ako fyzický server – inštalovať naň softvér, spúšťať aplikácie, spravovať databázy, atď.
    - výhoda: je lacnejší ako fyzický server, ale máme na ňom plnú kontrolu
- Dobré bezplatné VPS
    - https://www.vas-hosting.cz/
        - 7 dní zdarma
    - https://www.oracle.com/cloud/free/ - Oracle Cloud
        - 24 GB RAM, 4 CPU, 200 GB disk, navždy free
        - treba zadať údaje z kreditnej karty, ale nič sa neúčtuje
    - https://azure.microsoft.com/en-us/pricing/free-services - Azure Cloud
        - 100 USD kredit pre študentov
        - nejaké always free zdroje
        - nie iba VPS, ale aj iné služby, napr. databázy, alebo služby súvisiace s AI. Prakticky čokoľvek

### Kroky k nasadeniu aplikácie na VPS
- Aplikácie sa dajú nasadiť mnohými spôsobmi, toto je jeden z jednoduchších
    - v skutočnosti sa často používajú zložitejšie cloudové služby, ako napr. AWS, Azure, s infraštruktúrou definovanou pomocou Terraformu, alebo možno ste už počuli Kubernetese. Jednotlivé kroky nasadenia vykonáva pipeline (GitHub Actions, GitLab CI/CD, ...)
- my si na VPS zriadime prístup ku Git repozitáru, stiahneme kód, nainštalujeme Docker a Docker Compose, a spustíme aplikáciu
- Postup môže veľmi závisieť od konkrétneho hostingu a operačného systému na serveri (firewall)
- treba sa zaregistrovať na nejakom hostingu, vytvoriť VPS a získať prístupové údaje na SSH (IP adresa, používateľské meno, heslo)

```
NazevServeru: – test doma
#112089
89.203.249.103
root
0UpL5RT1theyf7Yo

obec1: – seminár
#112088
89.203.248.141
root
0UpL5RT1theyf7Yo
```
- otvoriť terminál, pripojiť sa na server ako root
```
ssh root@89.203.249.103
```
- vytvoriť nového používateľa, ktorý bude spúšťať aplikáciu
```
adduser obec
```
- apt-get install sudo -y
- usermod -aG sudo obec
- log out, log in as obec
```
ssh obec@89.203.249.103
```
- nainštalovať Docker
- https://docs.docker.com/engine/install/debian/
- https://docs.docker.com/engine/install/linux-postinstall/

### SSH prístup do repozitára
- ak je projekt verejný, nemusíme sa autentizovať, ale ak je súkromný, musíme sa autentizovať
- na serveri vygenerujeme SSH kľúče (súkromný a verejný)
- súkromný kľúč si necháme na serveri, verejný kľúč pridáme do repozitára
```
ssh-keygen -t ed25519
```
- vypísať verejný kľúč
```
cat ~/.ssh/id_ed25519.pub
```
- GitHub -> Settings -> SSH and GPG keys -> New SSH key
- na serveri: git clone git@github.com:cstanislav/obce-hk-api.git
- `cd obce-hk-api`
- `docker-compose up -d`
    - -d = detach, spustí v pozadí, takže môžeme zavrieť terminál
- možné vylepšenia:
    - nastaviť, aby sa aplikácia spúšťala automaticky po reštarte servera
        - vytvoriť systemd service
    - spojazdniť aplikáciu na vlastnej doméne (obce-hk-api.cz)
    - nastaviť, aby sa aplikácia spúšťala na HTTPS
- 89.203.248.141:8000
- ak nefunguje, treba otvoriť port
    - ```sudo apt install ufw```
    - ```sudo ufw allow 8000```
## Užitečné nástroje a zdroje
- Figma
