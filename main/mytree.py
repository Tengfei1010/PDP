import linecache
import os
import time

__author__ = 'kevin'
_BASE_PATH = os.path.abspath('../')
_FILE_DIR = _BASE_PATH + '/file/'

_LINE_COUNT = 1000


def main():
    pass


def init_file(file_name, line_count):
    if os.path.exists(_FILE_DIR + file_name):
        os.remove(_FILE_DIR + file_name)
    with open(_FILE_DIR + file_name, 'w') as f:
        f.writelines(str(line_count) + '\n')
        for i in range(line_count):
            f.writelines(str(i + 1) + ',' + str(i + 1) + '\n')
        # f.writelines('\n')
        f.close()


def gen_father_node(file_name):
    if not os.path.exists(_FILE_DIR + file_name):
        raise
    _FILE_NAME = _FILE_DIR + file_name
    try:
        input = open(_FILE_DIR + file_name, 'r')
        output = open(_FILE_DIR + file_name, 'a')
        line_count = input.readline()
        line_count = int(line_count)
        count = 2
        cursor = 1
        while True:
            a = linecache.getline(_FILE_NAME, count)
            b = linecache.getline(_FILE_NAME, count + 1)
            if (len(a) > 1) and (len(b) > 2):
                a = (a.split(','))[1]
                b = (b.split(','))[1]
                c = int(a) + int(b)
                output.writelines(str(line_count + cursor) + ',' + str(c) + '\n')
                cursor += 1
                count += 2
            else:
                break
    except:
        raise
    finally:
        input.close()
        output.close()

def test(file_name):
    s = linecache.getline(_FILE_DIR + file_name, 1004)
    print(len(s))

if __name__ == '__main__':
    start = time.time()
    init_file('test.txt', _LINE_COUNT)
    end = time.time()
    print(end - start)
    gen_father_node('test.txt')
    # test('test.txt')