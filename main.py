from fastapi import FastAPI
from rutas.cliente_rutas import cliente

#instancia
app = FastAPI() 

app.include_router(cliente)