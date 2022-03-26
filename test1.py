"""
 * Project name(项目名称)：Python函数注解
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 15:20
 * Version(版本): 1.0
 * Description(描述)： 函数注解没有任何语法上的意义，只是为函数参数和返回值做注解，
 并在运行获取这些注解，仅此而已。换句话说，为函数做的注解，Python不做检查，不做强制，不做验证，
 什么操作都不做，函数注解对Python解释器没任何意义。
 """


def f(ham: str, egg: str = 'eggs') -> str:
    pass


def square(number: "一个数字") -> "返回number的平方":
    """
    square
    :param number: 一个数字
    :return: 返回number的平方
    """
    return number ** 2


if __name__ == '__main__':
    print(f.__annotations__)
    f("123", "2")
    # 给函数中的参数做注解的方法是在形参后添加冒号“：”，
    # 后接需添加的注解（可以是类（如 str、int 等），也可以是字符串或者表示式）；
    # 给返回值做注解的方法是将注解添加到 def 语句结尾的冒号和 -> 之间。

    print(square(3))
    print(square.__annotations__)
