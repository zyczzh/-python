# encoding: utf-8
from sys import argv#cmd中输入文件路径位置

script,input_file=argv#script=py程序位置，input文件位置

def print_all(f):#定义一个函数print_all,接受一个参数f
    print f.read()#读取file

def rewind(f):#定义一个函数rewind,接受一个参数f
    f.seek(0)#f.seek(0)将f的文件指针恢复到文件开头

def print_a_line(line_count,f):
    print line_count,f.readline()

current_file=open(input_file)

print"First let's print the whole file:\n"

print_all(current_file)

print"Now let's rewind, kind of like a tape."

rewind(current_file)

print"Let's print three lines:"

current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)


