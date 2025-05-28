# **Festak Argazki Deskargatzailea**

`festak.py` da `festak.com` webguneko argazki albumak osorik deskargatzeko script bat. Album bakoitzak duen kode espezifikoa erabiliz, bertako argazki guztiak zure ordenagailuan gordetzeko aukera ematen du.

## **Deskribapena**

Script honek `festak.com` webguneko album batetik argazki guztiak modu automatizatuan jaisten ditu. Horretarako, albumaren URLean agertzen den `ev` parametroaren balioa (kodea) erabili behar da.

## **Baldintzak**

Scripta exekutatzeko **Docker** instalatuta izatea beharrezkoa da.

## **Erabilera**

Jarraitu pauso hauek album bat deskargatzeko:

#### **1. Lortu albumaren kodea**
Nahi duzun albumaren URLa ireki nabigatzailean. Kodea `ev=` parametroaren ondoren agertzen den balioa da.

* **Adibidez**, URL hau bada:
    `https://festak.com/evento.php?ev=KODEA_ADIBIDEA`
* Zure kodea `KODEA_ADIBIDEA` izango litzateke.

#### **2. Exekutatu scripta**
Ireki terminal bat eta exekutatu komando hau, `<kodea>` zure albumaren kodearekin ordezkatuz:

```bash
docker run --rm -v "$(pwd)":/app -w /app python:3.10-slim sh -c "pip install -r requirements.txt > /dev/null && python festak.py <kodea>"
```

#### **3. Emaitza**

Deskargatutako argazkiak `images` izeneko karpeta baten barruan gordeko dira. Karpeta horren barruan, zure albumaren kodearekin izendatutako beste karpeta bat sortuko da, eta bertan egongo dira argazki guztiak.

Adibidez, honako karpeta-egitura hau sortuko da:

```
.
├── images/
│   └── KODEA_ADIBIDEA/
│       ├── argazkia_1.jpg
│       ├── argazkia_2.jpg
│       └── ...
├── festak.py
└── requirements.txt
```