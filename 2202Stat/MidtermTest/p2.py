#201811194 이진욱


import numpy as np

#x = 마그네슘의 양
x = np.array([8.7, 9, 11, 8.5, 9.2, 12, 12, 18])

#y = 물의 맛에 대한 만족도
y = np.array([25, 25, 26, 48, 65, 87, 90, 100])

#calculate the correlation

import numpy as np

#x 와 y 의 상관계수를 계산한다 절댓값 1에 가까울수록 강한 연관이 있다고 여기면 된다.
#그 값이 0.73에 근사하므로 물의 맛과 마그네슘의 양에는 강한 상관관계가 있다고 볼 수 있다.
print(np.corrcoef(x,y)[0][1])
