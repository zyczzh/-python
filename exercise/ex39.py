#coding:utf-8
ten_things="Apples Oranges Crows Telephone Light Sugar"

print"Wait there's not 10 things in that list,let's fix that."

stuff=ten_things.split(' ')
more_stuff=["Day","Night","Song","Frisbee","Corn","Banana","Gril","Boy"]

while len(stuff) !=10:#!=意思是不等于#len()函数，作用：反回字符串/列表/字典/元组长度，用法：len(str),str：参数
    next_one=more_stuff.pop()
    print"Adding:",next_one
    stuff.append(next_one)
    print"There's %d item now."%len(stuff)

print"There we go: ",stuff
print"Let's do some things with stuff."
print stuff[1]
print stuff[-1]# 列表倒数第一个元素
print stuff.pop()     # 列表最后一个元素移除
print ' '.join(stuff)  #意思为用...连接stuff
print '#'.join(stuff[3:5])# [3:5]是第三个和第四个元素（要头不要尾）
