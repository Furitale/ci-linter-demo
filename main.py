# 这是一个有风格问题的 main.py 文件
def  hello_world  (  name ):  # 函数定义周围有多余空格
    # 一个非常长的行，肯定会超过flake8默认的79个字符的限制，让我们看看会发生什么，这行应该被标记出来。
    message = "Hello, " + name
    print(  message  )  # 函数调用内部有多余空格
    unused_variable = 42  # 定义了但未使用的变量
if __name__=="__main__":  # 运算符周围缺少空格
    hello_world("GitHub Actions")
