# -*- coding: utf8 -*-
from core.db import dbEngine
from core.utils import Singleton


class CommonBean(metaclass=Singleton):

    def __init__(self):
        self.engine = dbEngine.createSqliteEngine("../db", "plain")
        self.connection = self.engine.connect()

    def get_connection(self):
        return self.connection

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
