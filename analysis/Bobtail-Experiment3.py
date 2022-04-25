import numpy
import matplotlib.pyplot as plt

good_file = open("C:/Users/Ryan/Desktop/good.txt","r")
bad_file = open("C:/Users/Ryan/Desktop/experiment3_cpu1.txt","r")
good_delays = [int(i) for i in good_file.readlines()]
bad_delays = [int(i) for i in bad_file.readlines()]
good_delays.sort()
bad_delays.sort()
print(good_delays)
print(bad_delays)
def count_false_positive_nums_LOW_MARK(mark, bad_delays):
    count = 0
    for each in bad_delays:
        if each <= mark:
            count += 1
        else:
            break
    return count

def count_false_negative_nums_LOW_MARK(mark, good_delays):
    count = 0
    for each in good_delays:
        if each >= mark:
            count += 1
    return count

def count_false_positive_nums_HIGH_MARK(mark, bad_delays):
    count = 0
    for each in bad_delays:
        if each <= mark:
            count += 1
        else:
            break
    return count

def count_false_negative_nums_HIGH_MARK(mark, good_delays):
    count = 0
    for each in good_delays:
        if each >= 5 * mark:
            count += 1
    return count

# calculate the false positive rates and false negative rates with LOW_MARK
false_positive_rates_LOW_MARK = []
false_negative_rates_LOW_MARK = []
for i in range(0,500):
    false_positive_nums_LOW_MARK = count_false_positive_nums_LOW_MARK(i, bad_delays)
    false_positive_rates_LOW_MARK.append(false_positive_nums_LOW_MARK / 100)

    false_negative_nums_LOW_MARK = count_false_negative_nums_LOW_MARK(i, good_delays)
    false_negative_rates_LOW_MARK.append(false_negative_nums_LOW_MARK / 100)
print (false_positive_rates_LOW_MARK)
print (false_negative_rates_LOW_MARK)

# calculate the false positive rates and false negative rates with HIGH_MARK
false_positive_rates_HIGH_MARK = []
false_negative_rates_HIGH_MARK = []
for i in range(0,500):
    false_positive_nums_HIGH_MARK = count_false_positive_nums_HIGH_MARK(i, bad_delays)
    false_positive_rates_HIGH_MARK.append(false_positive_nums_HIGH_MARK / 100)

    false_negative_nums_HIGH_MARK = count_false_negative_nums_HIGH_MARK(i, good_delays)
    false_negative_rates_HIGH_MARK.append(false_negative_nums_HIGH_MARK / 100)
print (false_positive_rates_HIGH_MARK)
print (false_negative_rates_HIGH_MARK)

plt.plot(false_positive_rates_LOW_MARK, false_negative_rates_LOW_MARK, label='Low Mark')
plt.plot(false_positive_rates_HIGH_MARK, false_negative_rates_HIGH_MARK, label='High Mark')
plt.plot()
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.0])
plt.legend()
plt.xlabel("False Positive Rate")
plt.ylabel("False Negative Rate")
plt.show()