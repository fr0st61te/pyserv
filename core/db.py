# -*- coding: utf8 -*-
import sqlalchemy


class dbEngine(object):
    listEngines = {}  # idBean for work with only one Bean or default for all others

    @staticmethod
    def createMySqlEngine(host, port, dbname, user, psw, charset, unix_socket, \
                          strategy, pool_size, max_overflow, pool_recycle):
        engine = sqlalchemy.create_engine('mysql://%s:%s@%s:%s/%s' % (user, psw, host, \
                                                                      port, dbname), \
                                          connect_args={'use_unicode': True, 'charset': charset}, \
                                          pool_size=pool_size, max_overflow=max_overflow, \
                                          strategy=strategy, pool_recycle=pool_recycle)
        dbEngine.listEngines['default'] = engine
        return engine

    @staticmethod
    def createSqliteEngine(dbname, strategy):
        # staticpool
        engine = sqlalchemy.create_engine('sqlite:///%s' % (dbname), \
                                          strategy=strategy,
                                          # poolclass = sqlalchemy.pool.StaticPool,
                                          poolclass=sqlalchemy.pool.SingletonThreadPool
                                          # check_same_thread = False
                                          )
        dbEngine.listEngines['default'] = engine
        return engine

    @staticmethod
    def getEngine(host, port, dbname, user, psw, charset, unix_socket, \
                  strategy, pool_size, max_overflow, pool_recycle):
        # queuepool
        if not dbEngine.listEngines.has_key('default'):
            return dbEngine.createMySqlEngine(host, port, dbname, user, psw, charset, \
                                              unix_socket, strategy, pool_size, \
                                              max_overflow, pool_recycle)
        return dbEngine.listEngines['default']
