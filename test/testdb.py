from server.core.db import dbEngine

engine = dbEngine.createSqliteEngine(":memory:", "threadlocal")
engine.connect()
engine.begin()

text = """CREATE TABLE USERS (USERID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, LOGIN TEXT(45), PASSWORD TEXT(64) NOT NULL, REALM INTEGER(4))"""

# try:


engine.execute(text)
engine.commit()

text = """ INSERT INTO USERS values(NULL,"aa","ab",1)"""
engine.execute(text)
engine.commit()

text = """ INSERT INTO USERS values(NULL,"BBa","aFDSFb",2)"""

engine.execute(text)
engine.commit()

text = """ SELECT ROWID,* FROM USERS"""
cur = engine.execute(text)
print(cur.fetchall())

text = """CREATE UNIQUE INDEX LR_INDEX  ON USERS  (LOGIN, REALM)"""
engine.execute(text)
engine.commit()

text = """CREATE UNIQUE INDEX USERID_INDEX ON USERS (USERID)"""
engine.execute(text)
engine.commit()
text = """ select * from sqlite_master """
cur = engine.execute(text)
print(cur.fetchall())

text = """  """
cur = engine.execute(text)

# except:
#    engine.rollback()
