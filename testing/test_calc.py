import pytest
from pythoncode.calculator import Calculator


class TestCalc:

    def setup_class():
        print('【开始计算】')

    def teardown_class():
        print('【计算结束】')

    # 实例化被测类calc
    calc = Calculator()

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [10000, 10000, 20000]],
                             ids=['int', 'bignumber'])
    def test_add_int(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[0.1, 0.2, 0.3], [0.1, 0.1, 0.2]],
                             ids=['float1', 'float'])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [[-1, -1, -2], [-1, 1, 0]],
                             ids=['minus1', 'minus2'])
    def test_add_minus(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [[10, 5, 2], [1, 3, 1 / 3], [0.1, 0.2, 0.5]],
                             ids=['可整除', '无法整除', '小数'])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b', [[10, 0], [0.1, 0]], ids=['除数为0', '除数为0'])
    def test_div_zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)

    # def test_add1(self):
    #     test_data= [[1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2],[-1,-1,-3]]
    #     for i in range(0,len(test_data)):
    #     # 实例化被测类calc
    #     # calc = Calculator()
    #         result = self.calc.add(test_data[i][0], test_data[i][1])
    #         assert result == test_data[i][2]

    # def test_add2(self):
    #     # 实例化被测类calc
    #     # calc = Calculator()
    #     result = self.calc.add(0.1, 0.1)
    #     assert result == 0.2
