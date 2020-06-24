#coding=utf-8

obj={'fruit':'grape','vegetable':'tomato','car':'horse'}

# 第二种创建字典的方式

person=dict(name="henry",age=28)


# 打印出来一个数组，数组里面是元组
print (obj.items())

# 打印所有键，数组格式
print (obj.keys())

# 打印所有值,数组格式
print (obj.values())

# 判断对象中是否存在某个值
print ('fruit' in obj )





# 练习
piano_level={}

while 1:
    name=input("请输入你的名字：")
    level=input("请输入你的等级: ")
    piano_level[name]=level

    another=input ("是否继续输入?(y/n):")

    if another == 'y' :
        continue
    else:
        break

def self_info (dictionary) :
    # 遍历字典
    for key,val in dictionary.items():
        print (f"{key} 的钢琴等级是 {val}")

self_info(piano_level)