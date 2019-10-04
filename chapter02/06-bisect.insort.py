import bisect
import random

SIZE = 7
random.seed(1729)

my_list = []

# insort(seq, item)将变量item插入序列seq中，并能保证seq的升序

for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

