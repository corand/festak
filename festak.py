#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
import sys
import time
from bs4 import BeautifulSoup
import progressbar
from urllib import request as urllib_request

if len(sys.argv) < 2:
    print("Errorea: Sartu bilduma kodea komandoaren argumentu gisa (adib: python descargador.py 3835)")
    sys.exit(1)
kodea = sys.argv[1]

directory = os.path.join('images', kodea)
os.makedirs(directory, exist_ok=True)


s = requests.Session()
s.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})

try:
    url_principal = f"http://www.festak.com/visor5.php?mt=1&pag=p&ev={kodea}"
    print(f"'{kodea}' bildumako orriak bilatzen...")
    r = s.get(url_principal)
    r.raise_for_status()
    soup_principal = BeautifulSoup(r.text, 'html.parser')

    botonera = soup_principal.find("div", {"class": "botonera"})
    if not botonera:
        print(f"Ezin izan da '{kodea}' bilduma aurkitu. Egiaztatu kodea zuzena dela.")
        sys.exit(1)
    botoiak = botonera.find_all("a")
    print(f"{len(botoiak)} orri aurkitu dira.")

    lista_de_imagenes = []
    print("Orri guztiak aztertzen irudiak zenbatzeko...")
    for botoi in botoiak:
        link_pagina = f"http://www.festak.com/{botoi['href']}&ev={kodea}"
        req_pagina = s.get(link_pagina)
        soup_pagina = BeautifulSoup(req_pagina.text, 'html.parser')
        
        irudiak_en_pagina = soup_pagina.find_all("img", {"class": "marcofotomini"})
        for irudi in irudiak_en_pagina:
            k = irudi.get("onclick", "")
            if k:
                p = k[k.find("(") + 1:k.find(")")]
                if p:
                    lista_de_imagenes.append(p)

    if not lista_de_imagenes:
        print("Ez da irudirik aurkitu bilduma honetan.")
        sys.exit(0)

    print(f"Guztira {len(lista_de_imagenes)} irudi aurkitu dira. Deskargari ekiten...")

    # --- FASE 2: DESCARGA CON PROGRESO POR IMAGEN ---
    
    widgets = [
        progressbar.Percentage(),
        ' ', progressbar.Bar(marker='█', left='|', right='|'),
        ' ', progressbar.ETA(),
        ' ', progressbar.FileTransferSpeed(),
    ]
    with progressbar.ProgressBar(widgets=widgets, max_value=len(lista_de_imagenes)) as bar:
        for idx, p in enumerate(lista_de_imagenes):
            try:
                # Construir la URL de descarga y la ruta del archivo
                url_descarga = f"http://www.festak.org/fotoeve/{kodea}/MAXHD/{p}.JPG"
                filepath = os.path.join(directory, f"{p}.jpg")

                if not os.path.exists(filepath):
                    urllib_request.urlretrieve(url_descarga, filepath)
                    time.sleep(0.05)

            except Exception as e:
                print(f"\nErrorea '{p}.jpg' deskargatzean: {e}", file=sys.stderr)
            finally:
                bar.update(idx + 1)

    print(f"\nDeskarga amaituta! Argazkiak '{directory}' karpetan gorde dira.")

except Exception as e:
    print(f"\nErrore bat gertatu da: {e}")