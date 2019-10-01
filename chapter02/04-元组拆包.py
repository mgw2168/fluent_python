import os

_, filename = os.path.split('/opt/data/data.txt')
print(filename)


data = divmod(20, 8)
print(data)


# *运算符可以将一个可迭代对象拆解为函数的参数
t = (20, 8)
get_tuple = divmod(*t)
print(get_tuple)

# *args 来获取不确定数量的参数
a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

# 在平行赋值中， *只能用在一个变量名的前面
a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)
