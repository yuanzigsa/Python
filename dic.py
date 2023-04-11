# 访问字典里的值
emptyDict = dict()
print(emptyDict)
print("Length:", len(emptyDict))
print(type(emptyDict))

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

# 修改字典
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息
print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

# 删除字典里的元素
tinydict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del tinydict3['Name']  # 删除键 'Name'
tinydict3.clear()  # 清空字典
del tinydict3  # 删除字典
