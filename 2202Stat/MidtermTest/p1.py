#201811194 이진욱

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

#p(1- 12번 미만에서 10번 성공하는 경우)
#11번까지의 시도에서 10번을 성공해야 한다.
# = 10번 연달아 성공하는 경우 + 10번 이전에 한 번 실패하고 11번째에 성공하는 경우

#a = 10번 연달아 성공하는 확률
a = 0.7 * 0.7 * 0.7 * 0.7 * 0.7 * 0.7 * 0.7 * 0.7 * 0.7 * 0.7
#b = 중간에 한 번 실패 후 11번째에 성공하는 확률
b = 0.7 * 0.7 * 0.7 * 0.7 * 0.7 * 0.7 * 0.7 * 0.7 * 0.7 * 0.3 * 0.7 * 10
#c = 두 확률의 합
c = a+b
#d = 12번 이상 시도해야 할 확률 = 1-c
d = 1-c

print(d)