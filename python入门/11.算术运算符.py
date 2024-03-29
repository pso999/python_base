# 算术运算符
# + 加法运算符（如果是两个字符串之间进行加法运算，则会进行拼串操作）
# - 减法运算符
# * 乘法运算符（如果将字符串和数字相乘，则会对字符串进行复制操作，将字符串重复指定次数）
# / 除法运算符，运算时结果总会返回一个浮点类型
# // 整除，只会保留计算后的整数位，总会返回一个整型
# ** 幂运算，求一个值的几次幂
# % 取模，求两个数相除的余数

a = 10 + 5 # 计算
a = 'hello' + ' ' + 'world' # 拼串

a = 10 - 5 # 计算
a = 5 - True 
a = a - 2 # 用变量a的值减去2，然后再赋值给a
# a = 'hello' - 'h' TypeError

a = 5 * 5

a = 10 / 5
a = 5 / 2
# a = 5 / 0 ZeroDivisionError: division by zero
a = 10 / 3
a = 10 // 3
a = 5 // 2 

a = 2 ** 2
a = 10 ** 5
a = 16 ** 0.5 # 求16的平方根

a = 10 % 5 # 0
a = 10 % 4 # 2
a = 10 % 3 # 1
a = 10 % 2 # 0

print("a =",a)

## 运算符
# 运算符可以对一个值或多个值及逆行运算或各种操作
# 比如 +,-,=等都属于运算符
# 运算符的分类
#   - 算数运算符
#   - 赋值运算符
#   - 比较运算符（关系运算符）
#   - 