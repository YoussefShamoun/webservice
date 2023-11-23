#------------------------------------------------------------------------------
#UEBUNG 1
#------------------------------------------------------------------------------

import uvicorn
from fastapi import FastAPI

app = FastAPI()
d = {}

# Öffne die Datei und lade die Daten in das Dictionary
with open("PLZO_CSV_LV95.csv", encoding="utf-8") as file:
    next(file)  # Überspringe die Header-Zeile
    for line in file:
        data = line.strip().split(";")
        ortschaft = data [0]
        plz = data[1]
        zusatzziffer = data[2]
        gemeinde = data[3]
        bfs_nr = data[4]
        kanton = data[5]
        e = data[6]
        n = data[7]
        sprache = data[8]

        d[gemeinde] = {
            "plz": plz,
            "ortschaft": ortschaft,
            "kanton": kanton,
            "bfs_nr": bfs_nr,
            "zusatzziffer": zusatzziffer,
            "e": e,
            "n": n,
            "sprache": sprache
        }


@app.get("/search")
async def search(gemeinde: str):
    if gemeinde in d:
        return d[gemeinde]
    else:
        return {"error": "Gemeinde not found"}

# Starte den FastAPI-Webdienst
uvicorn.run(app, host="127.0.0.1", port=8000)


#------------------------------------------------------------------------------



