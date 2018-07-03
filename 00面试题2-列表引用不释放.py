def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, ['a', 'b', 'c'])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)


g = []


def el(val):
    g.append(val)
    return g


g1 = el(10)
# g2 = el(123, ['a', 'b', 'c'])
g3 = el('a')


print("g1 = %s" % g1)
# print("g2 = %s" % g2)
print("g3 = %s" % g3)

