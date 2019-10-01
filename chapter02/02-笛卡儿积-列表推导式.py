# 使用列表推导式生成笛卡儿积
# 假设三种不同尺寸的T恤，每个尺寸有两种颜色

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

