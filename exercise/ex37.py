#coding:utf-8
#http://www.cnblogs.com/xueweihan/p/4518022.html 我都是看这里的。。。。

#1.and：表示逻辑‘与’
#2.del：用于list列表操作，删除一个或者连续几个元素。
#3.from：导入相应的模块，用import或者from...impor
#4.not：表示逻辑‘非
#5.while：while循环，允许重复执行一块语句，一般无限循环的情况下用它。示例如下：
#while Ture:
   # if a > b:
      #  add()#调用函数求和
    #else:
        #print "输入错误！重新输入！"
#8.global:定义全局变量
#定义全局变量，变量名全部大写
NAME = "xueweihan"

#得到NAME值
def get_NAME():
    return NAME
    
#重新设定NAME值
def set_NAME(name_value):
    global NAME
    NAME = name_value
    
print u"输出全局变量NAME的值:",get_NAME()
new_name = "521xueweihan"
set_NAME(new_name)#为全局变量重新赋值
print u"输出赋值完的全局变量NMAE的值:",get_NAME()
#9.or　　  ：表示逻辑“或”
#10.with   ：和as一起用，使用的方法请看as，在上面！
#11.assert：表示断言（断言一个条件就是真的，如果断言出错则抛出异常）用于声明某个条件为真，如果该条件不是真的，则抛出异常：AssertionError
#14.pass  ：pass的意思就是什么都不做。用途及理解：当我们写一个软件的框架的时候，具体方法啊，类啊之类的都不写，等着后续工作在做。那么就在方法和类里面加上pass，那样编译起来就不会报错了！就像这样：

#理解yield
def test_yield(n):
    for i in range(n):
        yield i*2#每次的运算结果都返回
              
for j in test_yield(8):
    print j,":",
print u"结束理解yield"

#看这里，太厉害了，不是我写的。。。。
##########
#这的fab应该是斐波那契的意思。。。。
def fib(max):
    a,b = 0,1
    while a < max:
        yield a
        a, b = b, a+b
print u"斐波那契数列！"
for i in fib(50):
    print i,",",

#16.break：作用是终止循环，程序走到break的地方就是循环结束的时候。（有点强行终止的意思）
#注意：如果从for或while循环中终止（break）之后 ，else语句不执行。

##理解except
try:
    num = 5/0
except:
    print u"计算出错"
######
#我们为什么要写finally，是因为防止程序抛出异常最后不能关闭文件，但是需要关闭文件有一个前提就是文件已经打开了。
#在第一段错误代码中，如果异常发生在f=open(‘xxx’)的时候，比如文件不存在，立马就可以知道执行f.close()是没有意义的。改正后的解决方案就是第二段代码。

# 理解in
first_list = [1, 2]
second_list = [1, 2, 3]
element = 1
red = 'red'
red_clothes = "red clothes"
print red in red_clothes
print first_list in second_list   # false
print element in first_list      # true

# 理解is
e = 1
es = 1.0
ess = 1
print u"""is就是比对id的值，看是否指向同一对象，
这里需要注意的是：同一对象,不是值相等就是同一对象。"""
print id(e)
print id(es)
print id(ess)

# 理解lambda
g = lambda :"lambda test."
print g()
num1 = lambda x, y=1:x + y
print num1(1)      # 多个变量的时候，可以不给有默认值的变量传值
print num1(10,10)    # 值得注意的是，如果y没有默认值而且不给它传值的话报错！
####
#这一章我copy了很多别人的东西，可是还是有很多还不熟练，或者概念很模糊，需要好好练习。
