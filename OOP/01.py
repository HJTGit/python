'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    pass

# 定义一个对象
hjt = Student()

# 再定义一个类，描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 注意缩进层级
    # 默认有一个self参数
    def doHomeWork(self):
        print("做作业")
        # 推荐在函数末尾使用return语句
        return None

# 实例化
hjt = PythonStudent()
print(hjt.name)
print(hjt.age)
# 注意成员函数的调用没有传入参数
hjt.doHomeWork()