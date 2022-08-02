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
    disk = psutil.disk_usage()
    return {
        "temperature": psutil.sensors_temperatures()["cpu_thermal"][0]. current,
        "memtotal": mem.total,
        "memused": mem.used,
        "memavailable": mem.available,
        "mem_percent": mem.percent,
        "disktotal": disk.total,
        "diskusage": disk.usage,
        "diskavailable": disk.available,
        "diskpercent": disk.percent,
        "processor_usage": psutil.cpu_percent()
    }
    }
