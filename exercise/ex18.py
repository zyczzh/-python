#this one is like your scripts with argv
# encoding: utf-8
def print_two(*args):#参数必须放在圆括号 () 中才能正常工作。
    arg1,arg2=args#4 个空格缩进
    print"arg1:%r,arg2:%r"%(arg1,arg2)

#ok, that *args is actually pointless ,we can just do this
def print_two_again(arg1,arg2):
    print"arg1:%r,arg2:%r"%(arg1,arg2)

#this just takes one argument
def print_one(arg1):
    print"arg1:%r"%arg1


#this one takes no arguments
def print_none():
    print"I got nothin'."
    


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
