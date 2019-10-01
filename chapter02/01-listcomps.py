# 把一个字符串转换为Unicode码位的列表
symbols = "@#$%^&"
codes = []

for symbol in symbols:
    # ord返回一个单字符字符串的Unicode代码点。
    codes.append(ord(symbol))

print(codes)

# 使用列表推导式
codes_2 = [ord(symbol) for symbol in symbols]
print(codes_2)

# 使用filter和map组合
symbols_2 = "$￥%*%@！#"
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols_2)))
print(beyond_ascii)
