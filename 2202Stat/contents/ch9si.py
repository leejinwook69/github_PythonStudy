import numpy as np
a = np.random.randint(0, 100, size=5)

b = np.random.randint(0, 100, size=5)

np.random.seed(1)
c = np.random.randint(0, 100, size=5)

np.random.seed(1)
d = np.random.randint(0, 100, size=5)

print("a :", a)
print("b :", b)
print("c :", c)
print("d :", d)


import numpy as np
m = []
#np.random.seed()
for i in range(100):
    sample=np.random.randint(0, 10, size = 5)
    m.append(np.mean(sample))
m = np.array(m)

print(m)


##히스토그램

import matplotlib.pyplot as plt
plt.hist(m, bins=9)
plt.xlabel('m')
plt.ylabel('Frequency')
plt.title('Historam of m')
#plt.show()

#정규 확률 그림
import matplotlib.pyplot as plt
import statsmodels.api as sm


sm.qqplot(m,line='s')
plt.title("Normal Q-Q plot")
#plt.show()



from scipy.stats import norm
import math
print(norm.cdf(x=83.2,loc=82,scale=math.sqrt(144/64)))
x_cdf = norm.cdf(x=[80.8, 83.2], loc=82, scale=math.sqrt(144/64))
print(x_cdf[1]-x_cdf[0])
