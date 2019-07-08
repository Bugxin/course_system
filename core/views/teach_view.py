#!/usr/bin/env python
# -*- coding:utf-8 -*-


from core import Teachers
from core import Classes


class TeachView:
    def __init__(self, name):
        self.name = name

    def show_op_menu(self):
        menu = """
------------操作菜单
1.选班上课 输入choice_class
2.查看班级学生 输入show_students
3.修改成绩 输入modify_score
"""
        print(menu)

    def choice_class(self):
        obj = Teachers.Teachers(self.name)
        obj.choice_class()

    def show_students(self):
        obj = Teachers.Teachers(self.name)
        # 展示班级列表
        if not obj.show_class_list():
            return
        choice = input('要看哪个班的学生:').strip()
        if not obj.has_class(choice):
            print('没有该班级')
            return
        obj.show_students(choice)

    def modify_score(self):
        obj = Teachers.Teachers(self.name)
        # 展示讲师教的班级列表
        if not obj.show_class_list():
            return
        class_name = input('修改哪个班级的成绩:').strip()
        if not obj.has_class(class_name):
            print('没有该班级')
            return
        # 展示班级学生
        class_obj = Classes.Classes(class_name)
        if not class_obj.show_student():
            # 班级没有学生
            return
        student_name = input('选择学生:').strip()
        if not class_obj.is_in_class(student_name, 'student'):
            print('班级没有该学生')
            return
        obj.modify_score(class_name, student_name)

