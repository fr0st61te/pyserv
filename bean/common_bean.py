# -*- coding: utf8 -*-
from core.db import dbEngine
from core.utils import Singleton
from core.log import Log
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import os

log = Log().get_logger()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, unique=True)
    login = Column(String(256), nullable=False)
    lastdate = Column(Integer)
    password = Column(String(256), nullable=False)


class CommonBean(metaclass=Singleton):

    def __init__(self):
        path = './db'
        if 'PYSERV_DB_PATH' in os.environ:
            path = os.environ['PYSERV_DB_PATH']
        log.debug("db path %s" % path)
        self._engine = dbEngine.createSqliteEngine(path, 'plain')
        self._connection = self._engine.connect()
        _ = sessionmaker(bind=self._engine, autocommit=True)
        self._session = _()
        User.metadata.create_all(self._engine)

    def get_connection(self):
        return self._connection

    def get_session(self):
        return self._session

    def execute(self, query):
        """ execute INSERT UPDATE DELETE """
        conn = self.get_connection()
        conn.execute(query)

    def fetch_row(self, query):
        """ get a row """
        conn = self.get_connection()
        result = conn.execute(query)
        row = result.fetchone()
        return row

    def fetch_rows(self, query):
        """ get rows """
        conn = self.get_connection()
        result = conn.execute(query)
        rows = result.fetchall()
        return rows
