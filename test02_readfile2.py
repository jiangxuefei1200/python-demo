import re, fileinput

def file_read1():
    with open('.\\fileDirectory\\testfile1.txt', 'r', buffering=True, encoding='utf-8') as f:
        content = f.read()
        print(content)

def file_read2():
    with open('.\\fileDirectory\\testfile1.txt', 'r', buffering=True, encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')

def file_read3():
    with open('.\\fileDirectory\\testfile1.txt', 'r', buffering=True, encoding='utf-8') as f:
        for line in f:
            print(line, end='')

def file_read4():
    line_number = 0
    results = []
    with open('.\\fileDirectory\\testfile1.txt', 'r', buffering=True, encoding='utf-8') as f:
        #pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}' #邮箱
        pattern = r'1[3578][0-9]{9}' #手机号码
        for line in f:
            line_number += 1
            match = re.search(pattern, line)
            if match:
                results.append({
                    'line': line_number,
                    'content': line.rstrip('\n'),  # 移除换行符
                    'match': match
                })
    # 打印结果
    if results:
        for item in results:
            print(f"行 {item['line']}: {item['content']}")
            print(f"匹配内容: {item['match'].group()}\n")
    else:
        print(f"在文件中未找到匹配")


def file_read5():
    line_number = 0
    results = []
    with open('.\\fileDirectory\\testfile1.txt', 'r', buffering=True, encoding='utf-8') as f:
        pattern = r'@@\w+@@'
        for line in f:
            line_number += 1
            matches = re.findall(pattern, line, flags=0)
            if matches:
                results.append({
                    'line': line_number,
                    'content': line.rstrip('\n'),  # 移除换行符
                    'matches': matches
                })
    # 打印结果
    if results:
        for item in results:
            print(f"行 {item['line']}: {item['content']}")
            print("匹配内容:", end='')
            for e in item['matches']:
                print(e, end=',')
            print("\n")
    else:
        print(f"在文件中未找到匹配")

def file_read6():
    files=('.\\fileDirectory\\fileDirectory_child1\\testfile_child1.txt',
           '.\\fileDirectory\\fileDirectory_child1\\testfile_child2.txt')
    with fileinput.input(files=files, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')

if __name__ == '__main__':
    file_read5()
