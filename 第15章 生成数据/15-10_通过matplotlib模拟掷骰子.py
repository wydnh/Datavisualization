from die import Die
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(50000):
    # result = die_1.roll()
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
# max_results = die_1.num_sides
max_results = die_1.num_sides + die_2.num_sides
X_Range = list(set(results)) # set()去重
for value in X_Range:
    frequency = results.count(value)
    frequencies.append(frequency)

plt.bar(X_Range, frequencies, color='Pink', align='center', label='D6+D6')
plt.xticks(X_Range)

plt.xlabel("Results", fontsize=8)
plt.ylabel("Frequencies", fontsize=8)

# 图例
pink_patch = mpatches.Patch(color='Pink', label='D6+D6')
plt.legend(handles=[pink_patch])

plt.show()
