
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class clientes_esquema(BaseModel):

    clientesid: Optional[str]
    clientescodigo: Optional[str]
    codigocontable: Optional[str]
    clientes_gruposid: int
    provinciasid: Optional[str]
    ciudadesid: Optional[str]
    razonsocial: str
    parroquiasid: Optional[str]
    clientes_zonasid: int
    nombrecomercial: str
    direccion: str
    identificacion: str
    tipoidentificacion: str
    email: str
    telefono1: str
    telefono2: str
    telefono3: str
    vendedoresid: int
    cobradoresid: int
    creditocupo: float
    creditodias: int
    estado: int
    tarifasid: int
    forma_pago_empresaid: int
    ordenvisita: int
    latitud: str
    longitud: str
    clientes_rutasid: int
    observacion: str
    usuariocreacion: str
    fechacreacion: datetime
