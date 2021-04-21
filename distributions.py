# Jesus is Great!

#_____________________________poisson
from scipy.stats import poisson
import matplotlib.pyplot as plt

#Use the Probability mass function to calculate P(X=0)
# x = 0, lambda = 6 

x = 0 # change the values to 0,1,2,3,4,5,6
lmbda = 6
p= poisson.pmf(x,lmbda)
p

#_________________normal dist
import scipy.stats as stats
x = 700
mean_marks = 494
sd_marks = 100
prob=stats.norm.cdf((x-mean_marks)/sd_marks)
prob
print(' Probability that a randomly selected student will have marks more than 700 is {:.2f}%'.format((1-prob)*100))

#__________binomial
from scipy.stats import binom 
# setting the values 
# of n and p 
n = 30
p = 0.1
# defining the list of r values 
x_values = [0,1,2,3]
x_values
bp = binom.pmf(x_values, n, p)
bp
bp.sum()

#__________uniform
a = 750
b = 800
diff1 = b-a
diff1
x1 = 770
x2 = 780
diff2 = x2-x1
diff2
p_x = diff2/diff1
p_x

#________________________Factorial

8*7*6*5*4*3*2

num = 4
factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#____________ncr 
import math 
from math import comb
comb(n, r) # calculates "n choose r" aka nCr aka binomial coefficients


























