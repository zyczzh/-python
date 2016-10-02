#coding:utf-8
print"Let's practive everything."
print'You\'d need to know \'bout escapes wiht\\ that do \n newlines and \t tabs.'
# \' 作用是print出‘
#\\ 作用是print出\
#\n 作用是换行
#\t 作用是空两格
poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print"-----------------------"
print poem
print"-----------------------"



five=10-2+3+-6
print"This should be five:%s"%five

def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates

start_point=10000
beans,jars,crates=secret_formula(start_ppoint)


