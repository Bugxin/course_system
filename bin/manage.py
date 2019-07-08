#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_url)
sys.path.append(base_url)

from core import db_handler
from conf import settings
from core import School


class Admin:
    def create_school(self):
        school_name = input('要创建的学校名称:').strip()
        db_obj = db_handler.DbHandler.singleton()
        data = db_obj.get_data(settings.SCHOOL_DB_PATH, school_name)
        # print(data)
        if data:
            print('学校已存在')
            return
        school_info = settings.SCHOOL_INFO
        school_info['id'] = db_obj.get_max_id(settings.SCHOOL_DB_PATH) + 1
        school_info['name'] = school_name
        db_obj.save_data(school_info, settings.SCHOOL_DB_PATH)
        print('创建成功')

    def create_class(self):
        if not self.show_school():
            return
        school_name = input('选择在哪个学校开班:').strip()
        if not self.__school_exist(school_name):
            print('先建学校')
            return
        school_obj = School.School(school_name)
        school_obj.create_class()

    def create_teacher(self):
        if not self.show_school():
            return
        school_name = input('选择在哪个学校创建讲师:').strip()
        if not self.__school_exist(school_name):
            print('学校不存在，先建学校')
            return
        school_obj = School.School(school_name)
        teacher_name = input('讲师姓名:').strip()
        if school_obj.is_in_school(teacher_name, 'teacher'):
            print('讲师已存在')
            return
        if school_obj.create_teacher(teacher_name):
            self.__add_account(teacher_name)  # 创建老师的时候 默认注册一个讲师账户
            print('创建成功')

    def create_course(self):
        if not self.show_school():
            return
        school_name = input('选择在哪个学校开课:').strip()
        if not self.__school_exist(school_name):
            print('学校不存在，先建学校')
            return
        school_obj = School.School(school_name)
        school_obj.create_course()

    def __school_exist(self, school_name):
        db_obj = db_handler.DbHandler.singleton()
        data = db_obj.get_data(settings.SCHOOL_DB_PATH, school_name)
        if data is None:
            return False
        return True

    def show_school(self):
        db_obj = db_handler.DbHandler.singleton()
        data = db_obj.get_data_list(settings.SCHOOL_DB_PATH)
        if len(data) <= 0:
            print('还没有创建学校')
            return False
        print('当前已有学校:')
        for i in data:
            print(i['name'])
        return True

    def __add_account(self, name):
        db_obj = db_handler.DbHandler.singleton()
        account_info = settings.USER_INFO
        account_info['id'] = db_obj.get_max_id(settings.USER_DB_PATH) + 1
        account_info['name'] = name
        account_info['role'] = 2  # 默认添加讲师
        account_info['password'] = '123'  # 默认密码
        db_obj.save_data(account_info, settings.USER_DB_PATH)


obj = Admin()
menu = """
---------------管理员视图
1.创建学校 输入create_school
2.创建课程 输入create_course
3.创建讲师 输入create_teacher
4.创建班级 输入create_class
"""
while 1:
    print(menu)
    inp = input('输入选择:').strip()
    if hasattr(obj, inp):
        func = getattr(obj, inp)
        func()
    else:
        print('操作不存在')
