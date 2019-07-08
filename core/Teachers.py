#!/usr/bin/env python
# -*- coding:utf-8 -*-

from core import db_handler
from conf import settings
from core import Students
from core import Classes


class Teachers:
    """
    讲师类：管理讲师相关操作
    """
    def __init__(self, name):
        self.teacher_data = db_handler.DbHandler.singleton().get_data(settings.TEACHER_DB_PATH, name)

    def choice_class(self):
        # 展示所有老师讲课的班级
        if not self.show_class_list():
            return

        # 创建班级对象 调用上课方法
        choice = input('输入上课班级名:').strip()
        if not self.has_class(choice):
            print('没有该班级')
            return
        class_obj = Classes.Classes(choice)
        class_obj.is_teaching(self.teacher_data['name'])

    def show_students(self, class_name):
        """
        显示班级学生列表
        :param class_name:
        :return:
        """
        class_obj = Classes.Classes(class_name)
        class_obj.show_student()

    def modify_score(self, class_name, student_name):
        """
        修改成绩
        :return:
        """
        if not self.has_class(class_name):
            print('没有该班级')
            return
        class_obj = Classes.Classes(class_name)
        if not class_obj.is_in_class(student_name, 'student'):
            print('班级没有该学生')
            return

        # 设置成绩
        score_info = dict()  # 成绩信息
        score_info['course_name'] = self.teacher_data['course_name']
        score = input('成绩:').strip()
        if not score.isdigit() or int(score) < 0:
            print('成绩输入无效')
            return
        score_info['score'] = int(score)

        # 更新学生成绩
        student_obj = Students.Students(student_name)
        student_info = student_obj.get_student_info()
        student_info['score_list'].append(score_info)
        student_obj.update_student_info(student_info)

    def has_class(self, class_name):
        """
        讲师是否有这个班
        :param class_name:
        :return:
        """
        if len(self.teacher_data['class_list']) > 0:
            for name in self.teacher_data['class_list']:
                if name == class_name:
                    return True
        return False

    def show_class_list(self):
        """
        展示所教的班级列表
        :return:
        """
        # 遍历班级列表
        if len(self.teacher_data['class_list']) > 0:
            print('讲师教的班级有:')
            for name in self.teacher_data['class_list']:
                print(name)
            return True
        else:
            print('讲师还没有教课')
            return False


