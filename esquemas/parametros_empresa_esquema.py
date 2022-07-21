from datetime import date
from pydantic import BaseModel
from typing import Optional

from sqlalchemy import BLOB


class Parametros_Empresa_Esquema(BaseModel):
    codigocontable: str
    provinciasid: str
    ciudadesid: str
    parroquiasid: str
    sri_tipos_ivas_codigo: str
    sri_codigo_impuestos: str
    codigocontable_inventariosiniva: str
    codigocontable_ventasiniva: str
    codigocontable_costosiniva: str
    codigocontable_inventarioconiva: str
    codigocontable_ventaconiva: str
    codigocontable_costoconiva: str
    cobros_notificacion: int
    DBDatos: str
    de_fechacertificado: date
    de_clavecertificado: str    
    smtp_servidor: str
    #de_certificadodigital: BLOB
    smtp_usuario: str
    smtp_clave: str
    smtp_puerto: str
    de_sql_factura: str
    de_sql_notacredito: str
    clientesid: int
    de_correo_predeterminado: str
    nombrecomercial: str
