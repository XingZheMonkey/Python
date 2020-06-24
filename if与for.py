age=int(input("请输入你的年龄:"))

# if
if age<10 :
    print ("Too young too simple")
elif age>50 :
    print ("Too old too smart")
else :
    print("anyways....")


# for
arr=[1,2,3,"Henry",4,5,6]

for item in arr:
    print (item)

for item in arr[0:4] :
    print (item)

for item in arr:
    if item == 'Henry' :
        print (f"{item} is a good boy")
        break
    else :
        print(item)