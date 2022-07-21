from configuracion.db import engine


######################################################
# OPTENER SECUENCIALES INTERNOS
def ObtenerSecuecial(sTabla, Conexion):
    sql = "SELECT * from secuenciales where secuencial = '%s' "

    resulS = Conexion.execute(sql % (sTabla)).first()

    numero = str(resulS['valor'])
    secuencia = str(
        resulS['prefijo'])+('0' * (resulS['numeroceros']-len(numero)))+str((resulS['valor']))

    valor = resulS['valor'] + 1

    sql = "UPDATE secuenciales SET secuenciales.valor = %s where secuenciales.secuencial = %s"
    parametros = (valor, sTabla)
    Conexion.execute(sql, parametros)

    return secuencia
