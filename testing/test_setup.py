# 模块级别

def setup_module():
    print('资源准备setup module')


def teardown_module():
    print('资源准备teardown module')


def test_case1():
    print("case1")


# 函数级别
def setup_function():
    print('资源准备setup function')


def teardown_function():
    print('资源销毁teardown function')


class TestDemo:
    # 类前后执行
    def setup_class(self):
        print('TestDemo setup_class')

    def teardown_class(self):
        print('TestDemo teardown_class')

    # 用例前后执行
    def setup(self):
        print('TestDemo setup_method')

    def teardown(self):
        print('TestDemo teardown_method')

    def test_demo1(self):
        print('test demo1')

    def test_demo2(self):
        print('test demo2')

