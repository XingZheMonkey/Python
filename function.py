def greet(name,time="morning"):
    print (f"good {time} {name}")

name=input("请输入姓名：")

time=input("请输入时间: ")

greet(name)



# global可以将局部变量提升为全局变量

def print_name():
    global name
    name = "Henry"
    print (f"函数内的name为 : {name}")

print_name()

print (name)