# 定义一个函数，用于计算两个数的乘积
def multiply(num1, num2):
    return num1 * num2

# 定义一个函数，用于计算一个列表中所有元素的和
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# 定义一个函数，用于判断一个数是否为质数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 定义一个函数，用于生成斐波那契数列
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

# 主程序
num1 = 5
num2 = 7
product = multiply(num1, num2)
print("The product of", num1, "and", num2, "is", product)

lst = [1, 2, 3, 4, 5]
total = sum_list(lst)
print("The sum of", lst, "is", total)

num = 7
if is_prime(num):
    print(num, "is prime")
else:
    print(num, "is not prime")

n = 10
fib = fibonacci(n)
print("The first", n, "numbers in the Fibonacci sequence are", fib)