#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 学校配置信息
SCHOOL_DB_PATH = "%s/db/schools/" % BASE_PATH
SCHOOL_INFO = {
    'id': 0,            # 学校id
    'name': '',       # 学校名
    'class_list': [],   # 班级列表
    'teacher_list': [],  # 老师列表
    'course_list': [],    # 课程列表
    'money': 0          # 学费收入
}

# 系统使用者配置信息
USER_DB_PATH = '%s/db/users/' % BASE_PATH
USER_INFO = {
    'id': 0,
    'name': '',  # 用户名
    'password': '123',  # 初始密码
    'role': 0  # eg: 1 学生 2 讲师
}

# 讲师数据结构
TEACHER_DB_PATH = '%s/db/teachers/' % BASE_PATH
TEACHER_INFO = {
    'id': 0,         # 讲师id
    'name': '',       # 讲师姓名
    'school_name': '',  # 学校
    'course_name': '',  # 讲师教什么课
    'class_list': []   # 班级列表
 }

# 班级数据结构
CLASS_DB_PATH = '%s/db/classes/' % BASE_PATH
CLASS_INFO = {
    'id': 0,          # 班级id
    'name': '',     # 班级名
    'school_name': '',  # 学校名
    'teacher_list': [],  # 老师列表
    'course_list': [],    # 课程列表
    'student_list': []    # 学生列表
}


# 课程数据结构
COURSE_DB_PATH = '%s/db/courses/' % BASE_PATH
COURSE_INFO = {
    'id': 0,       # 课程id
    'name': '',  # 课程名
    'period': '',  # 周期
    'price': 0,     # 价格
    'school_name': ''  # 学校名
}

# 学生配置
STUDENT_DB_PATH = '%s/db/students/' % BASE_PATH
STUDENT_INFO = {
    'id': 0,       # 学号
    'name': '',    # 姓名
    'school_name': '',  # 学校
    'class_name': '',  # 班级
    'course_list': [],  # 课程列表
    'score_list': []  # 成绩列表
}

# 成绩
SCORE_INFO = {
    'course_name': '',  # 课程名
    'score': 0  # 成绩
}

