#------------------------------------------------------------------------------
#UEBUNG 2
#------------------------------------------------------------------------------

from pyproj import Transformer
import uvicorn
from fastapi import FastAPI
from fastapi import responses
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))

@app.get("/LV95toWGS84")
async def LV95toWGS84(E: float = 0.0, N: float = 0.0):
    transLV95toWGS84 = Transformer.from_crs("epsg:2056", "epsg:4326")
    result = transLV95toWGS84.transform(E, N)
    return {"LV95 Koordinaten": f"Latitude: {result[0]}, Longitude: {result[1]}"}

@app.get("/WGS84toLV95")
async def WGS84toLV95(lat: float = 0.0, lng: float = 0.0):
    transWGS84toLV95 = Transformer.from_crs("epsg:4326", "epsg:2056")
    result = transWGS84toLV95.transform(lat, lng)
    print(result)
    return {"LV95 Koordinaten": f"E: {result[0]}, N: {result[1]}"}

uvicorn.run(app, host="127.0.0.1", port=8000)

#Beispiel: 127.0.0.1:8000/WGS84toLV95?lat=46.95&lng=7.43

#------------------------------------------------------------------------------