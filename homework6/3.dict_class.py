# -*- encoding: utf-8 -*-
'''
@File    :   3.dict_class.py
@Time    :   2020/04/14 16:32:47
@Author  :   Gloria 
@Version :   1.0
@Contact :   angelhome21@qq.com
'''

# here put the import lib

#三、定义一个字典类：dictclass。完成下面的功能：
#dict = dictclass({你需要操作的字典对象})
#1 删除某个key
#del_dict(key)
#2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
#get_dict(key)
#3 返回键组成的列表：返回类型;(list)
#get_key()
#4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
#update_dict({要合并的字典})

class Dictclass():
    def __init__(self, d):
        self.dict = d

    def del_dict(self, key):
        if key in self.dict.keys():
            del self.dict[key]
            return self.dict
        else:
            return self.dict
    
    def get_dict(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return 'not found'
    
    def get_key(self):
        return list(self.dict.keys())
    
    def update_dict(self, d):
        self.dict.update(d)
        return self.dict

dict1 = Dictclass({
    '0': 0,
    '1': 1,
    '2': 2
})
print(dict1.del_dict('0'))
print(dict1.get_dict('1'))
print(dict1.get_key())
print(dict1.update_dict({'3': 3}))