from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, DateTime, Date, BLOB
from configuracion.db import engine, meta_data

parametros_empresa = Table("parametros_empresa", meta_data,
                           Column("codigocontable_clientes",String(300), nullable = False),
                           Column("provinciasid",String(2)),
                           Column("ciudadesid",String(4)),
                           Column("parroquiasid",String(6)),
                           Column("sri_tipos_ivas_codigo",String(6)),
                           Column("sri_codigo_impuestos",String(6)),
                           Column("codigocontable_inventariosiniva",String(30)),
                           Column("codigocontable_ventasiniva",String(30)),
                           Column("codigocontable_costosiniva",String(30)),
                           Column("codigocontable_inventarioconiva",String(30)),
                           Column("codigocontable_ventaconiva",String(30)),
                           Column("codigocontable_costoconiva",String(30)),
                           Column("cobros_notificacion", Integer),
                           Column("DBDatos",String(30)),
                           Column("de_fechacertificado",Date),
                           Column("de_clavecertificado",String(100)),
                           Column("smtp_servidor",String(75)),
                           #Column("de_certificadodigital",BLOB),
                           Column("smtp_usuario",String(75)),
                           Column("smtp_clave",String(35)),
                           Column("smtp_puerto",String(10)),
                           Column("de_sql_factura",String(300)),
                           Column("de_sql_notacredito",String(300)),
                           Column("clientesid",Integer),
                           Column("de_correo_predeterminado",String(150)),
                           Column("nombrecomercial",String(300)),

                           )
