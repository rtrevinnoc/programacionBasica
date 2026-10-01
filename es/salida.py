import csv
from pathlib import Path

def producir_archivo(ruta, historial):
    path = Path(ruta)
    if path.exists():
        with open(path, mode="a", newline="") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["Operacion","A","B"])
            writer.writerows(historial)
    else:
        with open(path, mode="w", newline="") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=["Operacion","A","B"])
            writer.writeheader()
            writer.writerows(historial)