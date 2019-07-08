#!/usr/bin/env python
# -*- coding:utf-8 -*-


from conf import settings
from core import db_handler
from core import Classes


class School:
    """
    学校类
    """
    def __init__(self, name):
        self.school_data = db_handler.DbHandler.singleton().get_data(settings.SCHOOL_DB_PATH, name)

    def create_class(self):
        """
        开班
        :return:
        """
        print('create class')
        # 创建班级
        db_obj = db_handler.DbHandler.singleton()
        data = settings.CLASS_INFO
        data['name'] = input('要创建的班级名:').strip()
        if self.is_in_school(data['name'], 'class'):
            print('班级已存在')
            return
        if len(self.school_data['teacher_list']) <= 0:
            print('先创建老师')
            return

        if len(self.school_data['course_list']) <= 0:
            print('先创建课程')
            return

        data['id'] = db_obj.get_max_id(settings.CLASS_DB_PATH) + 1  # 新建 id = 现有最大值+1
        data['school_name'] = self.school_data['name']
        teacher_list = self.arrange_teacher()
        data['teacher_list'] = teacher_list
        course_list = self.arrange_course()
        data['course_list'] = course_list

        # 创建班级
        db_obj.save_data(data, settings.CLASS_DB_PATH)

        # 讲师关联班级
        for i in teacher_list:
            teacher_info = db_obj.get_data(settings.TEACHER_DB_PATH, i)
            teacher_info['class_list'].append(data['name'])
            db_obj.save_data(teacher_info, settings.TEACHER_DB_PATH)

        # 学校关联班级
        self.school_data['class_list'].append(data['name'])
        db_obj.save_data(self.school_data, settings.SCHOOL_DB_PATH)
        print('创建成功')

    def create_course(self):
        """
        添加课程
        :return:
        """
        print('create course')
        db_obj = db_handler.DbHandler.singleton()
        course_info = settings.COURSE_INFO
        course_info['name'] = input('要创建的课程名:').strip()
        if self.is_in_school(course_info['name'], 'course'):
            print('课程已存在')
            return
        course_info['id'] = db_obj.get_max_id(settings.COURSE_DB_PATH) + 1
        course_info['school_name'] = self.school_data['name']
        course_info['period'] = input('上课周期:').strip()
        money = input('学费:').strip()
        if not money.isdigit() or int(money) < 0:
            print('学费输入不合法')
            return
        course_info['price'] = int(money)
        # 创建课程
        db_obj.save_data(course_info, settings.COURSE_DB_PATH)
        self.school_data['course_list'].append(course_info)
        # 学校关联课程
        db_obj.save_data(self.school_data, settings.SCHOOL_DB_PATH)
        print('创建成功')

    def create_teacher(self, name):
        """
        添加老师
        :return:
        """
        print('create teacher')
        db_obj = db_handler.DbHandler.singleton()
        teacher_info = settings.TEACHER_INFO
        # 每次创建 id +1
        teacher_info['id'] = db_obj.get_max_id(settings.TEACHER_DB_PATH) + 1
        teacher_info['name'] = name
        teacher_info['school_name'] = self.school_data['name']
        teacher_info['course_name'] = input('讲师教什么课:').strip()
        if not self.is_in_school(teacher_info['course_name'], 'course'):
            print('先创建课程')
            return False

        # 创建讲师
        db_obj.save_data(teacher_info, settings.TEACHER_DB_PATH)
        # 学校关联讲师
        self.school_data['teacher_list'].append(teacher_info['name'])
        db_obj.save_data(self.school_data, settings.SCHOOL_DB_PATH)
        return True

    def update_money(self, money):
        """
        收学费
        :return:
        """
        self.school_data['money'] += money
        db_obj = db_handler.DbHandler.singleton()
        db_obj.save_data(self.school_data, settings.SCHOOL_DB_PATH)

    def is_in_school(self, name, role_string):
        """
        讲师，课程，班级是否在学校
        :param name:
        :param role_string:
        :return:
        """
        if role_string == 'teacher':
            key = 'teacher_list'
        elif role_string == 'course':
            key = 'course_list'
        elif role_string == 'class':
            key = 'class_list'
        else:
            raise ValueError('is_in_class 参数不正确')

        if len(self.school_data[key]) > 0:
            for i in self.school_data[key]:
                if key == 'course_list':
                    if i['name'] == name:
                        return True
                else:
                    if i == name:
                        return True
        return False

    def arrange_teacher(self):
        teachers = input('输入要指派的老师姓名,以空格分隔:').strip()
        teacher_list = teachers.split()
        if len(teacher_list) <= 0:
            raise ValueError('指派老师不能为空')

        for i in teacher_list:
            if not self.is_in_school(i, 'teacher'):
                raise ValueError('不能指派不存在的讲师')

        return teacher_list

    def arrange_course(self):
        course = input('输入要指派到班级的课程姓名,以空格分隔:').strip()
        course_list = course.split()
        if len(course_list) <= 0:
            raise ValueError('课程不能为空')

        for i in course_list:
            if not self.is_in_school(i, 'course'):
                raise ValueError('不能指派不存在的课程')

        return course_list

    def show_school_info(self, info_type):
        if info_type == 'teacher':
            key = 'teacher_list'
        elif info_type == 'course':
            key = 'course_list'
        elif info_type == 'class':
            key = 'class_list'
        else:
            raise ValueError('参数不正确')

        if len(self.school_data[key]) > 0:
            print('%s列表已有成员如下:' % info_type)
            for i in self.school_data[key]:
                if key == 'course_list':
                    print(i['name'])
                else:
                    print(i)
        else:
            raise ValueError("还没创建")

    def show_schooling(self, class_name):
        schooling = 0
        if self.is_in_school(class_name, 'class'):
            class_obj = Classes.Classes(class_name)
            course_list = class_obj.get_all_course()
            if len(course_list) <= 0:
                raise ValueError('班级都没指定课程还想收钱')
            if len(self.school_data['course_list']) <= 0:
                raise ValueError('学校都没开课程还想收钱')
            for i in course_list:
                for j in self.school_data['course_list']:
                    if j['name'] == i:
                        schooling += j['price']
                        break
            return schooling
        else:
            raise ValueError('班都没开收什么钱')
