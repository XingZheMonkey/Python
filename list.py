#coding=utf-8

arr=['apple','banana','car']

# 输出数组
print (arr)

print (arr[0:])

# 倒序查找
print(arr[-2])

# 追加数据
arr.append('pen')
print (arr)

# 从最后开始删减数据
arr.pop()
print (arr)  

# 删除指定数据
arr.remove('banana')
print (arr)

del(arr[0])
print (arr)