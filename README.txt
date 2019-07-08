-----------------选课系统
实现功能:
管理员入口 manage.py
    创建分校，班级，课程 讲师

讲师,学生入口 start.py
根据用户名 密码识别用户身份展示操作菜单   讲师(用户名:讲师名 密码:123，创建讲师时自动创建系统账户)  学员(与注册时账户名密码一致）
    讲师功能：
        选班上课，查看班级学生，修改学生成绩
    学生功能：
        加入学校(即注册)  选择班级  交学费


|----bin    可执行文件
|   |---- manage.py 管理员入口 创建各种数据
|   |---- start.py   程序起始
|-----conf
|   |---- settings.py  配置文件
|
|-----core     核心逻辑
|   |---views
|   |   |---student_view   学员视图
|   |   |---teach_view    讲师视图
|   |
|   |----classes.py    班级类 负责班级管理
|   |----db_handler.py  数据类 负责数据处理
|   |----main.py        程序入口
|   |----school.py      学校类 学校操作管理
|   |----students.py    学生类 负责学生操作
|   |----teachers.py    讲师类 讲师操作管理
|
|
|------db
    |--classes  班级数据目录，以文件名命名班级
    |--courses  课程数据目录，以文件名命名课程
    |--schools  学校数据目录  以文件名命名学校
    |--teachers  讲师数据目录 以文件名命名讲师
    |--users     系统用户数据 登录系统用 以文件名命名用户


类图: https://www.processon.com/view/link/5c34a19ae4b056ae29e6de6a
https://www.processon.com/view/link/5c34e0f7e4b056ae29e70fe3
