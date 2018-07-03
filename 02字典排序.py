# 列表元素是字典排序：

infors = [{"name": "laowang", "age": 10}, {"name": "xiaoming", "age": 20}, {"name": "banzhang", "age": 10}, {"name": "zhangsan", "age": 18}]

infors.sort(key=lambda x: x['name'])
print(infors)

infors.reverse()

print(infors)

L = [23, 1761, 671, 7, 8, 16, 246, 17]
L.sort()
L.sort(reverse=True)
L.reverse()
