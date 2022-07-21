from importlib.metadata import metadata
from sqlalchemy import create_engine, MetaData
from sqlalchemy.pool import NullPool

engine = create_engine(
    "mariadb+mariadbconnector://root:Alfayomega1232*@localhost:5588/1032152398_db0000000003?charset=utf8mb4", poolclass=NullPool)


meta_data = MetaData()
