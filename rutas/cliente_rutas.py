from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
from esquemas.clientes_esquema import ClientesEsquema
from esquemas.parametros_empresa_esquema import Parametros_Empresa_Esquema
from configuracion.db import engine
from modelos.clientes_modelo import clientes
from modelos.paramentros_empresa import parametros_empresa
from time import time
from procedimientos.secuenciales import ObtenerSecuecial


cliente = APIRouter()


# pendiente de revisar
def ValidarExistenciaCliente(self, Conexion, identificacion, idCliente):

    if len(identificacion) == 10:
        ruc = identificacion+"001"

    if len(identificacion) == 13:
        cedula = identificacion[10:len(identificacion)]

    if idCliente == None:
        sql = "SELECT identificacion, razonsocial FROM clientes WHERE identificacion=%s"

    if idCliente != None:
        sql = "SELECT identificacion, razonsocial FROM clientes WHERE identificacion=%s AND clientesid <> %s"

    parametros = (identificacion, idCliente)

    resultado = Conexion.execute(sql, parametros).first()


@cliente.post("/api/cliente", status_code=HTTP_201_CREATED)
def crear_cliente(datos_cliente: ClientesEsquema):
    start_time = time()
    with Session(engine) as session:
        session.begin()
        try:
            nuevo_cliente = datos_cliente.dict()
            print(nuevo_cliente)
            # Consultas.ValidarExistenciaCliente(
            # nuevo_cliente['identificacion'], nuevo_cliente['clientesid'])
            # print(nuevo_cliente)
            # llama a la funcion para obtener el codigo del cliente
            secuencia = ObtenerSecuecial("CLIENTES", session)
            # secuencia = Consultas.actualizarSecuencial(15,"CLIENTES")
            print(secuencia)
            nuevo_cliente['clientescodigo'] = secuencia
            if secuencia in [None, '', 0]:
                nuevo_cliente['clientescodigo'] = nuevo_cliente['identificacion']

            # obtener los datos de parametros de empresa
            parametro_empresa = session.execute(
                parametros_empresa.select()).first()

            # validaciones de campos requeridos
            if nuevo_cliente['codigocontable'] in [None, '', 0]:
                nuevo_cliente['codigocontable'] = parametro_empresa['codigocontable_clientes']

            if nuevo_cliente['provinciasid'] in [None, '', 0]:
                nuevo_cliente['provinciasid'] = parametro_empresa['provinciasid']

            if nuevo_cliente['ciudadesid'] in [None, '', 0]:
                nuevo_cliente['ciudadesid'] = parametro_empresa['ciudadesid']

            if nuevo_cliente['parroquiasid'] in [None, '', 0]:
                nuevo_cliente['parroquiasid'] = parametro_empresa['parroquiasid']

            # session.execute(clientes.insert().values(nuevo_cliente))
            session.commit()

            fintiempo = time() - start_time
            print(fintiempo)

            return JSONResponse(status_code=HTTP_201_CREATED, content={"clientesid_viejo": 1, "clientesid_nuevo": 203, "clientes_codigo": "CL00000196"}, media_type="application/json")

        except Exception as e:
            session.rollback()
        finally:
            session.close()
