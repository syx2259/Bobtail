import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from decimal import Decimal
#read data1
data1 = open("C:/Users/Ryan/Desktop/22Spring/Cloud Computing/final project/Mid term/experiment1/rtt.txt","r")
content = data1.read().split("\n")
content = np.array(content,dtype='d')
content = sorted(content)
a = content[int(0.999*len(content)):]
loc = np.mean(a, dtype='d')
scale = np.var(a, dtype='d')

cdf_values1 = stats.norm.cdf(a,loc=loc,scale=scale)

#read data2
data2 = open("C:/Users/Ryan/Desktop/22Spring/Cloud Computing/final project/Mid term/experiment1/rtt_one_cpu_intensive.txt","r")
content2 = data2.read().split("\n")
content2 = np.array(content2,dtype='d')
content2 = sorted(content2)
b = content2[int(0.999*len(content2)):]
loc2 = np.mean(b, dtype='d')
scale2 = np.var(b, dtype='d')
cdf_values2 = stats.norm.cdf(b,loc=loc2,scale=scale2)

#read data3
data3 = open("C:/Users/Ryan/Desktop/22Spring/Cloud Computing/final project/Mid term/experiment1/rtt_two_cpu_intensive.txt","r")
content3 = data3.read().split("\n")
content3 = np.array(content3,dtype='d')
content3 = sorted(content3)
c = content3[int(0.999*len(content3)):]
loc3 = np.mean(c, dtype='d')
scale3 = np.var(c, dtype='d')
cdf_values3 = stats.norm.cdf(c,loc=loc3,scale=scale3)

#read data4
data4 = open("C:/Users/Ryan/Desktop/22Spring/Cloud Computing/final project/Mid term/experiment1/rtt_three_cpu_intensive.txt","r")
content4 = data4.read().split("\n")
content4 = np.array(content4,dtype='d')
content4 = sorted(content4)
d = content4[int(0.999*len(content4)):]
loc4 = np.mean(d, dtype='d')
scale4 = np.var(d, dtype='d')
cdf_values4 = stats.norm.cdf(d,loc=loc4,scale=scale4)

#read data5
data5 = open("C:/Users/Ryan/Desktop/22Spring/Cloud Computing/final project/Mid term/experiment1/rtt_four_cpu_intensive.txt","r")
content5 = data5.read().split("\n")
content5 = np.array(content5,dtype='d')
content5 = sorted(content5)
e = content5[int(0.999*len(content5)):]
loc5 = np.mean(e, dtype='d')
scale5 = np.var(e, dtype='d')
cdf_values5 = stats.norm.cdf(e,loc=loc5,scale=scale5)




# plot the sorted data:
plt.plot(a, cdf_values1,color='blue', label='0 CPU-Intensive')
plt.plot(b, cdf_values2,color='green', label='1 CPU-Intensive')
plt.plot(c, cdf_values3,color='red', label='2 CPU-Intensive')
plt.plot(d, cdf_values4,color='skyblue', label='3 CPU-Intensive')
plt.plot(e, cdf_values5,color='yellow', label='4 CPU-Intensive')

#plt.ylim((0.999,1.0001))
#my_y_ticks = np.arange(0.999,1,0.0001)
plt.legend()
plt.xlabel('RTT(s)')
plt.ylabel('CDF of RTT')
#plt.yticks(my_y_ticks)
plt.title("CDF")
plt.show()
