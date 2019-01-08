# -*- encoding: utf-8 -*-

print('将我这样框进来')#单引号

print("双引号用法")

print('''aaaa
adasd
asdad
asdasd
''')#三引号用法

#格式化语法
age = 20
name = '洋霸天'

print('我叫{0}，我今年{1}岁了'.format(name,age))
#{}中间的数字不是必填项
age = 21
name ='batting'
print('我叫{}，我今年{}岁了'.format(name,age))

name =  'zoe'
print('为什么{}是个女生？'.format(name))

# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 19
print('{0:_^19}'.format('hello'))

#为防止打印过程中出现这一换行符，你可以通过 end 指定其应以空白结尾
print('a',end='')
print('b')

#转义序列
#如果要生成遗传包含单引号（'）的字符串，使用转义序列来实现
print('\'what your name\'')

#如果你想指定一串双行字符串该怎么办？一种方式即使用如前所述的三引号字符串，或者你可以使用一个表示新一行的转义序列——\n 来表示新一行的开始。下面是一个例子：
print('这是第一行\n这是第二行')
#如果你需要指定一些未经过特殊处理的字符串，比如转义序列，那么你需要在字符串前增加 r 或 R 来指定一个 原始（Raw） 字符串4。下面是一个例子：
print(r"Newlines are indicated by \n")

