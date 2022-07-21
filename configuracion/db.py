from importlib.metadata import metadata
from sqlalchemy import create_engine, MetaData
from sqlalchemy.pool import NullPool

engine = create_engine("mariadb+mariadbconnector://perseo:Invencible4050*@localhost:5588/8610710168_db0000000004?charset=utf8mb4",poolclass=NullPool)

meta_data = MetaData()
