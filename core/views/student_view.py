#!/usr/bin/env python
# -*- coding:utf-8 -*-


from core import Students
from conf import settings
from core import db_handler

class StudentView:
    def __init__(self, name):
        self.name = name

    def show_op_menu(self):
        menu = """
------------操作菜单
1.选班 输入choice_class
2.交学费 输入do_tuition
3.加入学校 输入join_school
"""
        print(menu)

    def do_tuition(self):
        """
        交学费
        :return:
        """
        student_obj = Students.Students(self.name)
        student_obj.do_tuition()

    def choice_class(self):
        """
        选班
        :return:
        """
        student_obj = Students.Students(self.name)
        student_obj.choice_class()

    def join_school(self):
        """
        加入学校 即创建学员
        :return:
        """
        student_info = settings.STUDENT_INFO
        db_obj = db_handler.DbHandler.singleton()
        student_info['id'] = db_obj.get_max_id(settings.STUDENT_DB_PATH) + 1
        student_info['name'] = self.name
        student_info['school_name'] = input('注册学校名称:').strip()
        data = db_obj.get_data(settings.SCHOOL_DB_PATH, student_info['school_name'])
        if data is None:
            print('学校不存在')
            return
        db_obj.save_data(student_info, settings.STUDENT_DB_PATH)
