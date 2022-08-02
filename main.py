from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import psutil

app = FastAPI(title="SysView", description="A web app for monetoring system state")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/info/")
def info():
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    return {
        "cputemperature": round(psutil.sensors_temperatures()["cpu_thermal"][0].current, 2),
        "memtotal": round(mem.total, 2),
        "memused": round(mem.used, 2),
        "memavailable": round(mem.available, 2),
        "mem_percent": round(mem.percent, 2),
        "disktotal": round(disk.total, 2),
        "diskused": round(disk.used, 2),
        "diskavailable": round(disk.free, 2),
        "diskpercent": round(disk.percent, 2),
        "cpupercent": psutil.cpu_percent(),
    }
