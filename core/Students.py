#!/usr/bin/env python
# -*- coding:utf-8 -*-

from core import db_handler
from conf import settings
from core import School
from core import Classes


class Students:
    """
    学生类：
    """

    def __init__(self, name):
        self.student_data = db_handler.DbHandler().get_data(settings.STUDENT_DB_PATH, name)

    def do_tuition(self):
        """
        交学费
        :return:
        """
        if self.student_data is None:
            print('先加入学校注册')
            return

        if self.student_data['class_name'] == '':
            print('先选班')
            return

        # 获取学费
        school_obj = School.School(self.student_data['school_name'])
        schooling = school_obj.show_schooling(self.student_data['class_name'])

        # 交学费
        school_obj.update_money(schooling)
        print('成功缴费')

    def choice_class(self):
        """
        选班
        :return:
        """
        if self.student_data is None:
            print('先加入学校注册')
            return

        # 展示学校的班级信息 方便选择
        school_obj = School.School(self.student_data['school_name'])
        school_obj.show_school_info('class')

        # 选班
        choice = input('输入要选择的班级名:').strip()
        if not school_obj.is_in_school(choice, 'class'):
            print('学校没有该班级')
            return
        class_obj = Classes.Classes(choice)
        if class_obj.is_in_class(self.student_data['name'], 'student'):
            print('已在该班级')
            return
        class_obj.add_student(self.student_data['name'])  # 学生加入班级

        # 关联班级
        self.student_data['class_name'] = choice
        # 关联班级的课程
        self.student_data['course_list'] = class_obj.get_all_course()

        # 更新学生信息
        self.update_student_info(self.student_data)
        print('选班成功')

    def update_student_info(self, data):
        self.student_data = data
        print('更新后学员信息:', self.student_data)
        db_obj = db_handler.DbHandler.singleton()
        db_obj.save_data(self.student_data, settings.STUDENT_DB_PATH)

    def get_student_info(self):
        return self.student_data






