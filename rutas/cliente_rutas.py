from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED
from esquemas.clientes_esquema import clientes_esquema
from esquemas.parametros_empresa_esquema import Parametros_Empresa_Esquema
from configuracion.db import engine
from modelos.clientes_modelo import clientes_modelo
from modelos.paramentros_empresa import parametros_empresa
from time import time
from procedimientos.secuenciales import ObtenerSecuecial


cliente = APIRouter()


def ValidarExistenciaCliente(Conexion, identificacion, Clienteid):

    if len(identificacion) == 10:
        cedularuc = identificacion+"001"

    if len(identificacion) == 13:
        cedularuc = identificacion[10:len(identificacion)]

    if Clienteid == None:
        sql = "SELECT clientesid, identificacion, clientescodigo FROM clientes WHERE (identificacion='%s' or identificacion='%s')"
        resultado = Conexion.execute(sql % (identificacion, cedularuc)).first()

    if Clienteid != None:
        sql = "SELECT clientesid, identificacion, clientescodigo FROM clientes WHERE (identificacion='%s' or identificacion='%s') AND clientesid <> %s"
        resultado = Conexion.execute(
            sql % (identificacion, cedularuc, Clienteid)).first()

    return resultado


@cliente.post("/api/cliente", status_code=HTTP_201_CREATED)
def crear_cliente(datos_cliente: clientes_esquema):
    start_time = time()
    with Session(engine) as session:
        session.begin()
        try:
            nuevo_cliente = datos_cliente.dict()
            existenciaclientes = ValidarExistenciaCliente(
                session, nuevo_cliente['identificacion'], nuevo_cliente['clientesid'])

            # print(existenciaclientes)
            if existenciaclientes == None:
                # llama a la funcion para obtener el codigo del cliente
                secuencia = ObtenerSecuecial('CLIENTES', session)
                nuevo_cliente['clientescodigo'] = secuencia

                # obtener los datos de parametros de empresa
                parametro_empresa = session.execute(
                    parametros_empresa.select()).first()

                ###########################################################################
                # validacion de campos vacíos
                if secuencia in [None, '', 0]:
                    nuevo_cliente['clientescodigo'] = nuevo_cliente['identificacion']

                if nuevo_cliente['codigocontable'] in [None, '', 0]:
                    nuevo_cliente['codigocontable'] = parametro_empresa['codigocontable_clientes']

                if nuevo_cliente['provinciasid'] in [None, '', 0]:
                    nuevo_cliente['provinciasid'] = parametro_empresa['provinciasid']

                if nuevo_cliente['ciudadesid'] in [None, '', 0]:
                    nuevo_cliente['ciudadesid'] = parametro_empresa['ciudadesid']

                if nuevo_cliente['parroquiasid'] in [None, '', 0]:
                    nuevo_cliente['parroquiasid'] = parametro_empresa['parroquiasid']

                resultado = session.execute(
                    clientes_modelo.insert().values(nuevo_cliente))
                session.commit()

                fintiempo = time() - start_time
                print(fintiempo)

                return JSONResponse(status_code=HTTP_201_CREATED, content={"clientes": [{"clientesid_viejo": "", "clientesid_nuevo": "", "clientes_codigo": secuencia}]}, media_type="application/json")
            else:
                return JSONResponse(status_code=HTTP_201_CREATED, content={"clientes": [{"clientesid_viejo": nuevo_cliente['clientesid'], "clientesid_nuevo": existenciaclientes['clientesid'], "clientes_codigo": existenciaclientes['clientescodigo'], "observacion":"Ya exite el cliente"}]}, media_type="application/json")

        except Exception as e:
            session.rollback()
        finally:
            session.close()
