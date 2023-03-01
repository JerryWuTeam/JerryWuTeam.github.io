import time
import os
import sys
import pyperclip
n = int(input('位数> '))


def ref(a, b):
    strarrs = [' . ', '. .', '...']
    sys.stdout.write(f'[{a+1}/{b}]'+strarrs[a % 3]+'\r')
    sys.stdout.flush()


def get_pi(n):
    t = n+10  # 多计算10位，防止尾数取舍的影响
    b = 10**t  # 为算到小数点后t位，两边乘以10^t
    x1 = b*4//5  # 取整求含4/5的首项
    x2 = b // -239  # 取整求含1/239的首项
    s = x1+x2  # 求第一大项
    n *= 2  # 设置下面循环的终点，即共计算n项
    for i in range(3, n, 2):  # 循环初值=3，末值n,步长=2
        x1 //= -25  # 取整求每个含1/5的项及符号
        x2 //= -57121  # 取整求每个含1/239的项及符号
        x = (x1+x2) // i  # 求两项之和，除以对应因子，取整
        s += x  # 求总和
        ref(int((i-1)/2), int(n/2))
        # print('\r', "{:d}".format(15-i), end='', flush=True)
        # print(f'[{(i-1)/2}/{n/2}]\n')
    pi = s*4  # 求出π
    pi //= 10**10  # 舍掉后十位

    str_list = list(str(pi))
    str_list.insert(1, '.')
    a_b = ''.join(str_list)

    return a_b


pi = get_pi(n)
print(pi)
pyperclip.copy(pi)
input('结果已拷贝至粘贴板\n按Enter键以退出')
