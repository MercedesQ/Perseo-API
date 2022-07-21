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

cliente = APIRouter()


class ConsultasGeneraldes:
    
    def obtenerSecuencial(self, tabla):
        with engine.connect() as conn:
            ########proceso para generar el codigo del cliente#################
            sql = "SELECT * from secuenciales where secuencial = '%s' "

            resulS = conn.execute(sql % (tabla)).first()

            numero = str(resulS[5])
            secuencia = str(
                resulS[4])+('0' * (resulS[3]-len(numero)))+str((resulS[5]))

            valor = resulS[5] + 1
            
            sql = "UPDATE secuenciales SET secuenciales.valor = %s where secuenciales.secuencial = %s"
            print(sql)
            parametros = (valor, tabla)
            conn.execute(sql, parametros)

            return secuencia

########pendiente de revisar
    def ValidarExistenciaCliente(self, identificacion, idCliente):
        with engine.connect() as conn:
            print(identificacion)
            if len(identificacion) == 10:
                ruc=identificacion+"001"

            if len(identificacion) == 13:
                cedula = identificacion[10:len(identificacion)]

            if idCliente == None:
                sql = "SELECT identificacion, razonsocial FROM clientes WHERE identificacion=%s"

            if idCliente != None:
                sql = "SELECT identificacion, razonsocial FROM clientes WHERE identificacion=%s AND clientesid <> %s"
            
            print(sql)
            parametros = (identificacion, idCliente)
            print(idCliente)
            resultado = conn.execute(sql, parametros).first()

            print(resultado)
            

Consultas = ConsultasGeneraldes()
 
@cliente.post("/api/cliente", status_code=HTTP_201_CREATED)
def crear_cliente(datos_cliente: ClientesEsquema):
    start_time = time()
    with Session(engine) as session:
        session.begin()
        try:
            nuevo_cliente = datos_cliente.dict()
            print(nuevo_cliente)
            Consultas.ValidarExistenciaCliente(nuevo_cliente['identificacion'], nuevo_cliente['clientesid'])
            #print(nuevo_cliente)
            # llama a la funcion para obtener el codigo del cliente
            secuencia = Consultas.obtenerSecuencial("CLIENTES")
            #secuencia = Consultas.actualizarSecuencial(15,"CLIENTES")
            print(secuencia)
            nuevo_cliente['clientescodigo'] = secuencia
            if secuencia in [None, '', 0]:
                nuevo_cliente['clientescodigo'] = nuevo_cliente['identificacion']

            # obtener los datos de parametros de empresa
            parametro_empresa = session.execute(parametros_empresa.select()).first()

            # validaciones de campos requeridos
            if nuevo_cliente['codigocontable'] in [None, '', 0]:
                nuevo_cliente['codigocontable'] = parametro_empresa['codigocontable_clientes']

            if nuevo_cliente['provinciasid'] in [None, '', 0]:
                nuevo_cliente['provinciasid'] = parametro_empresa['provinciasid']

            if nuevo_cliente['ciudadesid'] in [None, '', 0]:
                nuevo_cliente['ciudadesid'] = parametro_empresa['ciudadesid']

            if nuevo_cliente['parroquiasid'] in [None, '', 0]:
                nuevo_cliente['parroquiasid'] = parametro_empresa['parroquiasid']

            #session.execute(clientes.insert().values(nuevo_cliente))
            session.commit()

            fintiempo = time() - start_time
            print(fintiempo)

            return JSONResponse(status_code=HTTP_201_CREATED, content={"clientesid_viejo":1, "clientesid_nuevo":203, "clientes_codigo":"CL00000196"},media_type="application/json")

        except Exception as e:
            session.rollback()
        finally:
            session.close()
