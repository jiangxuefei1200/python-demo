#获取目录下的文件

from pathlib import *

print('---------获取指定目录下的所有文件和目录-----------')
p = Path('.')
x_type = ''
elements = p.glob('*')  #glob方法获取当前目录下的所有文件和目录
for x in elements:
    if x.is_dir():
        x_type = '目录'
    elif x.is_file():
        x_type = '文件'
    print(f"{x_type}:{x}")

print('\n\n---------获取指定目录及其子目录下的所有文件和目录-----------')
p = Path('.')
x_type = ''
elements = p.rglob('*')  #rglob方法获取当前目录及其子目录下的所有文件和目录
for x in elements:
    if x.is_dir():
        x_type = '目录'
    elif x.is_file():
        x_type = '文件'
    print(f"{x_type}:{x}")

print('\n\n---------获取指定匹配规则的所有文件和目录-----------')
p = Path('.')
x_type = ''
#elements = p.rglob('*.py')
#elements = p.rglob('*.txt')
elements = p.rglob('*test*.py')
for x in elements:
    if x.is_dir():
        #x_type = '目录'
        continue
    elif x.is_file():
        x_type = '文件'
    print(f"{x_type}:{x}")
    print(type(x))




