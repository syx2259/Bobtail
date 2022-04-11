import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from decimal import Decimal
#read data1
data1 = open("C:/Users/Ryan/Desktop/results/delayFile_zero.txt","r")
content1 = [i[:-1].split(',') for i in data1.readlines()]
content1 = list(map(list, zip(*content1)))
time1 = np.array(content1[0],dtype='d')
num1 = np.array(content1[1],dtype='int')


#read data2
data2 = open("C:/Users/Ryan/Desktop/results/delayFile_one.txt","r")
content2 = [i[:-1].split(',') for i in data2.readlines()]
content2 = list(map(list, zip(*content2)))
time2 = np.array(content2[0],dtype='d')
num2 = np.array(content2[1],dtype='int')

#read data3
data3 = open("C:/Users/Ryan/Desktop/results/delayFile_two.txt","r")
content3 = [i[:-1].split(',') for i in data3.readlines()]
content3 = list(map(list, zip(*content3)))
time3 = np.array(content3[0],dtype='d')
num3 = np.array(content3[1],dtype='int')

#read data4
data4 = open("C:/Users/Ryan/Desktop/results/delayFile_three.txt","r")
content4 = [i[:-1].split(',') for i in data4.readlines()]
content4 = list(map(list, zip(*content4)))
time4 = np.array(content4[0],dtype='d')
num4 = np.array(content4[1],dtype='int')

#read data5
data5 = open("C:/Users/Ryan/Desktop/results/delayFile_four.txt","r")
content5 = [i[:-1].split(',') for i in data5.readlines()]
content5 = list(map(list, zip(*content5)))
time5 = np.array(content5[0],dtype='d')
num5 = np.array(content5[1],dtype='int')



# plot the sorted data:
plt.plot(time1, num1,color='blue', label='0 CPU-Intensive')
plt.plot(time2, num2,color='red', label='1 CPU-Intensive')
plt.plot(time3, num3,color='yellow', label='2 CPU-Intensive')
plt.plot(time4, num4,color='green', label='3 CPU-Intensive')
plt.plot(time5, num5,color='skyblue', label='4 CPU-Intensive')

plt.yscale('log')
plt.legend()
plt.xlabel('Time(s)')
plt.ylabel('Cumulative # of samples >= 10ms')
plt.show()
