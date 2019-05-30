# -*- coding: utf8 -*-
from bean.common_bean import CommonBean
from bean.common_bean import User


class UserBean(object):

    @staticmethod
    def get_user(login):
        session = CommonBean().get_session()
        res = session.query(User.uid).filter(User.login == login).one_or_none()
        if res:
            return res.uid
        return

    @staticmethod
    def create_user(login, password):
        if not UserBean.get_user(login):
            session = CommonBean().get_session()
            user = User(login=login, password=password)
            session.add(user)
