#!/usr/bin/env python
# -*- coding:utf-8 -*-


from conf import settings
from core import db_handler


class Classes:
    """
    班级类
    """
    def __init__(self, name):
        self.class_data = db_handler.DbHandler().get_data(settings.CLASS_DB_PATH, name)

    def is_in_class(self, name, role_string):
        """
        检查 学生 老师 课程是否在班级
        :param name:
        :param role_string:
        :return:
        """
        if role_string == 'teacher':
            key = 'teacher_list'
        elif role_string == 'course':
            key = 'course_list'
        elif role_string == 'student':
            key = 'student_list'
        else:
            raise ValueError('is_in_class 参数不正确')

        if len(self.class_data[key]) > 0:
            for info in self.class_data[key]:
                if info == name:
                    return True
        return False

    def show_student(self):
        """
        显示班级学生
        :return:
        """
        if len(self.class_data['student_list']) > 0:
            print('班级当前有学生如下:')
            for i in self.class_data['student_list']:
                print(i)
            return True
        else:
            print('班级还没有学生')
            return False

    def get_all_course(self):
        return self.class_data['course_list']

    def add_student(self, student_name):
        self.class_data['student_list'].append(student_name)
        db_obj = db_handler.DbHandler.singleton()
        db_obj.save_data(self.class_data, settings.CLASS_DB_PATH)

    def is_teaching(self, teacher_name):
        """
        哪个老师正在上课
        :param teacher_name:
        :return:
        """
        print('%s老师正在上%s的课' % (teacher_name, self.class_data['name']))






