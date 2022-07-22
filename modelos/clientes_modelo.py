
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, DateTime
from configuracion.db import engine, meta_data

clientes_modelo = Table("clientes", meta_data, Column("clientesid", Integer, primary_key=True),
                        Column("clientescodigo", String(10), nullable=False),
                        Column("codigocontable", String(30), ForeignKey(
                            "cuentas_contables.codigocontable"), nullable=False),
                        Column("clientes_gruposid", Integer, ForeignKey(
                            "clientes_grupos.clientes_gruposid"), nullable=False),
                        Column("provinciasid", String(2), ForeignKey(
                            "provincias.provinciasid"), nullable=False),
                        Column("ciudadesid", String(4), ForeignKey(
                            "ciudades.ciudadesid"), nullable=False),
                        Column("razonsocial", String(300), nullable=False),
                        Column("parroquiasid", String(6), ForeignKey(
                            "parroquias.parroquiasid"), nullable=False),
                        Column("clientes_zonasid", Integer, ForeignKey(
                            "clientes_zonas.clientes_zonasid"), nullable=False),
                        Column("nombrecomercial", String(300), nullable=False),
                        Column("direccion", String(300), nullable=False),
                        Column("identificacion", String(20), nullable=False),
                        Column("tipoidentificacion",
                               String(1), nullable=False),
                        Column("email", String(300), nullable=False),
                        Column("telefono1", String(15), nullable=False),
                        Column("telefono2", String(15), nullable=False),
                        Column("telefono3", String(15), nullable=False),
                        Column("vendedoresid", Integer, ForeignKey(
                            "facturadores.facturadoresid"), nullable=False),
                        Column("cobradoresid", Integer, ForeignKey(
                            "facturadores.facturadoresid"), nullable=False),
                        Column("creditocupo", Float, nullable=False),
                        Column("creditodias", Integer, nullable=False),
                        Column("estado", Integer, nullable=False),
                        Column("tarifasid", Integer, nullable=False),
                        Column("forma_pago_empresaid",
                               Integer, nullable=False),
                        Column("ordenvisita", Integer, nullable=False),
                        Column("latitud", String(30), nullable=True),
                        Column("longitud", String(30), nullable=True),
                        Column("clientes_rutasid", Integer, ForeignKey(
                            "rutas.rutasid"), nullable=False),
                        Column("observacion", String(300), nullable=True),
                        Column("usuariocreacion", String(25), nullable=False),
                        Column("fechacreacion", DateTime, nullable=False)
                        )
