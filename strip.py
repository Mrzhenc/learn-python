
dict = {'zhen': 7, 'hao': 6}
print "dict[zhen]", dict['zhen']
print "dict[chao]", dict['hao']

#del dict['zhen']
print "dict[zhen]", dict['hao']
#dict.clear()
print "dict[zhen]", dict['zhen']


tup = (1, 2, 3)
print tup[0]
#tup[0] = 4 can not be changed

lis = [1, 2, 3, 4]
lis[0] = 3
del lis[0]
print max(lis)

