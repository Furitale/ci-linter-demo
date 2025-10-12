import pytest
from calculator import add,subtract

def test_add_positive_numbers():
    """测试正常情况：正数相加"""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """测试边界情况：负数相加"""
    assert add(-1, -1) == -2

def test_add_mixed_numbers():
    """测试边界情况：正负数混合"""
    assert add(5, -3) == 2

def test_add_zero():
    """测试边界情况：零值"""
    assert add(0, 5) == 5
    assert add(0, 0) == 0

def test_add_decimal_numbers():
    """测试边界情况：小数"""
    assert add(1.5, 2.5) == 4.0

def test_add_string_exception():
    """测试异常情况：字符串参数应抛出TypeError"""
    with pytest.raises(TypeError):
        add("2", 3)

def test_subtract_numbers():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2