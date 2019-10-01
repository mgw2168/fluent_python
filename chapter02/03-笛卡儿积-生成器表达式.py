# 将列表推导式的方括号换成圆括号
symbols = "#$^$#^"
get_tuple = tuple(ord(symbol) for symbol in symbols)
print(get_tuple)

import array
# I: unsigned integer
get_array = array.array('I', (ord(symbol) for symbol in symbols))
print(get_array)

# 使用生成器表达式计算笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirts in ('%s %s' % (color, size) for color in colors for size in sizes):
    print(tshirts)

divmod()