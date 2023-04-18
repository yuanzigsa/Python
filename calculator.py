def add(a, b):
    """加法操作"""
    return a + b


def subtract(a, b):
    """减法操作"""
    return a - b


def multiply(a, b):
    """乘法操作"""
    return a * b


def divide(a, b):
    """除法操作"""
    if b == 0:
        return "错误：除数不能为零！"
    else:
        return a / b


# 主程序
while True:
    print("请选择操作：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 退出")
    choice = input("请输入操作选项（1/2/3/4/5）：")

    if choice == '5':
        print("退出计算器。")
        break

    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))

    if choice == '1':
        print("结果：", add(num1, num2))
    elif choice == '2':
        print("结果：", subtract(num1, num2))
    elif choice == '3':
        print("结果：", multiply(num1, num2))
    elif choice == '4':
        print("结果：", divide(num1, num2))
    else:
        print("错误：无效的选项！请重新选择。")
