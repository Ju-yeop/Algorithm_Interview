import os
import random
import time
from sys import stdin

ls = [0 for _ in range(40)]
s = 0
for _ in range(5):
    temp = random.randrange(40)
    ls[temp] = 8
    for i in range(40):
        print('%2d ' % i, end='')
    print('')
    for j in range(40):
        print('%2d ' % ls[j], end='')
    print('')
    time.sleep(2)
    os.system('cls')

    N = int(input('8자 어디에? : '))
    if N == temp:
        s = s + 1
        print('\n%d번 맞췄음' % s)
    else:
        print('\n 틀렸음, 맞춘 횟수 = %d' % s)
    ls[temp] = 0
input()