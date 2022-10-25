#chapter 7

from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
#calculate cdf/pmf of binomial
print(stats.binom.pmf(0,5,0.25))
print(stats.binom.pmf(4,5,0.25) + stats.binom.pmf(5,5,0.25))
print(1-stats.binom.cdf(3,5,0.25))


#환자 문제
rv_patint = stats.binom(15,0.5)
print(rv_patint.cdf(6))
print(stats.binom.cdf(6, 15,0.5))
print(stats.binom.cdf(10, 15,0.5) - stats.binom.cdf(5, 15,0.5))
print(1-stats.binom.cdf(11, 15,0.5))


print(stats.binom.cdf(10,200,0.04))
print(stats.binom.pmf(12,15,0.5))


print('xxxxxxxxx')

print(stats.binom.pmf(0, 100, 0.01))




#rv = stats.binom(n,p)
x = np.arange(0, 16)
print(x)
print(stats.binom.pmf(x, 15, 0.5))

plt.figure()
plt.plot(x, stats.binom.pmf(x, 15, 0.5), 'bo')
plt.vlines(x, 0, stats.binom.pmf(x, 15, 0.5), lw=2)
plt.xlabel('# of patients cured')
plt.ylabel('binomial')
plt.show()

#hypergeom
[M, n, N] = [48, 8, 12]
rv = stats.hypergeom(M, n, N)
print("cccccccccccccc")
print(rv.pmf(0))


x = np.arange(0, n+1)
pmf_cars = rv.pmf(x)

rv_dogs = stats.hypergeom(200,12,7)
x = np.arange(0, 13)
pmf_dogs = rv_dogs.cdf(x)

plt.figure()
plt.plot(x, pmf_dogs, 'bo')
plt.vlines(x, 0, pmf_dogs, lw=2)
plt.xlabel('# of dogs in our group of chosen animals')
plt.ylabel('hypergeom PMF')
plt.show()

#calculate cdf of poisson


from scipy import stats
print(stats.poisson.cdf(100,80))
print(stats.binom.cdf(100, 200, 0.04))


#실습
#분 단위로 끊자(5.5분 말고 5분, 6분)
