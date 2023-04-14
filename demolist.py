# 创建集合
thisset = set(("Google", "Runoob", "Taobao"))
print(thisset)
# 添加
thisset.add("apple")
print(thisset)
thisset.update({1,2,3})
print(thisset)
# 移除
thisset.remove("Taobao")
print(thisset)
thisset.discard("Runoob")
print(thisset)
# 计数
print(len(thisset))
# 判定集合中是否存在
a = "Runoob"
if a in thisset:
    print(a + "在集合中")
else:
    print(a + "不在集合中")