# -*- coding: utf8 -*-
from server.bean.common_bean import CommonBean


class UserBean(object):
    _SELECT_USER_BY_LOGIN = """ SELECT UID FROM USERS WHERE LOGIN="%s" LIMIT 1 """
    _INSERT_USER = """ INSERT INTO USERS (LOGIN) VALUES("%s") """

    @staticmethod
    def get_user_bean(login):
        row = CommonBean().fetch_row(UserBean._SELECT_USER_BY_LOGIN % (str(login)))
        if row:
            return row[0]
        else:
            return

    @staticmethod
    def set_user_bean(login):
        if not UserBean.get_user_bean(login):
            CommonBean().fetch_row(UserBean._INSERT_USER % (str(login)))
