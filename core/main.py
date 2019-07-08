#!/usr/bin/env python
# -*- coding:utf-8 -*-

from core.views import teach_view
from core.views import student_view
from core import db_handler
from conf import settings


def run():
    while 1:

        # 用户身份验证
        user_name = input('用户名:').strip()
        pwd = input('密码:').strip()
        inp = input('登录1，注册系统账户2:').strip()  # 选择注册 还是登录

        db_obj = db_handler.DbHandler.singleton()
        data = db_obj.get_data(settings.USER_DB_PATH, user_name)
        # print(data)
        if inp.isdigit():
            if inp == '1':  # 登陆
                if data is None:
                    print('账户不存在,先注册')
                    break
                if pwd != data['password']:
                    print('账户名密码不正确')
                    break

                if data['role'] == 1:  # 学生
                    obj = student_view.StudentView(user_name)
                elif data['role'] == 2:  # 讲师
                    obj = teach_view.TeachView(user_name)

            elif inp == '2':  # 注册
                data = settings.USER_INFO
                data['id'] = db_obj.get_max_id(settings.USER_DB_PATH) + 1
                data['name'] = user_name
                data['password'] = pwd
                data['role'] = 1
                db_obj.save_data(data, settings.USER_DB_PATH)
                obj = student_view.StudentView(user_name)  # 只有学生才能注册
            else:
                print('选项不存在')
                break
        else:
            print('输入不合法')
            break

        # 打印功能菜单
        while 1:
            obj.show_op_menu()

            # 根据用户输入反射操作
            inp = input('>>:').strip()
            if hasattr(obj, inp):
                func = getattr(obj, inp)
                func()
            else:
                print('操作不存在')
                return








